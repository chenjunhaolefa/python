# coding=utf-8
import json


def printCourse(*courses):
    for course in courses:
        print course


printCourse(1, 2, 3)


def printArgs(*args, **kargs):
    print args
    print kargs
    # 使用json模块将序列转换为json字符串，ensure_ascii表示不考虑asii,encoding表示转换编码
    # json.dumps进行序列化对中文默认使用ascii编码
    # 想要输出真正的中文就需要指定ensure_ascii为false

    print json.dumps(kargs, ensure_ascii=False, encoding='gbk')


printArgs(1, 2, 3, name=u'陈骏', age='27')
