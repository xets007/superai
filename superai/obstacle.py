import os
import sys
import time

import cv2
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

from superai.gameapi import GameApiInit, GetSeceneInfo, FlushPid, GetMenInfo, GetMonsters, GetGoods, IsManInMap, \
    GetNextDoor


def main():
    if GameApiInit():
        print("Init helpdll-xxiii.dll ok")
    else:
        print("Init helpdll-xxiii.dll err")
        exit(0)
    FlushPid()

    while True:

        dixinglst, dixingvec, obstacles, wh = GetSeceneInfo()
        # print("宽高: %s" % wh)
        img = np.zeros((wh.h, wh.w, 3), dtype=np.uint8)
        img[np.where(img == [0])] = [255]

        if IsManInMap():
            for v in dixinglst:
                cv2.rectangle(img, (v.x, v.y), (v.x + 0x10, v.y + 0xc), (64, 64, 64), -1)

            for v in dixingvec:
                cv2.rectangle(img, (v.x, v.y), (v.x + 0x10, v.y + 0xc), (64, 64, 64), -1)

            for v in obstacles:
                halfw = int(v.w / 2)
                halfh = int(v.h / 2)
                cv2.rectangle(img, (v.x - halfw, v.y - halfh), (v.x + halfw, v.y + halfh), (64, 64, 64), -1)

            meninfo = GetMenInfo()
            halfw = int(meninfo.w / 2)
            halfh = int(meninfo.h / 2)
            cv2.rectangle(img, (int(meninfo.x) - halfw, int(meninfo.y) - halfh),
                          (int(meninfo.x) + halfw, int(meninfo.y) + halfh),
                          (0, 0, 255), -1)

            monsters = GetMonsters()
            for mon in monsters:
                halfw = int(mon.w / 2)
                halfh = int(mon.h / 2)
                cv2.rectangle(img, (int(mon.x) - halfw, int(mon.y) - halfh),
                              (int(mon.x) + halfw, int(mon.y) + halfh),
                              (51, 255, 255), -1)

            goods = GetGoods()
            for good in goods:
                halfw = int(good.w / 2)
                halfh = int(good.h / 2)
                cv2.rectangle(img, (int(good.x) - halfw, int(good.y) - halfh),
                              (int(good.x) + halfw, int(good.y) + halfh),
                              (51, 255, 255), -1)

            nextdoor = GetNextDoor()
            cv2.rectangle(img, (nextdoor.x, nextdoor.y), (nextdoor.x + nextdoor.w, nextdoor.y + nextdoor.h), (255, 144, 30), -1)

            cv2.imshow('img', img)
            if (cv2.waitKey(30) & 0xFF) in [ord('q'), 27]:
                break
            time.sleep(0.3)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
