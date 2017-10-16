# coding=utf-8
import json
# try:
#     list = [1, 2, 3]
#     print list[3]
#
# except Exception as e:
#     print e


def functionName(level):
    try:
        if level < 1:
            raise Exception(u'这是一个错误', level)
    except Exception as e:
        print type(e.args)
        print json.dumps(e.args,ensure_ascii=False,encoding='gbk')

functionName(0)
