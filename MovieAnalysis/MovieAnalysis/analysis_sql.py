import pymysql
from collections import defaultdict
from translate import Translator
import operator
# 打开数据库连接
db = pymysql.connect(host="localhost",user="root",password="123456",db="movie")
# db = pymysql.connect(host="localhost",user="root",password="123456",db="aliyun")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
# 使用 fetchone() 方法获取单条数据.
# 使用 fetchall() 方法获取单条数据.

# 每年票房统计 单位亿元
def GetYear_money():
    sql = "select year,sum(money) from box group by year order by year desc;"
    cursor.execute(sql)
    year_money = cursor.fetchall()
    year_money = list(year_money)
    year = []
    money = []
    for i in year_money:
        year.append(i[0])
        # money.append(float(i[1]/10000))
        money.append(round(i[1]/10000))
    return {"year":year,"money":money}

# 某年分各地区票房统计
 # # 2019
def GetCountry_box(year):
    sql = "select movie_id , country from movie_information ;"
    cursor.execute(sql)
    cou = cursor.fetchall()
    cou = list(cou)
    country = []
    for i in cou:
        i = list(i)
        country.append(i)
    for i in range(len(country)):
        country[i][1] = country[i][1].split(' ')[1]
        if country[i][1][0] == "中" and country[i][1][1] == '国':
            country[i][1] = "中国"
    index, value = [], []
    for i in range(len(country)):
        index.append(country[i][0])
        value.append(country[i][1])
    country_dict = dict(zip(index, value))
    sql = "select movie_id , money from box where year=" + str(year) + ";"
    cursor.execute(sql)
    bo = cursor.fetchall()
    box = []
    for i in bo:
        i = list(i)
        box.append(i)
    country_money_2019 = []
    for i in range(len(box)):
        temp = []
        temp.append(country_dict[box[i][0]])
        temp.append(box[i][1])
        country_money_2019.append(temp)
    d = defaultdict(list)
    for key, value in country_money_2019:
        d[key].append(value)
    for i in d:
        d[i] = sum(d[i])
    return d


# zj = GetCountry_box(2019)
# print(zj)
# print(zj["中国"])
# namezj=[]
# valuezj=[]
# translator = Translator(from_lang="chinese", to_lang="english")
# print(translator.translate("印度"))
# for i,j in zj.items():
#     print(i,j)
#     namezj.append(translator.translate(i))
#     valuezj.append(j)
# zj={"name":namezj,"value":valuezj}
# print(zj)
# 某年度类型占比
# # 2019：
def GetTypes_box(year):
    sql = "select type_id , type_name from types ;"
    cursor.execute(sql)
    type = cursor.fetchall()
    type = list(type)
    types = []
    for i in type:
        i = list(i)
        types.append(i)
    index = []
    for i in types:
        index.append(i[1])
    value = [0] * len(index)
    types_box_2019 = dict(zip(index, value))
    # print(types_box_2019)
    sql = "select movie_id , money , movie from box where year = " +str(year)+";"
    cursor.execute(sql)
    box = cursor.fetchall()
    sql = "select film_id , type_id from belong_to ;"
    cursor.execute(sql)
    belong = cursor.fetchall()
    sql = "select film_id , film_name from film_names ;"
    cursor.execute(sql)
    film_name = cursor.fetchall()
    for i in belong:
        for j in film_name:
            if i[0] == j[0]:
                for k in box:
                    if k[2] == j[1]:
                        for l in types:
                            if l[0] == i[1]:
                                types_box_2019[l[1]] += k[1]
    return types_box_2019
