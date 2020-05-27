# PENGUIN
この Web アプリケーションは、11 月祭に関する事務手続きを補助します。
……っていうアプリを 2 年前に開発した人です。
事務局をやめたので何の権限もありませんが、勉強も兼ねてちゃんと作り直します。

## Prerequirements
* docker-compose
* python3 (環境変数ファイルを作成するのに使います)

## How to install and run
1. `git clone git@github.com:Zoniisan/penguin.git`
1. **環境変数ファイルを作成する必要があります**。
    * `python3 create_env_file.py` を実行すればいい感じに作ってくれます。
    * 本番環境でなければ何も考えずに Enter を連打すればいいはずです。
    * `DEBUG=True` の場合はメールと slack で送信されるべき情報が標準出力に
    流れるので、メールや slack に関する設定は適当で大丈夫です。
1. `docker-compose up`

* 残念ながら Zuya は docker のことを何も知らないので（適当に調べて Dockerfile などを
作りました）、何か不備があったらごめんなさい。
* 現時点では本番環境での動作を想定していません。本番環境で使用するのは危険なのでやめましょう。
    * 具体的には、gunicorn, nginx 関連の設定をまだしていません。
    * 本番環境では Shibboleth 認証を用いることを想定していますが、現時点で対応していません。

## Post-install
* 最初は何もデータが入っていませんが、下記のコマンドを入力することで最低限のデータが入力されます。
    * `docker-compose exec web python manage.py create_models_for_dev`

### 入力されるデータ
* `home.User`
    * パスワードはすべて `hogehoge` です
    * 学生番号 `9000000000` でスーパーユーザーとしてログインできます
        * 全権を持ちます
        * システム担当に所属します
    * 学生番号 `10000000[0-9]{2}` は一般ユーザー（生徒）です
    * 学生番号 `20000000[0-9]{2}` は一般ユーザー（先生）です
        * 本番環境においては、生徒/先生を Shibboleth 認証の IDP から送信される
        データにより判別していました。
        * 「生徒以外は統一テーマ投票に投票できなくする」などの条件分岐の実装が必要になります。
    * 学生番号 `30000000[0-9]{2}` はスタッフユーザー（事務局員）です。
        * `300000000[01]` はシステム担当です。
        * `300000001[01]` は幹部です。
* `auth.Group`
    * 「システム担当」「幹部」が作成されます
* `home.OfficeGroup`
    * `auth.Group` を拡張する OneToOne モデルです
    * 「システム担当」「幹部」に対応するメールアドレスと slack ch. が登録されます
* `home.ContactKind`
    * お問い合わせの種類を登録します
    * 「11 月祭全般について」 = システム担当, 幹部のみが閲覧可
    * 「バグ報告」 = システム担当のみが閲覧可
    * 「個人情報の変更依頼」 = システム担当のみが閲覧可

* データの永続化を行っているので、`docker-compose down` しても大丈夫です。

## Current Situation
* ユーザー認証
* プロフィール確認
* 一般京大生→事務局員への「お問い合わせ」
* 事務局員→一般京大生への「通知」
    * ただし現時点ではメールの送信が非同期処理になっていないため、
    大量同時送信については実用性がありません。
* 管理サイト
* ページトップに表示される「お知らせ」の管理

などの基本的な機能を実装しています。
ここから 11 月祭特有の機能の実装に入る予定です。

ここまでの機能に関するドキュメントについては近いうちに構成します。

## Caution
* **この作品は 11 月祭および 11 月祭事務局とは一切関係ありません**。
* このアプリに関してなにか損害を被るようなことがあったとしても、一切対応しません。
* 適当に pull して遊ぶなど好きにしてもらって構いません。
    * ただし、それっぽいドメインを取得し 11 月祭事務局が運営する
    （本物の）PENGUIN と判別が難しい状態を作るのは控えたほうがいいと思います。
    個人使用の範囲内でお楽しみください。
    * `templates/base.html` に記載されたクレジット「`Bootstrapious.com`」
    については、削除することができないことになっています。


## Contact
Zuya ([twitter](https://twitter.com/Zoniichan))
