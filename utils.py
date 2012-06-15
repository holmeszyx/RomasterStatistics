#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import re

__systemType = sys.getfilesystemencoding()

def utf8(str):
    return str.decode("UTF-8").encode(__systemType)

def unescape_word(s):
    words = re.findall("&#(\d+);", s)
    
    if words:
       result=s
       for r in words:
         word =unichr(int(r))
         result = result.replace("&#%s;" % r,word)
    else:
       result = s
    return result

def subString(str, s, e = None):
    sPos = str.find(s)
    if sPos == -1:
        return None
    sLen = len(s)
    if e == None:
      return str[sPos + sLen : ]
    ePos = str.find(e, sPos + sLen)
    # print sPos, ePos
    return str[sPos + sLen : ePos]


if __name__ == '__main__':
  print subString("20315次下载", "", "次下载")