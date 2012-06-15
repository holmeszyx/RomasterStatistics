#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time

def getFormatCurrentTime():
    """得到格式化后的当前时间"""
    t_dic = time.localtime()
    return getFormatTime(t_dic)
    # year = t_dic.tm_year
    # if sYear :
    #     year = year % 100
    # return getFormatTime(year, t_dic.tm_mon,\
    #     t_dic.tm_mday, t_dic.tm_hour, t_dic.tm_min, t_dic.tm_sec)

# %y-%m-%d_%H-%M-%S
def getFormatTime(structTime):
    """得到格式化时间"""
    return time.strftime("%y-%m-%d_%H-%M-%S", structTime)


if __name__ == '__main__':
    print getFormatCurrentTime()