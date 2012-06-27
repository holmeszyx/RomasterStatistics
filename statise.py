#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from http.httpclient import HttpClient
from pyquery import PyQuery as pq
from utils import *
import urllib

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Statise (object):
    """
    统计
    """
    _name = None
    _rawData = None
    _msg = None

    def __init__(self, name):
        self._name = name

    def _getRawData(self):
        """统计过程
            子类重写
        """
        pass

    def _log(self, f):
        """记录"""
        # print self._rawData
        f.write(self._name + " : ")
        if self._rawData != None:
            f.write(self._rawData)
        elif self._msg == None:
            self._msg = "No found"
        if self._msg != None:
            f.write(" message: " + self._msg)

    def name(self):
        return self._name

    def statis(self, file):
        """开始统计"""
        self._getRawData()
        self._log(file)

    def get(self, url):
        """提到一个URL的内容"""
        client = HttpClient(url)
        return client.get()


class Baohe360Statis(Statise):
    """docstring for Baohe360Statis"""

    def __init__(self, name = u"360宝盒"):
        Statise.__init__(self, name)

    def _getRawData(self):
        client = HttpClient(u"http://app.m.360.cn/search/index/?kw=刷机大师")
        self._rawData = client.get().decode("utf8")
        # print type(self._rawData)
        q = pq(self._rawData)
        count = q("p.downNum:first")
        # print count.eq(0)
        # self._rawData = count.text().encode("utf-8")
        t = count.text()
        # print t, type(t)
        self._rawData = subString(t, "", u"次下载")


class HiapkStatis(Statise):
    """hiapk statis"""

    def __init__(self, name = u"安卓网"):
        Statise.__init__(self, name)

    def _getRawData(self):
        client = HttpClient(u"http://apk.hiapk.com/SoftDetails.aspx?action=GetBaseInfo&callback=?&apkId=548861") 
        self._rawData = client.get()
        s = self._rawData
        ss = s.split(r"$")
        self._rawData = ss[4]

class AppChinaStatis(Statise):

    def __init__(self, name = u"应用汇"):
        Statise.__init__(self, name)

    def _getRawData(self):
        client = HttpClient(u"http://www.appchina.com/soft_detail_291336_0_10.html")
        # html = client.get();
        # print html;
        self._rawData = client.get().decode("utf8")
        # print self._rawData
        q = pq(self._rawData)
        count = q("div.sidebar")
        self._rawData = subString(count.eq(0).text(), u"下载：", u"次")
        # print self._rawData

class CrossCatStatis(Statise):

    def __init__(self, name = u"十字猫"):
        Statise.__init__(self, name)

    def _getRawData(self):
        client = HttpClient(u"http://soft.crossmo.com/softinfo_34963.html")
        self._rawData = client.get().decode("utf8")
        q = pq(self._rawData)
        count = q("div.aniu dl dd").eq(2)
        # print count
        self._rawData = subString(count.text(), u"下载次数：")
        if self._rawData == None:
            self._msg = "No found"

class EoeStatis(Statise):

    def __init__(self, name = u"Eoe"):
        Statise.__init__(self, name)

    def _getRawData(self):
        self._rawData = self.get(u"http://www.eoemarket.com/apps/83711")
        q = pq(self._rawData)
        count = q(".downnum").eq(0)
        self._rawData = subString(count.text(), u"下载：", u"次")
        # print self._rawData

class GfanSatatis(Statise):

    def __init__(self, name = u"机锋"):
        Statise.__init__(self, name)

    def _getRawData(self):
        self._rawData = self.get(u"http://apk.gfan.com/Product/DataDeal.aspx?act=dnum&d=&pid=245848")

class NDuoSatatis(Statise):

    def __init__(self, name = u"N多"):
        Statise.__init__(self, name)

    def _getRawData(self):
        self._rawData = self.get("http://www.nduoa.com/apk/detail/320442").decode("utf8")
        q = pq(self._rawData)
        count = q("div.levelCount span.count")
        self._rawData = subString(count.eq(0).text(), u"", u"次下载")
        self._rawData = self._rawData.replace(",", "")

class ThreeGStatis(Statise):

    def __init__(self, name = u"3G"):
        Statise.__init__(self, name)
    
    def _getRawData(self):
        self._rawData = self.get("http://soft.3g.cn/xuan/xuanInfo.aspx?sid=00E60DEC575&waped=9&sysid=&isbibei=&Typelist=&selectType=0&id=37296")
        q = pq(self._rawData)
        count = q("div.info ul li:eq(2)").eq(0)
        self._rawData = subString(count.text(), u"下载：")

class ZhangkuStatis(Statise):

    def __init__(self, name = u"掌酷"):
        Statise.__init__(self, name)

    def _getRawData(self):
        self._rawData = self.get("http://bbs.zhangku.com/thread-90336-1-1.html").decode("gbk")
        q = pq(self._rawData)
        count = q("span#attach_194072 em").eq(0)
        self._rawData = subString(count.text(), u"下载次数:", u")")

class AnzhiStatis(Statise):

    def __init__(self, name = u"安智市场"):
        Statise.__init__(self, name)

    def _getRawData(self):
        self._rawData = self.get("http://www.anzhi.com/soft_183409.html").decode("utf-8")
        q = pq(self._rawData)
        count = q("div.titleline").eq(2).children("span").eq(0)
        # count = count("span").eq(0)
        self._rawData = subString(count.text(), u"下载：", u"次")

if __name__ == '__main__':
    b = ThreeGStatis()
    f = open("./log.txt", "w")
    b.statis(f)
    f.close();
