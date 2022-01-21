import pandas as pd
import pymysql
from collections import defaultdict
import jieba

# 打开数据库连接
db = pymysql.connect(host="localhost",user="root",password="123456",db="movie")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


actor=pd.read_csv(r'C:\MovieAnalysis\MovieAnalysis\MovieAnalysis\actor.csv',encoding='utf_8').values[:,1]
director=pd.read_csv(r'C:\MovieAnalysis\MovieAnalysis\MovieAnalysis\director.csv',encoding='utf_8').values[:,1]
film_names=pd.read_csv(r'C:\MovieAnalysis\MovieAnalysis\MovieAnalysis\film_names.csv',encoding='utf_8').values[:,1]
types_names=pd.read_csv(r'C:\MovieAnalysis\MovieAnalysis\MovieAnalysis\types.csv',encoding='utf_8').values[:,1]

with open('typesnames.txt','w',encoding='utf_8') as file:
    for item in types_names:
        file.write(item)
        file.write('\n')

with open('filmnames.txt','w',encoding='utf_8') as file:
    for item in film_names:
        file.write(item)
        file.write('\n')

with open('filmactors.txt','w',encoding='utf_8') as file:
    for item in actor:
        temp=str(item)
        if '·' in temp:
            name = temp.split('·')
            temp = ''
            for i in name:
                temp += i
        file.write(temp)
        file.write('\n')

with open('filmdirectors.txt','w',encoding='utf_8') as file:
    for item in director:
        temp = str(item)
        if '·' in temp:
            name = temp.split('·')
            temp = ''
            for i in name:
                temp += i
        file.write(temp)
        file.write('\n')

keywordlist=['演员','导演','上映日期','上映地区','评分','时长','类型','语言']
with open('relation.txt','w',encoding='utf_8') as file:
    file.write('演员')
    file.write('\n')
    file.write('导演')
    file.write('\n')
    file.write('上映日期')
    file.write('\n')
    file.write('上映地区')
    file.write('\n')
    file.write('评分')
    file.write('\n')
    file.write('时长')
    file.write('\n')
    file.write('类型')
    file.write('\n')
    file.write('语言')
    file.write('\n')

keywordlist_person=['导演','出演','演过','性别','职业','星座','出生地','生日']
with open('relation_p.txt','w',encoding='utf_8') as file:
    file.write('导演')
    file.write('\n')
    file.write('出演')
    file.write('\n')
    file.write('演过')
    file.write('\n')
    file.write('性别')
    file.write('\n')
    file.write('职业')
    file.write('\n')
    file.write('星座')
    file.write('\n')
    file.write('出生地')
    file.write('\n')
    file.write('生日')
    file.write('\n')

namewords_path = './filmnames.txt'
actorwords_path='./filmactors.txt'
directorwords_path='./filmdirectors.txt'
typesnames_path='./typesnames.txt'
keywords_path='./relation.txt'
keywords_p_path='./relation_p.txt'

def nameText(text):
    mywordlist = []
    f_name = open(namewords_path,encoding='UTF-8')
    for name in film_names:
        jieba.add_word(name)
    seg_list = jieba.cut(text,cut_all=True)
    liststr="/ ".join(seg_list)
    try:
        f_name_text = f_name.read( )
        f_name_text=str(f_name_text)
    finally:
        f_name.close()
    f_name_seg_list=f_name_text.split('\n')
    for myword in liststr.split('/'):
        if (myword.strip() in f_name_seg_list):
            mywordlist.append(myword)
    return ''.join(mywordlist)

def actorText(text):
    mywordlist = []
    f_name = open(actorwords_path,encoding='UTF-8')
    for name in actor:
        try:
            temp = str(name)
            if '·' in name:
             name=name.split('·')
             temp=''
             for i in name:
                 temp+=i
            jieba.add_word(temp)
        except:
            continue
    seg_list = jieba.cut(text,cut_all=True)
    liststr="/ ".join(seg_list)
    try:
        f_name_text = f_name.read( )
        f_name_text=str(f_name_text)
    finally:
        f_name.close()
    f_name_seg_list=f_name_text.split('\n')
    for myword in liststr.split('/'):
        if (myword.strip() in f_name_seg_list):
            mywordlist.append(myword)
    return ''.join(mywordlist)

