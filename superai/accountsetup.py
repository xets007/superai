import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

from superai.common import GameWindowToTop
from superai.pathsetting import GetCfgPath, GetCfgFile

settingdir = GetCfgPath()

# 当前的账号
currentaccount = None

# 当前的大区
currentregion = None


def GetAccount():
    return currentaccount


def GetRegion():
    return currentregion


def IsAccountSetted():
    return currentaccount is not None and currentregion is not None


# 打印选择
def PrintSwitchTips():
    accounts = GetSettingAccounts()
    for i, account in enumerate(accounts):
        print("%d => %s" % (i, account))
    print("输入你想选择的序号")


# 阻塞等待用户选择当前是哪个账号
def BlockGetSetting():
    accounts = GetSettingAccounts()

    while True:
        i = input()
        i = int(i)
        if i > len(accounts) or i < 0:
            print("序号超过范围")
            continue

        global currentaccount, currentregion
        currentaccount = accounts[i].account
        currentregion = accounts[i].region

        print("你当前选择的序号: %d 账号: %s 大区: %s" % (i, currentaccount, currentregion))
        break

    # GameWindowToTop()


# 设置当前选择的账号(通过自动登录)
def SetCurrentAccount(account, region):
    global currentaccount, currentregion
    currentaccount = account
    currentregion = region


# 读取文件中所有配置的账号
def GetSettingAccounts():
    accountmap = {}

    with open(GetCfgFile(), "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip('\r').strip('\n')
            vecs = line.split('----')

            regions = vecs[3].split(',')
            for region in regions:
                if region != "":

                    first = region.find('[')
                    last = region.find(']')
                    if first != -1 and last != -1:
                        region = region[0:first]

                    account = Account(vecs[0], vecs[1], vecs[2], region)

                    if account.account not in accountmap:
                        accountmap[account.account] = [account]
                    else:
                        accountmap[account.account].append(account)
    maxlen = 0

    accounts = []
    for k, v in accountmap.items():
        if len(v) > maxlen:
            maxlen = len(v)

    for i in range(maxlen):
        for k, v in accountmap.items():
            if i < len(v):
                accounts.append(v[i])

    return accounts

class Account:
    def __init__(self, account, password, phone, region):
        self.account = account
        self.password = password
        self.phone = phone
        self.region = region

    def __str__(self):
        return self.account + "/" + self.region


def main():
    accounts = GetSettingAccounts()
    for account in accounts:
        print(account)


if __name__ == '__main__':
    main()
