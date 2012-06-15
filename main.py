#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from statise import *
import timeUtils

statis = []
statis.append(HiapkStatis())
statis.append(AppChinaStatis())
statis.append(AnzhiStatis())
statis.append(Baohe360Statis())
statis.append(CrossCatStatis())
statis.append(NDuoSatatis())
statis.append(GfanSatatis())
statis.append(EoeStatis())
statis.append(ZhangkuStatis())
statis.append(ThreeGStatis())

logFile = open("/home/holmes/xy/" + timeUtils.getFormatCurrentTime(True) + ".txt", "w")
for st in statis:
    print st.name()
    st.statis(logFile)
    logFile.write("\n")

logFile.close()