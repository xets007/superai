import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

# 旧客户端 固定大区坐标
firstposes = [
    (324, 155), (452, 155), (570, 155), (691, 155), (814, 155),
    (324, 208), (452, 208), (570, 208), (691, 208), (814, 208),
    (324, 257), (452, 257), (570, 257), (691, 257), (814, 257),
    (324, 307), (452, 307), (570, 307), (691, 307), (814, 307),
]

secondposes = [
    (324, 397), (452, 397), (570, 397), (691, 397), (814, 397),
    (324, 448), (452, 448), (570, 448), (691, 448), (814, 448),
    (324, 500), (452, 500), (570, 500), (691, 500), (814, 500),
]

daqus = {
    "电信": [
        ("广东区", [
            "广东1区",
            "广东2区",
            "广东3区",
            "广东1/2区",
            "广东4区",
            "广东5区",
            "广东6区",
            "广东7区",
            "广东8区",
            "广东9区",
            "广东10区",
            "广东11区",
            "广东12区",
            "广东13区",
        ]),
        ("西北区", [
            "西北1区",
            "西北2/3区"
        ]),
        ("江西区", [
            "江西1区",
            "江西2区",
            "江西3区"
        ]),
        ("广西区", [
            "广西1区",
            "广西2/4区",
            "广西3区",
            "广西5区"
        ]),
        ("西南区", [
            "西南1区",
            "西南2区",
            "西南3区"
        ]),
        ("湖南区", [
            "湖南1区",
            "湖南2区",
            "湖南3区",
            "湖南4区",
            "湖南5区",
            "湖南6区",
            "湖南7区",
        ]),
        ("陕西区", [
            "陕西1区",
            "陕西2/3区"
        ]),
        ("湖北区", [
            "湖北1区",
            "湖北2区",
            "湖北3区",
            "湖北4区",
            "湖北5区",
            "湖北6区",
            "湖北7区",
            "湖北8区",
        ]),
        ("云贵区", [
            "云南1区",
            "贵州1区",
            "云贵1区"
        ]),
        ("上海区", [
            "上海1区",
            "上海2区",
            "上海3区",
            "上海4/5区",
        ]),
        ("四川区", [
            "四川1区",
            "四川2区",
            "四川3区",
            "四川4区",
            "四川5区",
            "四川6区",
        ]),
        ("江苏区", [
            "江苏1区",
            "江苏2区",
            "江苏3区",
            "江苏4区",
            "江苏5/7区",
            "江苏6区",
            "江苏8区",
        ]),
        ("重庆区", [
            "重庆1区",
            "重庆2区"
        ]),
        ("浙江区", [
            "浙江1区",
            "浙江2区",
            "浙江3区",
            "浙江4/5区",
            "浙江6区",
            "浙江7区",
        ]),
        ("新疆区", [
            "新疆1区"
        ]),
        ("安徽区", [
            "安徽1区",
            "安徽2区",
            "安徽3区",
        ]),
        ("福建区", [
            "福建1区",
            "福建2区",
            "福建3/4区",
        ])
    ],
    "联通": [
        ("东北区", [
            "东北1区",
            "东北2区",
            "东北3/7区",
            "东北4/5/6区",
        ]),
        ("北京区", [
            "北京1区",
            "北京2/4区",
            "北京3区",
        ]),
        ("天津区", [
            "天津1区"
        ]),
        ("内蒙古区", [
            "内蒙古1区"
        ]),
        ("辽宁区", [
            "辽宁1区",
            "辽宁2区",
            "辽宁3区"
        ]),
        ("吉林区", [
            "吉林1/2区"
        ]),
        ("黑龙江区", [
            "黑龙江1区",
            "黑龙江1/2区"
        ]),
        ("河南区", [
            "河南1区",
            "河南2区",
            "河南3区",
            "河南4区",
            "河南5区",
            "河南6区",
            "河南7区",
            "河南8区",
        ]),
        ("华北区", [
            "华北1区",
            "华北2区",
            "华北3区",
            "华北4区",
        ]),
        ("山东区", [
            "山东1区",
            "山东2/7区",
            "山东3区",
            "山东4区",
            "山东5区",
            "山东6区",
        ]),
        ("河北区", [
            "河北1区",
            "河北2/3区",
            "河北4区",
            "河北5区",
        ]),
        ("山西区", [
            "山西1区",
            "山西2区"
        ])
    ]
}

