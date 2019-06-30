import sys
import os
import time

import win32con
import win32gui
from win32api import Sleep

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

import math

from superai.yijianshu import YijianshuInit, DownZUO, DownYOU, DownXIA, DownSHANG, DownZUOSHANG, DownZUOXIA, \
    DownYOUSHANG, DownYOUXIA, UpZUO, UpYOU, UpSHANG, UpXIA, UpZUOSHANG, UpZUOXIA, UpYOUSHANG, UpYOUXIA, PressRight, \
    PressLeft, JiPaoZuo, JiPaoYou

from superai.gameapi import GameApiInit, FlushPid, PrintMenInfo, PrintMapInfo, PrintSkillObj, PrintNextMen, PrintMapObj, \
    GetMonsters, IsLive, HaveMonsters, NearestMonster, GetMenXY, GetQuadrant, Quardant, IsClosed, GetFangxiang, \
    GetMenChaoxiang, RIGHT, WithInDistance, WithInDistanceExtra

QuadKeyDownMap = {
    Quardant.ZUO: DownZUO,
    Quardant.YOU: DownYOU,
    Quardant.SHANG: DownSHANG,
    Quardant.XIA: DownXIA,
    Quardant.ZUOSHANG: DownZUOSHANG,
    Quardant.ZUOXIA: DownZUOXIA,
    Quardant.YOUSHANG: DownYOUSHANG,
    Quardant.YOUXIA: DownYOUXIA
}

QuadKeyUpMap = {
    Quardant.ZUO: UpZUO,
    Quardant.YOU: UpYOU,
    Quardant.SHANG: UpSHANG,
    Quardant.XIA: UpXIA,
    Quardant.ZUOSHANG: UpZUOSHANG,
    Quardant.ZUOXIA: UpZUOXIA,
    Quardant.YOUSHANG: UpYOUSHANG,
    Quardant.YOUXIA: UpYOUXIA
}


class StateMachine:
    currentState = None

    owner = None

    def __init__(self, owner):
        self.owner = owner

    def ChangeState(self, newState):
        self.currentState = newState

    def Update(self):
        if self.currentState is not None:
            self.currentState.Execute(self.owner)


