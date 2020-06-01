# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.conf import settings
from django.core import mail


@shared_task
def send_mail_async(
    subject,
    body,
    to_list,
    from_email=settings.EMAIL_HOST_USER,
    reply_to=['system@example.com']
):
    """メールを非同期送信する

    Note:
        to_list に 2 件以上アドレスを投入すると
        to 同士でメールアドレスが共有されます。
    """

    # reply_to などを設定した場合は適用する（**kwargs）
    mail.EmailMessage(
        subject,
        body,
        from_email,
        to_list,
        reply_to=reply_to
    ).send()
