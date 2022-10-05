# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line3 = '<a href="/play/">进入游戏界面</a>'
    line4 = '<hr>'
    line2 = '<img src="https://bkimg.cdn.bcebos.com/pic/c2cec3fdfc039245efdd58288f94a4c27d1e25a8?x-bce-process=image/resize,m_lfit,w_536,limit_1/format,f_jpg" width=1400 >'

    return HttpResponse(line1 + line4 + line3 + line2)


def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'
    line3 = '<a href="/">返回主页面</a>'
    line4 = '<hr>'
    line2 = '<img src="https://pic.baike.soso.com/ugc/baikepic2/5331/20220507093610-459274137_jpeg_500_309_32218.jpg/300" width=1400 >'
    return HttpResponse(line1 + line4 + line3 + line2)