def directorText(text):
    mywordlist = []
    f_name = open(directorwords_path,encoding='UTF-8')
    for name in director:
        try:
            name = str(name)
            if '·' in name:
                name = name.split('·')
                temp = ''
                for i in name:
                    temp += i
            jieba.add_word(temp)
        except:
            continue
    seg_list = jieba.cut(text,cut_all=True)
    liststr="/ ".join(seg_list)
    try:
        f_name_text = f_name.read( )
        f_name_text=str(f_name_text)
    finally:
        f_name.close()
    f_name_seg_list=f_name_text.split('\n')
    for myword in liststr.split('/'):
        if (myword.strip() in f_name_seg_list):
            mywordlist.append(myword)
    return ''.join(mywordlist)

def typeText(text):
    mywordlist = []
    f_name = open(typesnames_path,encoding='UTF-8')
    for name in types_names:
        jieba.add_word(name)
    seg_list = jieba.cut(text,cut_all=True)
    liststr="/ ".join(seg_list)
    try:
        f_name_text = f_name.read( )
        f_name_text=str(f_name_text)
    finally:
        f_name.close()
    f_name_seg_list=f_name_text.split('\n')
    for myword in liststr.split('/'):
        if (myword.strip() in f_name_seg_list):
            mywordlist.append(myword)
    return ''.join(mywordlist)

def keywordText(text):
    mywordlist = []
    f_name = open(keywords_path,encoding='UTF-8')
    for name in keywordlist:
        try:
            name=str(name)
            jieba.add_word(name)
        except:
            continue
    seg_list = jieba.cut(text,cut_all=True)
    liststr="/ ".join(seg_list)
    try:
        f_name_text = f_name.read( )
        f_name_text=str(f_name_text)
    finally:
        f_name.close()
    f_name_seg_list=f_name_text.split('\n')
    for myword in liststr.split('/'):
        if (myword.strip() in f_name_seg_list):
            mywordlist.append(myword)
    return ''.join(mywordlist)

def keywordText_person(text):
    mywordlist = []
    f_name = open(keywords_p_path,encoding='UTF-8')
    for name in keywordlist_person:
        try:
            name=str(name)
            jieba.add_word(name)
        except:
            continue
    seg_list = jieba.cut(text,cut_all=True)
    liststr="/ ".join(seg_list)
    try:
        f_name_text = f_name.read( )
        f_name_text=str(f_name_text)
    finally:
        f_name.close()
    f_name_seg_list=f_name_text.split('\n')
    for myword in liststr.split('/'):
        if (myword.strip() in f_name_seg_list):
            mywordlist.append(myword)
    return ''.join(mywordlist)

def intersection(list1,list2):
    inter=[]
    for item2 in list2:
        if item2 in list1:
            inter.append(item2)
    return inter

def film_default(filmlist):
    types = filmtype(filmlist)
    rate = filmrate(filmlist)
    date = filmdate(filmlist)
    country = filmregion(filmlist)
    len = filmlen(filmlist)
    language = filmlanguage(filmlist)
    actor = filmactor(filmlist)
    director = filmdirector(filmlist)
    res = []
    for i in filmlist:
        index = ["类型", "评分", "上映日期", "上映国家", "时长", "语言", "演员", "导演"]
        value = []
        value.append(types)
        value.append(rate)
        value.append(date)
        value.append(country)
        value.append(len)
        value.append(language)
        value.append(actor)
        value.append(director)
        dic = dict(zip(index, value))
        res.append(dic)
    return res
def filmrate(filmlist):   #电影评分函数
    res = []
    for i in filmlist:
        rates = []
        sql = "select movie_rate from movie_information where movie_name ='" + i + "';"
        cursor.execute(sql)
        rate = cursor.fetchone()
        rates.append(rate[0])
        res.append(rates)
    return res[0]