# print(GetTypes_box(2019))
# a=GetTypes_box(2000)
# for k in range(2001,2020):
#     b=GetTypes_box(k)
#     for i,j in b.items():
#         if(i in a):
#             a[i]+=j
#         else:
#             print(k,i)
#             a[i]=j
# print(a)
# 某年度最受欢迎的演员排名：
# # 2019：
def GetStar_box(year):
    sql = "select film_id , actor_id from acted_in ;"
    cursor.execute(sql)
    acted = cursor.fetchall()
    sql = "select actor_id , actor_name from actor ;"
    cursor.execute(sql)
    actor = cursor.fetchall()
    sql = "select movie_id , money , movie from box where year = " + str(year) + ";"
    cursor.execute(sql)
    box = cursor.fetchall()
    sql = "select film_id , film_name from film_names ;"
    cursor.execute(sql)
    film_name = cursor.fetchall()

    actor = list(actor)
    actors = []
    for i in actor:
        i = list(i)
        actors.append(i)
    index = []
    for i in actors:
        index.append(i[1])
    value = [0] * len(index)
    star_box_2019 = dict(zip(index, value))
    for i in acted:
        for j in film_name:
            if i[0] == j[0]:
                for k in box:
                    if k[2] == j[1]:
                        for l in actor:
                            if l[0] == i[1]:
                                star_box_2019[l[1]] += k[1]
    star_box_2019 = sorted(star_box_2019.items(), key=lambda d: d[1], reverse=True)
    return star_box_2019[:10]

# 某年度最受欢迎的导演排名：
# # 2019：
def getDirector_box(year):
    sql = "select film_id , director_id from directed ;"
    cursor.execute(sql)
    directed = cursor.fetchall()
    sql = "select director_id , director_name from director ;"
    cursor.execute(sql)
    director = cursor.fetchall()
    sql = "select movie_id , money , movie from box where year = " + str(year) +";"
    cursor.execute(sql)
    box = cursor.fetchall()
    sql = "select film_id , film_name from film_names ;"
    cursor.execute(sql)
    film_name = cursor.fetchall()

    actor = list(director)
    directors = []
    for i in director:
        i = list(i)
        directors.append(i)
    index = []
    for i in directors:
        index.append(i[1])
    value = [0] * len(index)
    director_box_2019 = dict(zip(index, value))
    for i in directed:
        for j in film_name:
            if i[0] == j[0]:
                for k in box:
                    if k[2] == j[1]:
                        for l in director:
                            if l[0] == i[1]:
                                director_box_2019[l[1]] += k[1]
    director_box_2019 = sorted(director_box_2019.items(), key=lambda d: d[1], reverse=True)
    return director_box_2019[:10]

# 国内外票房比较：
# # 2019
def Getbox_compare(year):
    sql = "select movie_id , country from movie_information ;"
    cursor.execute(sql)
    cou = cursor.fetchall()
    cou = list(cou)
    country = []
    for i in cou:
        i = list(i)
        country.append(i)
    for i in range(len(country)):
        country[i][1] = country[i][1].split(' ')[1]
        if country[i][1][0] == "中" and country[i][1][1] == '国':
            country[i][1] = "中国"
    index, value = [], []
    for i in range(len(country)):
        index.append(country[i][0])
        value.append(country[i][1])
    country_dict = dict(zip(index, value))
    sql = "select movie_id , money from box where year=" + str(year) + ";"
    cursor.execute(sql)
    bo = cursor.fetchall()
    box = []
    for i in bo:
        i = list(i)
        box.append(i)
    country_money_2019 = []
    for i in range(len(box)):
        temp = []
        temp.append(country_dict[box[i][0]])
        temp.append(box[i][1])
        country_money_2019.append(temp)
    d = defaultdict(list)
    for key, value in country_money_2019:
        d[key].append(value)
    for i in d:
        d[i] = sum(d[i])
    index = ['国内', '国外']
    value = [0, 0]
    for i in d.items():
        if i[0] == '中国':
            value[0] += i[1]
        else:
            value[1] += i[1]
    box_compare = dict(zip(index, value))
    return box_compare



def getMovieTypes(movie_name):
    res=[]
    for i in movie_name:
        sql = "select film_id from film_names where trim(film_name) = '" + i + "';"
        cursor.execute(sql)
        id = cursor.fetchone()
        sql = "select type_id from belong_to where film_id= " + id[0] + ";"
        cursor.execute(sql)
        type_id = cursor.fetchall()
        types = []
        for i in type_id:
            sql = "select type_name from types where type_id= " + i[0] + ";"
            cursor.execute(sql)
            type = cursor.fetchone()
            types.append(type[0])
        res.append(types)
    #return dict(zip(movie_name,res))
    return res[0]
def getMovieRate(movie_name):
    res=[]
    for i in movie_name:
        rates=[]
        sql = "select movie_rate from movie_information where movie_name ='" + i + "';"
        cursor.execute(sql)
        rate = cursor.fetchone()
        rates.append(rate[0])
        res.append(rates)
    #return dict(zip(movie_name,res))
    return res[0]
