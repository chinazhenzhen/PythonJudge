import requests
import time

def work():
    d = {
        "csrf_token":"IjdjMTc5NWYwMmY0NDk1MTViMTU0OGY4YWU3MDU5MGMwNDcwZjllYzEi.DdaVXw.GtywPiaYntGTEolH3asp9uxDdss",
        "code_language":"1",
        "code":"#include <iostream>\n using namespace std;\nint main()\n{int a=5;\n cout<<a<<endl;}",
        "submit":"提交代码"
    }

    url = "http://0.0.0.0:8080/showproblem/1"

    #cookie 字典形式储存
    cookie ={  #F12 cookie
        "remember_token":"1|e25374a0efd87350505b6354b108174fc6c7693d4"
                         "7e0f581113298d22a9ee5443e5481555662d1d8fb9c3b15081111fccac7ac7519a729d4689c9a280567c5c9",
        "session":".eJylj01uAzEIha9SeT0LsAHbuUoTRTbGbdU"
                  "_aZxZRbl7kbrtrht4oIfexz1c50dbr7bC6fkenm7ewqet1V4sbOF8ZMn9fPBkPh8SEVzHOsPlsf3lFpnklTv8y33ZHGu39RpOt_0wn95GOIXOTajMmCZwLFKKAuaqpfVKOHJ21mw5iRZFEZpIGMtMjEPUUxSSJutDcdRGvqojNQXFXrCIIAsQ4exEluJga31Ad9moDO3Vybaga5_X2_e7fTlPVo_nCXESVUbuyI5XmmXgCgqUYVZT9Ltj2f77BIbHDy8hazY.DdaBwg.5rnIEbnx0TpJEWulsMlhJtBdY8E"
    }


    r = requests.post(url,data=d,cookies=cookie)  #发送post请求，data是表单内容，cookies填写cookie

#for i in range(1,50):  #循环填写请求的次数
    #r = requests.post(url, data=d, cookies=cookie)


def set_fun(func):
    def call_fun(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('程序用时：%s秒' % int(end_time - start_time))
    return call_fun

@set_fun
def mywork():
    for i in range(1, 50):
        work()

mywork()