kuaqus = [
    ("跨一", [
        "广东1区",
        "广东2区",
        "广东3区",
        "广东4区",
        "广东5区",
        "广东6区",
        "广东7区",
        "广东8区",
        "广东9区",
        "广东10区",
        "广东11区",
        "广东12区",
        "广东1/2区",
        "广西1区",
        "广西2/4区",
        "广西3区",
        "广西5区"
    ]),
    ("跨二", [
        "湖北1区",
        "湖北2区",
        "湖北3区",
        "湖北4区",
        "湖北5区",
        "湖北6区",
        "湖北7区",
        "湖北8区",
        "湖南1区",
        "湖南2区",
        "湖南3区",
        "湖南4区",
        "湖南5区",
        "湖南6区",
        "湖南7区"
    ]),
    ("跨三A区", [
        "四川1区",
        "四川2区",
        "四川3区",
        "四川4区",
        "四川5区",
        "四川6区",
        "西北1区",
        "西北2/3区",
        "新疆1区"
    ]),
    ("跨三B区", [
        "陕西1区",
        "陕西2/3区",
        "云南1区",
        "贵州1区",
        "西南1区",
        "西南2区",
        "西南3区",
        "重庆1区",
        "重庆2区",
        "云贵1区"
    ]),
    ("跨四", [
        "上海4/5区",
        "江苏5/7区",
        "江苏6区",
        "江苏8区",
        "浙江4/5区",
        "浙江6区",
        "浙江7区",
        "福建3/4区",
        "江西3区",
        "安徽3区"
    ]),
    ("跨五", [
        "上海1区",
        "上海2区",
        "上海3区",
        "江苏1区",
        "江苏2区",
        "江苏3区",
        "江苏4区",
        "浙江1区",
        "浙江2区",
        "浙江3区",
        "福建1区",
        "福建2区",
        "江西1区",
        "江西2区",
        "安徽1区",
        "安徽2区",
    ]),
    ("跨六", [
        "北京1区",
        "北京2/4区",
        "华北1区",
        "华北2区",
        "华北3区",
        "东北1区",
        "东北2区",
        "东北3/7区",
        "辽宁1区",
        "西北1区",
        "山东1区",
        "山东2/7区",
        "河北1区",
        "河南1区",
        "河南2区",
        "黑龙江1区",
        "吉林1/2区"
    ]),
    ("跨七A区", [
        "辽宁2区",
        "辽宁3区",
        "东北4/5/6区",
        "河北2/3区",
        "河北4区",
        "河北5区"
    ]),
    ("跨七B区", [
        "河南3区",
        "河南4区",
        "河南5区",
        "河南6区",
        "河南7区"
    ]),
    ("跨八", [
        "山西2区",
        "黑龙江2/3区",
        "北京3区",
        "天津1区",
        "内蒙古1区",
        "华北4区",
        "山东3区",
        "山东4区",
        "山东5区",
        "山东6区"
    ])
]


# 联通还是电信
def GetDaqu(region):
    mainregions = daqus["电信"]
    for mainregion in mainregions:
        if region in mainregion[1]:
            return "电信"

    mainregions = daqus["联通"]
    for mainregion in mainregions:
        if region in mainregion[1]:
            return "联通"

    return ""


# 获取主服务器位置
def GetMainregionPos(region):
    for k, v in daqus.items():
        for i, mainregion in enumerate(v):
            if region in mainregion[1]:
                return firstposes[i]

    raise Exception("找不到主服务器地址")


# 获取服务器位置
def GetRegionPos(r):
    for k, v in daqus.items():
        for i, mainregion in enumerate(v):
            for k, region in enumerate(mainregion[1]):
                if r == region:
                    return secondposes[k]
    raise Exception("找不到服务器地址")


def main():
    # ClientWindowToTop()

    qus = ["广西5区[跨一]", "湖南7区[跨二]", "新疆1区[跨三A]", "安徽3区[跨四]", "安徽2区[跨五]", "北京1区[跨六]", "河北5区[跨七A]", "北京3区[跨八]"]

    # 横竖的 8皇后  = = . 所以这里是 8 x 8 的情况, 竖向不能有重复的. 直接打印啦

    for i in range(len(qus)):
        for k in range(i, len(qus)):
            print(qus[k], end=",")

        for j in range(i):
            print(qus[j], end=",")

        print("")


if __name__ == '__main__':
    main()