def getMovieDate(movie_name):
    res=[]
    for i in movie_name:
        datas=[]
        sql = "select year from movie_information where movie_name ='" + i + "';"
        cursor.execute(sql)
        year = cursor.fetchone()
        datas.append(year[0])
        res.append(datas)
    #return dict(zip(movie_name, res))
    return res[0]
def getMovieCountry(movie_name):
    res=[]
    for i in movie_name:
        sql = "select country from movie_information where movie_name like '" + i + "';"
        cursor.execute(sql)
        country = cursor.fetchone()
        res.append(country[0].split(",")[1:])
    #return dict(zip(movie_name, res))
    return res[0]
def getMovielen(movie_name):
    res = []
    for i in movie_name:
        lens = []
        sql = "select length from movie_information where movie_name ='" + i + "';"
        cursor.execute(sql)
        len = cursor.fetchone()
        lens.append(len[0])
        res.append(lens)
    #return dict(zip(movie_name, res))
    return res[0]
def getMovielanguage(movie_name):
    res = []
    for i in movie_name:
        sql = "select language from movie_information where movie_name like '" + i + "';"
        cursor.execute(sql)
        language = cursor.fetchone()
        res.append(language[0].split(",")[1:])
    #return dict(zip(movie_name, res))
    return res[0]
def getMovieActor(movie_name):
    res = []
    for j in movie_name:
        sql = "select film_id from film_names where trim(film_name) = '" + j + "';"
        cursor.execute(sql)
        id = cursor.fetchone()
        sql = "select actor_id from acted_in where film_id= " + id[0] + ";"
        cursor.execute(sql)
        actor_id = cursor.fetchall()
        actors = []
        for i in actor_id:
            sql = "select actor_name from actor where actor_id= " + i[0] + ";"
            cursor.execute(sql)
            actor = cursor.fetchone()
            actors.append(actor[0])
        res.append(actors)
    #return dict(zip(movie_name, res))
    return res[0]
def getMovieDirector(movie_name):
    res = []
    for j in movie_name:
        sql = "select film_id from film_names where trim(film_name) = '" + j + "';"
        cursor.execute(sql)
        id = cursor.fetchone()
        sql = "select director_id from directed where film_id= " + id[0] + ";"
        cursor.execute(sql)
        director_id = cursor.fetchall()
        directors = []
        for i in director_id:
            sql = "select director_name from director where director_id= " + i[0] + ";"
            cursor.execute(sql)
            director = cursor.fetchone()
            directors.append(director[0])
        res.append(directors)
    #return dict(zip(movie_name, res))
    return res[0]
def getMovieInformation(movie_name):
    types=getMovieTypes(movie_name)
    rate=getMovieRate(movie_name)
    date=getMovieDate(movie_name)
    country=getMovieCountry(movie_name)
    len=getMovielen(movie_name)
    language=getMovielanguage(movie_name)
    actor=getMovieActor(movie_name)
    director=getMovieDirector(movie_name)
    res=[]
    for i in movie_name:
        index=["types","rate","date","country","len","language","actor","director"]
        value=[]
        value.append(types)
        value.append(rate)
        value.append(date)
        value.append(country)
        value.append(len)
        value.append(language)
        value.append(actor)
        value.append(director)
        dic=dict(zip(index,value))
        res.append(dic)
    return res

def persondirect(personlist):
    for i in personlist:
        sql="select director_id from director where trim(director_name) = '" + i + "';"
        cursor.execute(sql)
        id = cursor.fetchone()
        sql="select film_id from directed where trim(director_id) = '" + id[0] + "';"
        cursor.execute(sql)
        film_id = cursor.fetchall()
        res=[]
        for j in film_id:
            sql="select film_name from film_names where film_id=" + j[0]
            cursor.execute(sql)
            name = cursor.fetchone()
            res.append(name[0])
    return res
def personact(personlist):#输入是单元列表
    for i in personlist:
        sql="select actor_id from actor where trim(actor_name) = '" + i + "';"
        cursor.execute(sql)
        id = cursor.fetchone()
        sql="select film_id from acted_in where trim(actor_id) = '" + id[0] + "';"
        cursor.execute(sql)
        film_id = cursor.fetchall()
        res=[]
        for j in film_id:
            sql="select film_name from film_names where film_id=" + j[0]
            cursor.execute(sql)
            name = cursor.fetchone()
            res.append(name[0])
    return res
