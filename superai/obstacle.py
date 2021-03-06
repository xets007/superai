import os
import sys
import time

import cv2
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))


import logging

logger = logging.getLogger(__name__)
from superai.common import InitLog
from superai.plot import DidPlotAccept
from superai.gameapi import GameApiInit, GetSeceneInfo, FlushPid, GetMenInfo, GetGoods, IsManInMap, \
    GetNextDoor, GetMapInfo, GetMonstersWrap


class GameObstacleData():
    def __init__(self, mapw, maph, dixingtree, dixingvec, dixingextra, obstacles):
        self.mapw = mapw
        self.maph = maph
        self.dixingtree = dixingtree
        self.dixingvec = dixingvec
        self.dixingextra = dixingextra
        self.obstacles = obstacles


# 获取地形 障碍 宽高
def GetGameObstacleData():
    dixingtree, dixingvec, dixingextra, obstacles, wh = GetSeceneInfo()

    for ob in obstacles:
        if ob.code == 109006963:  # 水晶柱
            ob.w = 40
            ob.h = 40
    # 109006963 问题的关键是这里为啥可以穿过去但是又穿不过去

    # 不要设置地形了. 可以走过去的
    mapinfo = GetMapInfo()
    if mapinfo.name == "城主宫殿":
        if DidPlotAccept("从天而落之物"):
            dixingtree = []
            dixingvec = []
            dixingextra = []
            obstacles = []

    wh.w += 20
    wh.h += 20

    return GameObstacleData(wh.w, wh.h, dixingtree, dixingvec, dixingextra, obstacles)


def drawDixing(img, d):
    # 地形二叉树. x,y左上角
    for v in d.dixingtree:
        cv2.rectangle(img, (v.x, v.y), (v.x + 0x10, v.y + 0xc), (144, 128, 112), 2)

    # 地形数组. x,y左上角
    for v in d.dixingvec:
        cv2.rectangle(img, (v.x, v.y), (v.x + 0x10, v.y + 0xc), (64, 64, 64), 2)

    # 地形额外. x,y左上角
    for v in d.dixingextra:
        cv2.rectangle(img, (v.x, v.y), (v.x + 0x10, v.y + 0xc), (64, 64, 64), 2)


def drawObstacles(img, d):
    # 障碍物. x,y中点
    for v in d.obstacles:
        halfw = int(v.w / 2)
        halfh = int(v.h / 2)

        # 障碍物可以被攻击
        if v.CanBeAttack() > 0:
            cv2.rectangle(img, (v.x - halfw, v.y - halfh), (v.x + halfw, v.y + halfh), (0, 255, 0), 2)
        else:
            cv2.rectangle(img, (v.x - halfw, v.y - halfh), (v.x + halfw, v.y + halfh), (64, 64, 64), 2)


def drawOther(img):

    # 人,怪物,物品. x,y中点
    meninfo = GetMenInfo()
    halfw = int(meninfo.w / 2)
    halfh = int(meninfo.h / 2)
    cv2.rectangle(img, (int(meninfo.x) - halfw, int(meninfo.y) - halfh),
                  (int(meninfo.x) + halfw, int(meninfo.y) + halfh),
                  (0, 0, 255), 2)

    monsters = GetMonstersWrap()
    for mon in monsters:
        halfw = int(mon.w / 2)
        halfh = int(mon.h / 2)
        cv2.rectangle(img, (int(mon.x) - halfw, int(mon.y) - halfh),
                      (int(mon.x) + halfw, int(mon.y) + halfh),
                      (0, 140, 255), 2)

    goods = GetGoods()
    for good in goods:
        halfw = int(20 / 2)
        halfh = int(20 / 2)
        cv2.rectangle(img, (int(good.x) - halfw, int(good.y) - halfh),
                      (int(good.x) + halfw, int(good.y) + halfh),
                      (0, 140, 255), 2)


def drawDoor(img):
    # 门. x,y 左上角
    nextdoor = GetNextDoor()
    cv2.rectangle(img, (nextdoor.x, nextdoor.y), (nextdoor.x + nextdoor.w, nextdoor.y + nextdoor.h),
                  (255, 144, 30), 2)


def drawLine(img, d):
    for i in range(d.mapw // 10):
        cv2.line(img, (i * 10, 0), (i * 10, d.maph), (144, 128, 112), 1)

    for i in range(d.maph // 10):
        cv2.line(img, (0, i * 10), (d.mapw, i * 10), (144, 128, 112), 1)


def drawAll(img, d):
    drawDixing(img, d)
    drawObstacles(img, d)
    drawOther(img)
    drawDoor(img)
    drawLine(img, d)


def drawBack(img, d):
    drawDixing(img, d)
    drawObstacles(img, d)
    drawDoor(img)
    drawLine(img, d)


def drawWithOutDoor(img, d):
    drawDixing(img, d)
    drawObstacles(img, d)
    # drawDoor(img)
    drawLine(img, d)


def loop():
    while True:
        if IsManInMap():

            d = GetGameObstacleData()
            if d.maph != 0 and d.mapw != 0:
                img = np.zeros((d.maph, d.mapw, 3), dtype=np.uint8)
            else:
                img = np.zeros((1, 1, 3), dtype=np.uint8)
            img[np.where(img == [0])] = [255]

            drawAll(img, d)

            cv2.imshow('img', img)
            if (cv2.waitKey(30) & 0xFF) in [ord('q'), 27]:
                break

        time.sleep(0.3)

    cv2.destroyAllWindows()


def main():
    InitLog()
    if not GameApiInit():
        sys.exit()
    FlushPid()

    try:
        loop()
    except KeyboardInterrupt:
        logger.info("main thread exit")
        sys.exit()


if __name__ == "__main__":
    main()
