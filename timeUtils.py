#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time

def getFormatCurrentTime(sYear = False):
    t_dic = time.localtime()
    year = t_dic.tm_year
    if sYear :
        year = year % 100
    return getFormatTime(year, t_dic.tm_mon,\
        t_dic.tm_mday, t_dic.tm_hour, t_dic.tm_min, t_dic.tm_sec)

def getFormatTime(year, month, day, hour, minut, second):
    return "%s-%s-%s_%s-%s-%s" % (year, month, day, hour, minut, second)


if __name__ == '__main__':
    print getFormatCurrentTime(True)