def filmlen(filmlist): #电影时长
    res = []
    for i in filmlist:
        lens = []
        sql = "select length from movie_information where movie_name ='" + i + "';"
        cursor.execute(sql)
        len = cursor.fetchone()
        lens.append(len[0])
        res.append(lens)
    return res[0]
def filmtype(filmlist): #电影类型
    res = []
    for i in filmlist:
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
    return res[0]
def filmdate(filmlist): #上映日期
    res = []
    for i in filmlist:
        datas = []
        sql = "select year from movie_information where movie_name ='" + i + "';"
        cursor.execute(sql)
        year = cursor.fetchone()
        datas.append(year[0])
        res.append(datas)
    return res[0]
def filmregion(filmlist): #上映地区
    res = []
    for i in filmlist:
        sql = "select country from movie_information where movie_name like '" + i + "';"
        cursor.execute(sql)
        country = cursor.fetchone()
        res.append(country[0].split(",")[1:])
    return res[0]
def filmlanguage(filmlist):  #电影语言
    res = []
    for i in filmlist:
        sql = "select language from movie_information where movie_name like '" + i + "';"
        cursor.execute(sql)
        language = cursor.fetchone()
        res.append(language[0].split(",")[1:])
    return res[0]
def filmactor(filmlist): #电影演员
    res = []
    for j in filmlist:
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
    return res[0]
def filmdirector(filmlist): #电影导演
    res = []
    for j in filmlist:
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
    return res[0]
def person_default(personlist):#输入是单元列表
    direct = persondirect(personlist)
    act = personact(personlist)
    gender = persongender(personlist)
    job = personjob(personlist)
    cons = personcons(personlist)
    birthplace = personbirthplace(personlist)
    birthday = personbirthday(personlist)
    famliy = personfamily(personlist)
    res = []
    for i in personlist:
        index = ["导演了", "演过", "性别", "职业", "星座是", "出生地", "生日", "家庭"]
        value = []
        value.append(direct)
        value.append(act)
        value.append(gender)
        value.append(job)
        value.append(cons)
        value.append(birthplace)
        value.append(birthday)
        value.append(famliy)
        dic = dict(zip(index, value))
        res.append(dic)
    return res
def persondirect(personlist):#输入是单元列表
    for i in personlist:
        sql = "select director_id from director where trim(director_name) = '" + i + "';"
        cursor.execute(sql)
        id = cursor.fetchone()
        sql = "select film_id from directed where trim(director_id) = '" + id[0] + "';"
        cursor.execute(sql)
        film_id = cursor.fetchall()
        res = []
        for j in film_id:
            sql = "select film_name from film_names where film_id=" + j[0]
            cursor.execute(sql)
            name = cursor.fetchone()
            res.append(name[0])
    return res
def personact(personlist):#输入是单元列表
    for i in personlist:
        sql = "select actor_id from actor where trim(actor_name) = '" + i + "';"
        cursor.execute(sql)
        id = cursor.fetchone()
        sql = "select film_id from acted_in where trim(actor_id) = '" + id[0] + "';"
        cursor.execute(sql)
        film_id = cursor.fetchall()
        res = []
        for j in film_id:
            sql = "select film_name from film_names where film_id=" + j[0]
            cursor.execute(sql)
            name = cursor.fetchone()
            res.append(name[0])
    return res
def persongender(personlist):#输入是单元列表
    res = []
    for i in personlist:
        sql = "select ifnull(gender,'暂无信息') from fianlly where person_name like '%" + i + "%';"
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
    res = []
    sql = "select type_id from types where trim(type_name)= trim('" + type[0] + "');"
    cursor.execute(sql)
    id = cursor.fetchone()
    sql = "select film_id from belong_to where type_id=" + id[0] + ";"
    cursor.execute(sql)
    film = cursor.fetchall()
    for i in film:
        sql = "select film_name from film_names where film_id=" + i[0] + ";"
        cursor.execute(sql)
        film_name = cursor.fetchone()
        res.append(film_name[0])
    return res

