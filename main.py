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

logFileName = timeUtils.getFormatCurrentTime() + ".txt"
logFilePath = "/home/holmes/xy/" +logFileName
print u"[文件保存于 %s ]" % (logFilePath)
logFile = open(logFilePath, "w")
for st in statis:
    print st.name(),
    st.statis(logFile)
    print "\n",
    logFile.write("\n")

logFile.close()

print u"[完成]"