def persongender(personlist):#输入是单元列表
    res=[]
    for i in personlist:
        sql="select ifnull(gender,'暂无信息') from fianlly where person_name like '%" + i + "%';"
        cursor.execute(sql)
        id = cursor.fetchone()
        res.append(id[0])
    return res
def personjob(personlist):#输入是单元列表
    res = []
    for i in personlist:
        sql = "select ifnull(job,'暂无信息') from fianlly where person_name like '%" + i + "%';"
        cursor.execute(sql)
        id = cursor.fetchone()
        res.append(id[0])
    return res
def personcons(personlist):#输入是单元列表
    res = []
    for i in personlist:
        sql = "select ifnull(constellation,'暂无信息') from fianlly where person_name like '%" + i + "%';"
        cursor.execute(sql)
        id = cursor.fetchone()
        res.append(id[0])
    return res
def personbirthplace(personlist):#输入是单元列表
    res = []
    for i in personlist:
        sql = "select ifnull(birthplace,'暂无信息') from fianlly where person_name like '%" + i + "%';"
        cursor.execute(sql)
        id = cursor.fetchone()
        res.append(id[0])
    return res
def personbirthday(personlist):#输入是单元列表
    res = []
    for i in personlist:
        sql = "select ifnull(birthday,'暂无信息') from fianlly where person_name like '%" + i + "%';"
        cursor.execute(sql)
        id = cursor.fetchone()
        res.append(id[0])
    return res
def personfamily(personlist):#输入是单元列表
    res = []
    for i in personlist:
        sql = "select ifnull(famliy,'暂无信息') from fianlly where person_name like '%" + i + "%';"
        cursor.execute(sql)
        id = cursor.fetchone()
        res.append(id[0])
    return res
def personcountry(personlist):#输入是单元列表
    res = []
    for i in personlist:
        sql = "select ifnull(country,'暂无信息') from fianlly where person_name like '%" + i + "%';"
        cursor.execute(sql)
        id = cursor.fetchone()
        res.append(id[0])
    return res
def typefilm(type):#输入是元素
    res=[]
    sql="select type_id from types where trim(type_name)= trim('" + type[0] +"');"
    cursor.execute(sql)
    id = cursor.fetchone()
    sql="select film_id from belong_to where type_id=" + id[0] + ";"
    cursor.execute(sql)
    film = cursor.fetchall()
    for i in film:
        sql="select film_name from film_names where film_id="  + i[0] + ";"
        cursor.execute(sql)
        film_name = cursor.fetchone()
        res.append(film_name[0])
    return res
def person_default(personlist):#输入是单元列表
    direct=persondirect(personlist)
    act=personact(personlist)
    gender=persongender(personlist)
    job=personjob(personlist)
    cons=personcons(personlist)
    birthplace=personbirthplace(personlist)
    birthday=personbirthday(personlist)
    famliy=personfamily(personlist)
    res=[]
    for i in personlist:
        index=["direct","act","gender","job","cons","birthplace","birthday","famliy"]
        value=[]
        value.append(direct)
        value.append(act)
        value.append(gender)
        value.append(job)
        value.append(cons)
        value.append(birthplace)
        value.append(birthday)
        value.append(famliy)
        dic=dict(zip(index,value))
        res.append(dic)
    return res
def GetLen_movie():
    lit=[]
    sql = "select count(*) from movie_information where length between 0 and 60;"
    cursor.execute(sql)
    infor = cursor.fetchone()
    lit.append(infor[0])
    sql = "select count(*) from movie_information where length between 60 and 90;"
    cursor.execute(sql)
    infor = cursor.fetchone()
    lit.append(infor[0])
    sql = "select count(*) from movie_information where length between 90 and 120;"
    cursor.execute(sql)
    infor = cursor.fetchone()
    lit.append(infor[0])
    sql = "select count(*) from movie_information where length between 120 and 150;"
    cursor.execute(sql)
    infor = cursor.fetchone()
    lit.append(infor[0])
    sql = "select count(*) from movie_information where length >150;"
    cursor.execute(sql)
    infor = cursor.fetchone()
    lit.append(infor[0])
    name=["0-60","60-90","90-120","120-150","150-"]
    result={'name':name,'value':lit}
    return result
