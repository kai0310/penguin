from django.conf import settings
from django.contrib import messages
from django.contrib.auth import mixins
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from period import models as period_models
from period.functions import is_active
from theme import forms, models


class SubmitView(mixins.LoginRequiredMixin, generic.FormView):
    """統一テーマ案応募
    """
    template_name = 'theme/submit.html'
    form_class = forms.SubmitForm
    success_url = reverse_lazy('theme:submit')

    def get(self, request, **kwargs):
        # 個人情報が登録されていない場合は登録を促す
        if not request.user.email:
            messages.error(request, 'まず個人情報を入力してください')
            return redirect('home:signup_token')

        # 期間外の場合は 403
        if not is_active(period_models.PeriodThemeSubmit):
            raise PermissionDenied

        return super().get(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 応募済みのデータ（なければ None)
        context['submitted_data'] = models.Theme.objects.filter(
            writer=self.request.user
        ).first()

        return context

    def form_valid(self, form):
        # すでに応募済みの場合は 403
        if models.Theme.objects.filter(writer=self.request.user).exists():
            raise PermissionDenied

        # 期間外の場合は 403
        if not is_active(period_models.PeriodThemeSubmit):
            raise PermissionDenied

        # インスタンスを作成
        theme = models.Theme.objects.create(
            writer=self.request.user,
            **form.cleaned_data
        )
        theme.save()

        # message を登録
        messages.success(self.request, '応募しました！')

        return super().form_valid(form)


class FirstVoteView(mixins.LoginRequiredMixin, generic.TemplateView):
    """統一テーマ案予選投票
    """
    template_name = 'theme/first_vote.html'

    def get(self, request, **kwargs):
        # 期間外の場合は 403
        if not is_active(period_models.PeriodThemeFirstVote):
            raise PermissionDenied

        return super().get(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 予選コードが振られた統一テーマ一覧
        context['theme_list'] = models.Theme.objects.filter(
            first_id__isnull=False
        )

        # 予選投票済みかどうか
        context['voted'] = models.FirstVoteEptid.objects.filter(
            eptid=self.request.user.shib_eptid
        ).exists()

        # BASE_URL（ツイート用）
        context['base_url'] = settings.BASE_URL

        return context


def first_vote(request, pk):
    """統一テーマ予選投票処理
    """
    # 期間外の場合は 403
    if not is_active(period_models.PeriodThemeFirstVote):
        raise PermissionDenied

    # すでに投票済みの場合は 403
    if models.FirstVoteEptid.objects.filter(
        eptid=request.user.shib_eptid
    ).exists():
        raise PermissionDenied

    # テーマを指定
    theme = get_object_or_404(models.Theme, pk=pk)

    # 投票データを登録
    obj = models.FirstVote.objects.create(
        theme=theme
    )
    obj.save()
    obj_eptid = models.FirstVoteEptid.objects.create(
        eptid=request.user.shib_eptid
    )
    obj_eptid.save()

    # message を登録
    messages.success(request, '投票しました！')

    return redirect('theme:first_vote')


class FinalVoteView(mixins.LoginRequiredMixin, generic.TemplateView):
    """統一テーマ案決選投票
    """
    template_name = 'theme/final_vote.html'

    def get(self, request, **kwargs):
        # 期間外の場合は 403
        if not is_active(period_models.PeriodThemeFinalVote):
            raise PermissionDenied

        return super().get(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 決選コードが振られた統一テーマ一覧
        context['theme_list'] = models.Theme.objects.filter(
            final_id__isnull=False
        )

        # 決選投票済みかどうか
        context['voted'] = models.FinalVoteEptid.objects.filter(
            eptid=self.request.user.shib_eptid
        ).exists()

        # BASE_URL（ツイート用）
        context['base_url'] = settings.BASE_URL

        return context


def final_vote(request, pk):
    """統一テーマ決選投票処理
    """
    # 期間外の場合は 403
    if not is_active(period_models.PeriodThemeFinalVote):
        raise PermissionDenied

    # すでに投票済みの場合は 403
    if models.FinalVoteEptid.objects.filter(
        eptid=request.user.shib_eptid
    ).exists():
        raise PermissionDenied

    # テーマを指定
    theme = get_object_or_404(models.Theme, pk=pk)

    # 投票データを登録
    obj = models.FinalVote.objects.create(
        theme=theme
    )
    obj.save()
    obj_eptid = models.FinalVoteEptid.objects.create(
        eptid=request.user.shib_eptid
    )
    obj_eptid.save()

    # message を登録
    messages.success(request, '投票しました！')

    return redirect('theme:final_vote')
