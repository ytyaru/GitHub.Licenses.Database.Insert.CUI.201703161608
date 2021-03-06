﻿# このソフトウェアについて

ライセンスのキー名をCUIで入力しライセンスDBに挿入する。

# 前回まで

* https://github.com/ytyaru/GitHub.Licenses.Database.Insert.201703141133
* https://github.com/ytyaru/GitHub.Licenses.Database.Insert.Pagenation.201703142055
* https://github.com/ytyaru/GitHub.Licenses.Database.Create.201703140852

LicenseマスターDBを作るのは難しい。APIで一覧取得しても全件取得できない。たとえばCC0ライセンスが取得できない。そこで今回はCUIでキー名を入力して存在すればDB登録するようにした。

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
    * [requests](http://requests-docs-ja.readthedocs.io/en/latest/)
    * [dataset](https://github.com/pudo/dataset)
* [SQLite3](https://www.sqlite.org/index.html) 3.8.2

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 準備

## 必要なデータベースを作成する

* [GitHub.Accounts.Database](https://github.com/ytyaru/GitHub.Accounts.Database.20170107081237765)
    * [GiHubApi.Authorizations.Create](https://github.com/ytyaru/GiHubApi.Authorizations.Create.20170113141429500)
* [GitHub.Repositories.Database.Create](https://github.com/ytyaru/GitHub.Repositories.Database.Create.20170114123411296)
* [GitHub.Licenses.Database.Create.201703140852](https://github.com/ytyaru/GitHub.Licenses.Database.Create.201703140852)

## 設定

`Main.py`の以下コードで、GitHubユーザ名とDBパスを任意に設定する。

```python
if __name__ == "__main__":
	github_user_name = 'ytyaru'
	os_user_name = getpass.getuser()
	device_name = 'some_device'
	path_db_base = 'db/GitHub'
	path_db_account = '/media/{0}/{1}/{2}/GitHub.Accounts.sqlite3'.format(os_user_name, device_name, path_db_base)
	path_db_repo = '/media/{0}/{1}/{2}/GitHub.Repositories.{3}.sqlite3'.format(os_user_name, device_name, path_db_base, github_user_name)
	path_db_license = '/media/{0}/{1}/{2}/GitHub.Licenses.sqlite3'.format(os_user_name, device_name, path_db_base)
	main = Main(github_user_name, path_db_account, path_db_repo, path_db_license)
	main.Run()
```

# 実行

```sh
python3 Main.py
```

```sh
入力したKeyのライセンスを問い合わせます。(未入力+Enterで終了)
サブコマンド    l:既存表示  m:一覧更新
```

* `l:既存表示`はDBレコードの内容を一覧表示する
* `m:一覧更新`はAPIで一覧を取得する

APIで一覧取得しても、すべてのライセンスを取得できるわけではない。たとえばCC0ライセンスが取得できない。
そこで今回CUIでライセンスのキー名を入力し、APIで問い合わせ、存在すればDBに登録する。たとえばCC0なら以下のキー名。

```sh
cc0-1.0
```

キー名はGitHubサイトのリポジトリページに記載されてある。すべてのキー名一覧ページは見つけられなかった。

# 結果

* `GitHub.Licenses.sqlite3`ファイルにライセンスデータが挿入される

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)
