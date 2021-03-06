#!python3
#encoding:utf-8
import os.path
import getpass
import Data
import command.miscellaneous.Licenses
class Main:
    def __init__(self, user_name, path_db_account, path_db_repo, path_db_license):
        self.data = Data.Data(user_name, path_db_account, path_db_repo, path_db_license)
        self.licenses = command.miscellaneous.Licenses.Licenses(self.data)
    def Run(self):
        license_key = 'start'
        while '' != license_key:
            print('入力したKeyのライセンスを問い合わせます。(未入力+Enterで終了)')
            print('サブコマンド    l:既存表示  m:一覧更新')
            key = input()
            if '' == key:
                break
            elif 'l' == key or 'L' == key:
                self.licenses.Show()
            elif 'm' == key or 'M' == key:
                self.licenses.Update()
            else:
                self.licenses.InsertOne(key)


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

