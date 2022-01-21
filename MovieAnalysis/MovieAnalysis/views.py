from django.http import HttpResponse
from django.shortcuts import render
import json
import pandas as pd
from . import FFF
from . import chat
from . import analysis_sql
import operator
import types
# import translator
from translate import Translator
from . import movie_recommend
cn_en={"中国":"China","美国":"United States","意大利":"Italy","黎巴嫩":"Lebanon","印度":"India","德国":"Germany","日本":"Japan","英国":"United Kingdom","西班牙":"Spain","爱尔兰":"Irelan","俄罗斯":"Russia","泰国":"Thailand","墨西哥":"Mexico","芬兰":"Finla","比利时":"Belgium","法国":"France","匈牙利":"Hunga","韩国":"Korea","荷兰":"Netherlands","苏联":"Russi","越南":"Vietnam"}
def hello(request):
    return HttpResponse("Hello world ! ")
def first(request):
    #左一图
    # l1=analysis_sql.GetYear_money()
    # l1["year"].reverse()
    # l1["money"].reverse()
    #左二图
    # l2=analysis_sql.GetTypes_box(2019)
    # l2=sorted(analysis_sql.GetTypes_box(2019).items(),key=operator.itemgetter(1),reverse=True)
    # namel2=[]
    # valuel2=[]
    # for i in range(5):
    #     namel2.append(l2[i][0])
    #     valuel2.append(l2[i][1])
    # l2={'name':namel2,'value':valuel2}
    #中间大图
    # zj=analysis_sql.GetCountry_box(2019)
    # namezj=[]
    # valuezj=[]
    # translator = Translator(from_lang="chinese", to_lang="english")
    # for i,j in zj.items():
    #     print(i,j)
    #     namezj.append(cn_en[i])
    #     valuezj.append(j)
    # zj={"name":namezj,"value":valuezj}
    # print(zj)
    #下边第一个图
    # x1=analysis_sql.GetLen_movie()
    #右下角的图
    # right=analysis_sql.GetLrate_movie()
    return render(request,'analysis.html')
def ajax_handle(request):
    if request.method == "POST":
        name = request.POST.get('name')
        status = 1
        result = "hhhhh"
        return HttpResponse(json.dumps({
            "status": status,
            "result": result,
            "data":[1000, 300, 300, 900, 1500, 1200, 300],
        }))
def zhishi(request):
    dic = FFF.find_film("战狼2")
    status = 1
    print(dic)
    return render(request,'zhishitupu.html',{
        "status": status,
        "data": dic["data"],
        "link": dic["link"],
    })
def appendnode(request):
    if request.method == "POST":
        type= request.POST.get('ty')
        name=request.POST.get('name')
        status=0
        dic={}
        if(type=="2"):#电影
            dic=FFF.find_film(name)
            status = 1
        if(type=="1"):#导演
            dic=FFF.find_person(name)
            status = 1
        if(type=="0"):#演员
            dic=FFF.find_person(name)
            status = 1
        if (type == "3"):#类型
            dic = FFF.find_type(name)
            status = 1
        print(dic["data"])
        return HttpResponse(json.dumps({
            "status": status,
            "data": dic["data"],
            "link": dic["link"],
        }))
def search_node(request):
    if request.method == "POST":
        name=request.POST.get('name')
        status=1
        dic=FFF.find_film(name)
        print(len(dic["data"]))
        if(len(dic["data"])==0):
            dic=FFF.find_person(name)
            print(name)
            print(dic)
            if(len(dic["data"])==0):
                dic=FFF.find_type(name)
        print(dic)
        return HttpResponse(json.dumps({
            "status": status,
            "data": dic["data"],
            "link": dic["link"],
        }))
def chatt(request):
    context={}
    context['hello']='Hello World!'
    temp=["I want to find a girlfriend","hhh",91,100]
    num=91
    return render(request,'chat.html', {"name":json.dumps(temp)})
def chat_response(request):
    if request.method == "POST":
        question = request.POST.get('txt')
        status = 1
        print(question)
        retxt=chat.questionInput(question)
        print(retxt,'retxt')
        return HttpResponse(json.dumps({
            "status": status,
            "txt": retxt,
        }))
def second(request):
    context = {}
    context['hello'] = 'Hello World!'
    temp = ["I want to find a girlfriend", "hhh", 91, 100]
    num = 91
    return render(request, 'analysis2.html', {"name": json.dumps(temp)})
def third(request):
    context = {}
    context['hello'] = 'Hello World!'
    temp = ["I want to find a girlfriend", "hhh", 91, 100]
    num = 91
    return render(request, 'analysis3.html', {"name": json.dumps(temp)})
def recommend(request):
    context = {}
    context['hello'] = 'Hello World!'
    temp = ["I want to find a girlfriend", "hhh", 91, 100]
    num = 91
    print(request)
    return render(request, 'recommend.html', {"name": json.dumps(temp)})
def ajax_recommend(request):
    uid=request.POST.get('uid')
    r=movie_recommend.getmovie(uid)
    status=1
    return HttpResponse(json.dumps({
        "status": status,
        "url": r["url"],
        "pic": r["pic"],
    }))