class Player:
    # 状态机
    stateMachine: StateMachine

    # 上一次按下的键
    latestDown = None

    # 正在疾跑
    injipao = False

    def __init__(self):
        self.stateMachine = StateMachine(self)

    def ChangeState(self, state):
        self.stateMachine.ChangeState(state)

    def Update(self):
        self.stateMachine.Update()

    # 靠近
    def Seek(self, objx, objy):
        menx, meny = GetMenXY()

        # 是否在范围内
        if IsClosed(menx, meny, objx, objy):
            print("seek: 目标(%.f, %.f)在范围内" % (objx, objy))

            # 上一次的按键恢复
            self.UpLatestKey()
            self.ChaoxiangFangxiang(menx, objx)

        else:
            quad = GetQuadrant(menx, meny, objx, objy)

            withined, dis, kuandu, changdu = WithInDistanceExtra(menx, meny, objx, objy)
            jipao = not withined

            print("seek: 目标: %s 在慢走范围内: %d 疾跑: %d 距离: %d 宽度: %d 长度: %d" %
                  (quad.name, withined, jipao, dis, kuandu, changdu))

            if self.KeyDowned():
                # 疾跑
                if self.latestDown == quad:
                    print("seek: 目标(%.f, %.f)在%s, 维持" % (objx, objy, quad.name))
                elif self.SwitchFangxiang(quad):
                    print("seek: 目标(%.f, %.f)在%s, 去掉一个方向的速度" % (objx, objy, quad.name))
                else:
                    print("seek: 目标(%.f, %.f)在%s, 更换方向" % (objx, objy, quad.name))
                    self.UpLatestKey()
                    if jipao:
                        self.KeyJiPao(quad)
                    self.DownKey(quad)
            else:
                print("seek: 目标(%.f, %.f)在%s, 首次靠近" % (objx, objy, quad.name))

                if jipao:
                    self.KeyJiPao(quad)
                self.DownKey(quad)

    def ChaoxiangFangxiang(self, menx, objx):
        # 是否面向对方
        if not GetFangxiang(menx, objx) == GetMenChaoxiang():
            # 调整朝向
            if GetFangxiang(menx, objx) == RIGHT:
                PressRight()
            else:
                PressLeft()

    # 开启疾跑状态
    def KeyJiPao(self, quad):
        if self.injipao:
            return

        if quad in [Quardant.ZUO, Quardant.SHANG, Quardant.XIA, Quardant.ZUOSHANG, Quardant.ZUOXIA]:
            JiPaoZuo()

        if quad in [Quardant.YOU, Quardant.YOUSHANG, Quardant.YOUXIA]:
            JiPaoYou()

        self.injipao = True

    # 疾跑斜方向象限移动到水平或垂直位置时. 保留一个方向的速度. 并按键弹起释放另一个方向的速度
    def SwitchFangxiang(self, quad) -> bool:
        if not self.KeyDowned():
            return False
        if self.latestDown == quad:
            return False

        if self.latestDown == Quardant.ZUOSHANG:
            if quad == Quardant.ZUO:
                UpSHANG()
                self.latestDown = Quardant.ZUO
            elif quad == Quardant.SHANG:
                UpZUO()
                self.latestDown = Quardant.SHANG
            else:
                return False

        if self.latestDown == Quardant.YOUSHANG:
            if quad == Quardant.YOU:
                UpSHANG()
                self.latestDown = Quardant.YOU
            elif quad == Quardant.SHANG:
                UpYOU()
                self.latestDown = Quardant.SHANG
            else:
                return False

        if self.latestDown == Quardant.ZUOXIA:
            if quad == Quardant.ZUO:
                UpXIA()
                self.latestDown = Quardant.ZUO
            elif quad == Quardant.XIA:
                UpZUO()
                self.latestDown = Quardant.XIA
            else:
                return False

        if self.latestDown == Quardant.YOUXIA:
            if quad == Quardant.YOU:
                UpXIA()
                self.latestDown = Quardant.YOU
            elif quad == Quardant.XIA:
                UpYOU()
                self.latestDown = Quardant.XIA
            else:
                return False

        return True

    # 键已经按过
    def KeyDowned(self):
        return self.latestDown is not None

    # 重置键盘
    def ResetKey(self):
        self.latestDown = None

    # 按下键
    def DownKey(self, quad):
        QuadKeyDownMap[quad]()
        self.latestDown = quad

    # 恢复之前按的键
    def UpLatestKey(self):
        if self.KeyDowned():
            QuadKeyUpMap[self.latestDown]()
            self.ResetKey()

            # 疾跑 -> 八方位移动.  恢复站立状态 -> 疾跑状态关闭
            self.injipao = False


class State:
    def Execute(self, player):
        raise NotImplementedError()


# 图内站立
class StandState(State):
    def Execute(self, player):
        if IsLive() and HaveMonsters():
            player.ChangeState(SeekAndAttackMonsterInstance)


# 靠近并攻击怪物
class SeekAndAttackMonster(State):
    def Execute(self, player):
        obj = NearestMonster()

        objx, objy = obj.x, obj.y
        menx, meny = GetMenXY()
        if IsClosed(menx, meny, objx, objy):
            # 上一次的按键恢复
            player.UpLatestKey()
            player.ChaoxiangFangxiang(menx, objx)

            print("SeekAndAttackMonster: 开始攻击 %.f, %.f" % (objx, objy))

        else:
            player.Seek(objx, objy)


StandStateInstance = StandState()
SeekAndAttackMonsterInstance = SeekAndAttackMonster()


def main():
    if GameApiInit():
        print("Init helpdll-xxiii.dll ok")
    else:
        print("Init helpdll-xxiii.dll err")
        exit(0)

    if YijianshuInit():
        print("Init 易键鼠 ok")
    else:
        print("Init 易键鼠 err")
        exit(0)

    FlushPid()

    hwnd = win32gui.FindWindow("地下城与勇士", "地下城与勇士")
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 800, 600,
                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    win32gui.SetForegroundWindow(hwnd)

    player = Player()
    player.ChangeState(SeekAndAttackMonsterInstance)

    try:
        while True:
            Sleep(100)
            player.Update()
    except KeyboardInterrupt:
        player.UpLatestKey()
        sys.exit()


if __name__ == "__main__":
    main()