def questionInput(text):
    text=str(text).strip()
    Keywordlist=keywordText(text).lstrip(' ').split(' ')
    if Keywordlist[0]=='':
        Keywordlist=[]
    filmnamelist=nameText(text).lstrip(' ').split(' ')
    if filmnamelist[0] == '':
        filmnamelist = []
    directorlist=directorText(text).lstrip(' ').split(' ')
    if directorlist[0] == '':
        directorlist = []
    actorlist=actorText(text).lstrip(' ').split(' ')
    if actorlist[0] == '':
        actorlist = []
    typelist=typeText(text).lstrip(' ').split(' ')
    if typelist[0] == '':
        typelist = []
    Keywordlist_person=keywordText_person(text).lstrip(' ').split(' ')
    if Keywordlist_person[0] == '':
        Keywordlist_person = []
    #resultlist={}

    answer=''
    if len(filmnamelist)==1:
        answer+=filmnamelist[0]
        if len(actorlist)==0 and len(typelist)==0 and len(directorlist)==0:
            if len(Keywordlist) == 0:  # 电影基本信息
                #resultlist['基本信息'] = (film_default(filmnamelist))
                for item in film_default(filmnamelist):
                    for key, value in item.items():
                        if value[0]!='':
                            answer += str(key) + ":"
                            for i in value:
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
            else:  # 电影具体信息
                if '评分' in Keywordlist:
                    #resultlist['评分'] = (filmrate(filmnamelist))
                    answer += '评分是' + str(filmrate(filmnamelist)[0]) + '，'
                if '时长' in Keywordlist:
                    #resultlist['时长'] = (filmlen(filmnamelist))
                    answer += '时长是' + str(filmlen(filmnamelist)[0]) + '分钟，'
                if '类型' in Keywordlist:
                    #resultlist['类型'] = (filmtype(filmnamelist))
                    answer += '类型是'
                    for i in filmtype(filmnamelist):
                        answer += str(i) + '、'
                    answer = answer.rstrip('、') + '，'
                if '上映日期' in Keywordlist:
                    #resultlist['上映日期'] = (filmdate(filmnamelist))
                    answer += '上映日期是' + str(filmdate(filmnamelist)[0]) + '，'
                if '上映地区' in Keywordlist:
                    #resultlist['上映地区'] = (filmregion(filmnamelist))
                    answer += '上映地区是' + str(filmregion(filmnamelist)[0]) + '，'
                if '语言' in Keywordlist:
                    #resultlist['语言'] = filmlanguage(filmnamelist)
                    answer += '语言是' + str(filmlanguage(filmnamelist)[0]) + '，'
                if '演员' in Keywordlist:
                    #resultlist['演员'] = filmactor(filmnamelist)
                    answer += '演员是'
                    for i in filmactor(filmnamelist):
                        answer += str(i) + '、'
                    answer = answer.rstrip('、') + '，'
                if '导演' in Keywordlist:
                    #resultlist['导演'] = filmdirector(filmnamelist)
                    answer += '导演是'
                    for i in filmdirector(filmnamelist):
                        answer += str(i) + '、'
                    answer = answer.rstrip('、') + '，'
            answer = answer.rstrip('，') + '。'
    elif len(filmnamelist)==0:
        if len(actorlist)==1:
            answer += actorlist[0]
            if (len(directorlist)==0 or directorlist==actorlist):
                if len(typelist)==0:
                    if len(Keywordlist_person) == 0:  # 只有演员，问基本信息
                        #resultlist['基本信息'] = person_default(actorlist)
                        for item in person_default(actorlist):
                            for key, value in item.items():
                                if value[0]!='':
                                    answer += str(key) + ":"
                                    for i in value:
                                        answer += str(i) + '、'
                                    answer = answer.rstrip('、') + '，'
                    else:  # 只有演员问具体信息
                        if '导演' in Keywordlist_person:
                            #resultlist['导演'] = (persondirect(actorlist))
                            answer += "导演了"
                            for i in persondirect(actorlist):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
                        if '出演' in Keywordlist_person:
                            #resultlist['出演'] = (personact(actorlist))
                            answer += "出演了"
                            for i in personact(actorlist):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
                        if '演过' in Keywordlist_person:
                            #resultlist['出演'] = (personact(actorlist))
                            answer += "出演了"
                            for i in personact(actorlist):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
                        if '性别' in Keywordlist_person:
                            answer += "性别是"
                            #resultlist['性别'] = persongender(actorlist)
                            for i in persongender(actorlist):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
                        if '职业' in Keywordlist_person:
                            #resultlist['职业'] = personjob(actorlist)
                            answer += "职业是"
                            for i in personjob(actorlist):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
                        if '星座' in Keywordlist_person:
                            #resultlist['星座'] = personcons(actorlist)
                            answer += "星座是"
                            for i in personcons(actorlist):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
                        if '出生地' in Keywordlist_person:
                            #resultlist['出生地'] = personbirthplace(actorlist)
                            answer += "出生地在"
                            for i in personbirthplace(actorlist):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
                        if '生日' in Keywordlist_person:
                            #resultlist['生日'] = personbirthday(actorlist)
                            answer += "生日是"
                            for i in personbirthday(actorlist):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
                    answer = answer.rstrip('，') + '。'
                elif len(typelist) == 1:
                    #resultlist['电影'] = intersection(typefilm(typelist), personact(actorlist[0]))
                    answer += '出演的' + typelist[0] + '电影:'
                    for i in intersection(typefilm(typelist), personact([actorlist[0]])):
                        answer += str(i) + '、'
                    answer = answer.rstrip('、')
                elif len(directorlist) == 1 and len(intersection(actorlist, directorlist)) == 0:
                    answer += '和' + str(directorlist[0]) + '合作的'
                    if len(typelist) == 0:  # 演员和导演合作
                        #resultlist['合作'] = intersection(personact(actorlist), persondirect(directorlist))
                        answer += '电影:'
                        for i in intersection(personact(actorlist), persondirect(directorlist)):
                            answer += str(i) + '、'
                        answer = answer.rstrip('、')
                    if len(typelist) == 1:  # 演员和导演合作具体类型电影
                        templist = intersection(personact(actorlist), persondirect(directorlist))
                        #resultlist['合作'] = intersection(templist, typefilm(typelist))
                        answer += str(typelist[0]) + '电影:'
                        for i in intersection(templist, typefilm(typelist)):
                            answer += str(i) + '、'
                        answer = answer.rstrip('、')
                elif len(directorlist) == 2 and (actorlist[0] in directorlist):
                    answer = ''
                    answer += str(directorlist[0]) + '和' + str(directorlist[1]) + '合作的'
                    if len(typelist) == 0:  # 两个导演合作,其中一个导演也是演员
                        #resultlist['合作'] = intersection(persondirect([directorlist[0]]),
                                                        #persondirect([directorlist[1]]))
                        answer += '电影:'
                        for i in intersection(persondirect([directorlist[0]]), persondirect([directorlist[1]])):
                            answer += str(i) + '、'
                        answer = answer.rstrip('、')
                    if len(typelist) == 1:  # 两个导演合作具体类型电影，其中一个导演是演员
                        templist = intersection(persondirect([directorlist[0]]), persondirect([directorlist[1]]))
                        #resultlist['合作'] = intersection(templist, typefilm(typelist))
                        answer += str(typelist[0]) + '电影:'
                        for i in intersection(persondirect([directorlist[0]]), persondirect([directorlist[1]])):
                            answer += str(i) + '、'
                        answer = answer.rstrip('、')
        elif len(actorlist) == 2:
                    answer += str(actorlist[0]) + '和' + str(actorlist[1]) + '合作的'
                    if len(intersection(directorlist, actorlist)) == len(directorlist):
                        if len(typelist) == 0:  # 两个演员合作
                            #resultlist['合作'] = intersection(personact([actorlist[0]]), personact([actorlist[1]]))
                            answer += '电影:'
                            for i in intersection(personact([actorlist[0]]), personact([actorlist[1]])):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、')
                        if len(typelist) == 1:  # 两个演员合作具体类型电影
                            templist = intersection(personact([actorlist[0]]), personact([actorlist[1]]))
                            #resultlist['合作'] = intersection(templist, typefilm(typelist))
                            answer += str(typelist[0]) + '电影:'
                            for i in intersection(templist, typefilm(typelist)):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、')
        elif len(actorlist)==0:
            if len(directorlist)==1:
                answer += directorlist[0]
                if len(typelist)==0:
                    if len(Keywordlist_person) == 0:  # 只有导演，问导演基本信息
                        #resultlist['基本信息'] = person_default(directorlist)
                        for item in person_default(directorlist):
                            for key, value in item.items():
                                if value[0]!='':
                                    answer += str(key) + ":"
                                    for i in value:
                                        answer += str(i) + '、'
                                    answer = answer.rstrip('、') + '，'
                    else:  # 只有导演问导演详细信息
                        if '导演' in Keywordlist_person:
                            #resultlist['导演'] = (persondirect(directorlist))
                            answer += "导演了"
                            for i in persondirect(directorlist):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
                        if '性别' in Keywordlist_person:
                            #resultlist['性别'] = persongender(directorlist)
                            answer += "性别是"
                            for i in persongender(directorlist):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
                        if '职业' in Keywordlist_person:
                            #resultlist['职业'] = personjob(directorlist)
                            answer += "职业是"
                            for i in personjob(directorlist):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
                        if '星座' in Keywordlist_person:
                            #resultlist['星座'] = personcons(directorlist)
                            answer += "星座是"
                            for i in personcons(directorlist):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
                        if '出生地' in Keywordlist_person:
                            #resultlist['出生地'] = personbirthplace(directorlist)
                            answer += "出生地"
                            for i in personbirthplace(directorlist):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
                        if '生日' in Keywordlist_person:
                            #resultlist['生日'] = personbirthday(directorlist)
                            answer += "生日是"
                            for i in personbirthday(directorlist):
                                answer += str(i) + '、'
                            answer = answer.rstrip('、') + '，'
                    answer = answer.rstrip('，') + '。'
                elif len(typelist) == 1:
                    #resultlist['电影'] = intersection(typefilm(typelist), persondirect(directorlist[0]))
                    answer += '出演的' + typelist[0] + '电影:'
                    for i in intersection(typefilm(typelist), persondirect([directorlist[0]])):
                        answer += str(i) + '、'
                    answer = answer.rstrip('、')
            elif len(directorlist) == 2:
                answer += str(directorlist[0]) + '和' + str(directorlist[1]) + '合作的'
                if len(typelist) == 0:  # 两个导演合作
                        #resultlist['合作'] = intersection(persondirect([directorlist[0]]),
                                                        #persondirect([directorlist[1]]))
                        answer += '电影:'
                        for i in intersection(persondirect([directorlist[0]]), persondirect([directorlist[1]])):
                            answer += str(i) + '、'
                        answer = answer.rstrip('、')
                if len(typelist) == 1:  # 两个导演合作具体类型电影
                        templist = intersection(persondirect([directorlist[0]]), persondirect([directorlist[1]]))
                        #resultlist['合作'] = intersection(templist, typefilm(typelist))
                        answer += str(typelist[0]) + '电影:'
                        for i in intersection(templist, typefilm(typelist)):
                            answer += str(i) + '、'
                        answer = answer.rstrip('、')
            elif len(directorlist) == 0:
                    if len(typelist) > 0:
                        #resultlist['电影'] = typefilm(typelist)
                        for i in typelist:
                            answer += i + '、'
                        answer = answer.rstrip('、') + '电影:'
                        for j in typefilm(typelist):
                            answer += j + '，'
                        answer = answer.rstrip('，')
    if answer=='':
        answer='对不起，我不知道'
    return answer

