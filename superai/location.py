import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

import logging

logger = logging.getLogger(__name__)

from superai.common import KongjianSleep
from superai.vkcode import VK_CODE
from superai.anjian import aj
from superai.flannfind import Picture, GetImgDir

locationGelanzhisen = Picture(GetImgDir() + "ditu_gelanzhisen.png")
locationTiankongzhichen = Picture(GetImgDir() + "ditu_tiankongzhicheng.png")
locationTianzhuijushou = Picture(GetImgDir() + "ditu_tianzhuijushou.png")
locationAfaliya = Picture(GetImgDir() + "ditu_afaliya2.png")
locationNuoyipeila = Picture(GetImgDir() + "ditu_nuoyipeila.png")
locationXueshan = Picture(GetImgDir() + "ditu_xueshan.png")
locationNuosimaer = Picture(GetImgDir() + "ditu_nuosimaer.png")
locationYanuofasenlin = Picture(GetImgDir() + "ditu_yanuofasenlin.png")
locationEyunzhichen = Picture(GetImgDir() + "ditu_eyun.png")
locationNiliupubu = Picture(GetImgDir() + "ditu_niliupubu.png")
locationGente = Picture(GetImgDir() + "ditu_gente.png")
locationHaigang = Picture(GetImgDir() + "ditu_xuankonghaigang.png")

wenziaierwenfangxian = Picture(GetImgDir() + "wenzi_aierwenfangxian.png", 610, 22, 182, 25)
wenzihedunmaer = Picture(GetImgDir() + "wenzi_hedunmaer.png", 610, 22, 182, 25)
wenziaerfayingdi = Picture(GetImgDir() + "wenzi_aerfayingdi.png", 610, 22, 182, 25)
wenzianheicheng = Picture(GetImgDir() + "wenzi_anheicheng.png", 610, 22, 182, 25)
wenzixihaian = Picture(GetImgDir() + "wenzi_xihaian.png", 610, 22, 182, 25)
wenzisidunxueyu = Picture(GetImgDir() + "wenzi_sidunxueyu.png", 610, 22, 182, 25)
wenzijingxiang = Picture(GetImgDir() + "wenzi_jingxiangalade.png", 610, 22, 182, 25)
wenzigente = Picture(GetImgDir() + "wenzi_gente.png", 610, 22, 182, 25)
wenzisunan = Picture(GetImgDir() + "wenzi_sunan.png", 610, 22, 182, 25)
wenzifadianzhan = Picture(GetImgDir() + "wenzi_fadianzhan.png", 610, 22, 182, 25)
wenzijijingcheng = Picture(GetImgDir() + "wenzi_jijingcheng.png", 610, 22, 182, 25)
wenzidiguizhongxin = Picture(GetImgDir() + "wenzi_diguizhongxin.png", 610, 22, 182, 25)
wenzixuankonghaigang = Picture(GetImgDir() + "wenzi_xuankonghaigang.png", 610, 22, 182, 25)

sailiya = Picture(GetImgDir() + "ditu_sailiya.png")
fuckgame = Picture(GetImgDir() + "fuckgame.png")
maptip = Picture(GetImgDir() + "maptip.png", 742, 43, 12, 13)


# 是否在赛丽亚访问
def IsinSailiya():
    if sailiya.Match():
        logger.info("在赛丽亚房间")
        return True
    else:
        # logger.warning("不在赛丽亚房间")
        return False


# 是否在艾尔文防线
def IsinAierwenfnagxian():
    if wenziaierwenfangxian.Match() or wenzisidunxueyu.Match():
        logger.info("在艾尔文防线")
        return True

    elif maptip.Match():
        pos = maptip.Pos()
        aj().MouseMoveTo(pos[0], pos[1]), KongjianSleep()
        aj().MouseLeftClick(), KongjianSleep()
        logger.info("在艾尔文防线")
        return True
    else:
        # logger.warning("不在艾尔文防线")
        return False


# 是否在赫顿玛尔
def IsinHedunmaer():
    if wenzihedunmaer.Match() or wenzixihaian.Match():
        logger.info("在赫顿玛尔")
        return True
    else:
        # logger.warning("不在赫顿玛尔")
        return False


# 是否在阿尔法营地
def IsinAerfayingdi():
    if wenziaerfayingdi.Match() or wenzianheicheng.Match():
        logger.info("在阿尔法营地")
        return True
    else:
        # logger.warning("不在阿尔法营地")
        return False


# 是否在镜像阿拉德
def IsInJingxiangalade():
    if wenzijingxiang.Match():
        logger.info("在镜像阿拉德")
        return True


# 是否在根特
def IsIngente():
    if wenzigente.Match() or wenzixuankonghaigang.Match():
        logger.info("在根特")
        return True


# 是否在素喃
def IsInSunan():
    if wenzisunan.Match():
        logger.info("在素喃")
        return True


# 是否在发电站
def IsInFadianzhan():
    if wenzifadianzhan.Match():
        logger.info("在发电站")
        return True


# 是否在寂静城
def IsInJijingchen():
    if wenzijijingcheng.Match():
        logger.info("在寂静城")
        return True


# 是否在地轨中心
def IsInDiguizhongxin():
    if wenzidiguizhongxin.Match():
        logger.info("地轨中心")
        return True


# 分解,出售,修理 单独使用吧
class Location:
    def __init__(self):
        pass

    def GetFenjieLocation(self):
        if IsinAierwenfnagxian() and locationGelanzhisen.Match():
            return "格兰之森"
        if IsinAierwenfnagxian() and locationXueshan.Match():
            return "雪山"
        elif IsinHedunmaer() and locationTiankongzhichen.Match():
            return "天空之城"
        elif IsinHedunmaer() and locationTianzhuijushou.Match():
            return "天锥巨兽"
        elif IsinHedunmaer() and locationNuosimaer.Match():
            return "诺斯玛尔"
        elif IsinAerfayingdi() and locationAfaliya.Match():
            return "阿法利亚"
        elif IsinAerfayingdi() and locationNuoyipeila.Match():
            return "诺伊佩拉"
        elif IsInJingxiangalade() and locationYanuofasenlin.Match():
            return "亚诺法森林"
        elif IsInJingxiangalade() and locationEyunzhichen.Match():
            return "厄运之城"
        elif IsInJingxiangalade() and locationNiliupubu.Match():
            return "逆流瀑布"
        elif IsIngente() and locationGente.Match():
            return "根特"
        elif IsIngente() and locationHaigang.Match():
            return "悬空海港"

        return ""

    def GetLocation(self):
        if IsinAierwenfnagxian():
            return "艾尔文防线"
        elif IsinHedunmaer():
            return "赫顿玛尔"
        elif IsinAerfayingdi():
            return "阿法利亚"
        elif IsInJingxiangalade():
            return "镜像阿拉德"
        elif fuckgame.Match():  # TODO 这里没有用
            return "艾尔文防线"
        elif IsIngente():
            return "根特"
        else:
            logger.warning("无法判断在哪里所以按一下.")
            aj().PressKey(VK_CODE['.']), KongjianSleep()
        return ""


def main():
    pass


if __name__ == '__main__':
    main()