def GetLrate_movie():
    lit=[]
    sql = "select count(*) from movie_information where movie_rate between 0 and 2;"
    cursor.execute(sql)
    infor = cursor.fetchone()
    lit.append(infor[0])
    sql = "select count(*) from movie_information where movie_rate between 2 and 4;"
    cursor.execute(sql)
    infor = cursor.fetchone()
    lit.append(infor[0])
    sql = "select count(*) from movie_information where movie_rate between 4 and 6;"
    cursor.execute(sql)
    infor = cursor.fetchone()
    lit.append(infor[0])
    sql = "select count(*) from movie_information where movie_rate between 6 and 8;"
    cursor.execute(sql)
    infor = cursor.fetchone()
    lit.append(infor[0])
    sql = "select count(*) from movie_information where movie_rate between 8 and 10;"
    cursor.execute(sql)
    infor = cursor.fetchone()
    lit.append(infor[0])
    name=['0-2','3-4','5-6','7-8','9-10']
    r={"name":name,"value":lit}
    return r
# print(GetLen_movie())
# print(getMovieInformation(["1921"]))
# print(getMovieTypes(["海上钢琴师"]))
# print(getMovieRate(["海上钢琴师"]))
# print(getMovieDate(["海上钢琴师"]))
# print(getMovieCountry(["狼行者"]))
# print(getMovielen(["狼行者"]))
# print(getMovielanguage(["狼行者"]))
# print(getMovieActor(["狼行者"]))
# print(getMovieDirector(["狼行者"]))
# print(persondirect(["贾玲"]))
# print(personact(["贾玲"]))
# print(persongender(["佐野和真","贾玲"]))
# print(personjob(["佐野和真","贾玲"]))
# print(personcons(["佐野和真","贾玲"]))
# print(personbirthplace(["佐野和真","贾玲"]))
# print(personbirthday(["佐野和真","贾玲"]))
# print(personfamily(["佐野和真","贾玲"]))
# print(personcountry(["佐野和真","贾玲"]))
# print(typefilm(["恐怖"]))
# print(person_default(["贾玲"]))













# coding=utf-8
# import pandas as pd
# f=open(r'C:\ProgramData\MySQL\MySQL Server 5.7\Uploads\all_person_info.txt')
# s=""
# txt=[]
# for line in f:
#     txt.append(line.strip().encode('utf8','ignore').decode('unicode_escape'))
# f.close()
# print(txt[0])
# print(txt[2].split('"ID":')[1].split(',')[0])
# # for i in txt[2].split('"ID":')[1].split(',')[0]:
# #     print(i)
# data= pd.DataFrame({'id':[],'person_name':[],'head_portrait':[],'gender':[],'job':[],'constellation':[],'birthplace':[],'country':[],'birthday':[],'famliy':[],'imdb':[],'brief':[]})
# #print(data)
# index=0
# for i in txt:
#     temp=[]
#     temp.append(i.split('"ID":')[1].split(',')[0])
#     temp.append(i.split('"Name":')[1].split(',')[0])
#     temp.append(i.split('"Head_portrait":')[1].split('[')[1].split(']')[0])
#     temp.append(i.split('"Gender":')[1].split('[')[1].split(']')[0])
#     temp.append(i.split('"Job":')[1].split('[')[1].split(']')[0])
#     temp.append(i.split('"Constellation":')[1].split('[')[1].split(']')[0])
#     temp.append(i.split('"Birthplace":')[1].split('[')[1].split(']')[0])
#     temp.append(i.split('"Country":')[1].split('[')[1].split(']')[0])
#     temp.append(i.split('"Birthday":')[1].split('[')[1].split(']')[0])
#     temp.append(i.split('"Family":')[1].split('[')[1].split(']')[0])
#     temp.append(i.split('"IMDb":')[1].split('[')[1].split(']')[0])
#     temp.append(i.split('"Brief":')[1].split('[')[1].split(']')[0])
#     data.loc[index] = temp
#     index +=1
#
#
# data.to_csv(r"C:\ProgramData\MySQL\MySQL Server 5.7\Uploads\fianlly.csv",header=True,errors='ignore')
# print(data)
# 关闭数据库连接
# print(GetYear_money())


