from py2neo import Graph,Node,Relationship
import json
import pandas as pd
import csv
class UpdateParams:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        print(f"没有该属性:{item}")
        return None


def json2obj(json_data):
    d = UpdateParams.__new__(UpdateParams)
    d.__dict__.update(json_data)
    return d
graph=Graph("http://localhost:7474",auth=('neo4j','123456'))
def find_actor_in_film(film_name):
    ans=graph.run("match (movie:movie{film_names:\""+film_name+"\"})-[:acted_in]->(actor:person) return"
                            " {name:movie.film_names,des:movie.index},{name:actor.actor,des:actor.index}").data()
    count=1
    datas=[]
    link=[]
    temp={'source':'','target':'','name':'演员','des':2}
    for item in ans:
        for key,values in item.items():
           if count%2==0:
               temp['target']=values['name']
               link.append(temp)
               values['symbolSize'] = 40
               values['category'] = 0
               datas.append(values)
           else:
               temp={'source':'','target':'','name':'演员','des':2}
               temp['source']=values['name']
           count=count+1

    return {'data':datas,'link':link}

def find_director_in_film(film_name):
    ans = graph.run(
        "match (movie:movie{film_names:\"" + film_name + "\"})-[:directed]->(director:person) return "
                            "{name:movie.film_names,des:movie.index},{name:director.director,des:director.index}").data()
    count = 1
    datas = []
    link=[]
    temp={'source':'','target':'','name':'导演','des':3}
    for item in ans:
        for key, values in item.items():
            if count % 2 == 0:
                temp['target'] = values['name']
                link.append(temp)
                values['symbolSize'] = 50
                values['category'] = 1
                datas.append(values)
            else:
                temp = {'source': '', 'target': '', 'name': '导演', 'des': 3}
                temp['source'] = values['name']
            count = count + 1
    return {'data':datas,'link':link}

def find_film_of_actor(actor):
    ans = graph.run(
        "match (movie:movie)-[:acted_in]->(actor:person{actor:\""+actor+"\"}) return "
                            "{name:actor.actor,des:actor.index},{name:movie.film_names,des:movie.index}").data()
    count = 1
    datas = []
    link = []
    temp = {'source': '', 'target': '', 'name': '出演', 'des': 0}
    for item in ans:
        for key, values in item.items():
            if count % 2 == 0:
                temp['target'] = values['name']
                link.append(temp)
                values['symbolSize'] = 60
                values['category'] = 2
                datas.append(values)
            else:
                temp = {'source': '', 'target': '', 'name': '出演', 'des': 0}
                temp['source'] = values['name']
            count = count + 1
    return {'data': datas, 'link': link}

def find_film_of_director(director):
    ans = graph.run(
        "match (movie:movie)-[:directed]->(director:person{director:\"" + director + "\"}) return "
                            "{name:director.director,des:director.index},{name:movie.film_names,des:movie.index}").data()
    count = 1
    datas = []
    link = []
    temp = {'source': '', 'target': '', 'name': '导演', 'des': 1}
    for item in ans:
        for key, values in item.items():
            if count % 2 == 0:
                temp['target'] = values['name']
                link.append(temp)
                values['symbolSize'] = 60
                values['category'] = 2
                datas.append(values)
            else:
                temp = {'source': '', 'target': '', 'name': '导演', 'des': 1}
                temp['source'] = values['name']
            count = count + 1
    return {'data': datas, 'link': link}


def find_director_actor(director):
    ans = graph.run(
        "match (actor:person)-[:cooperation]->(director:person{director:\"" + director + "\"}) return "
                            "{name:director.director,des:director.index},{name:actor.actor,des:actor.index}").data()
    count = 1
    datas = []
    link = []
    temp = {'source': '', 'target': '', 'name': '合作', 'des': 4}
    for item in ans:
        for key, values in item.items():
            if count % 2 == 0:
                if values['name'] == director:
                    continue
                temp['target'] = values['name']
                link.append(temp)
                values['symbolSize'] = 40
                values['category'] = 0
                datas.append(values)
            else:
                temp = {'source': '', 'target': '', 'name': '合作', 'des': 4}
                temp['source'] = values['name']
            count = count + 1
    return {'data': datas, 'link': link}

def find_actor_director(actor):
    ans = graph.run(
        "match (actor:person{actor:\"" + actor + "\"})-[:cooperation]->(director:person) return "
                            "{name:actor.actor,des:actor.index},{name:director.director,des:director.index}").data()
    count = 1
    datas = []
    link = []
    temp = {'source': '', 'target': '', 'name': '合作', 'des': 4}
    for item in ans:
        for key, values in item.items():
            if count % 2 == 0:
                if values['name'] == actor:
                    continue
                temp['target'] = values['name']
                link.append(temp)
                values['symbolSize'] = 50
                values['category'] = 1
                datas.append(values)
            else:
                temp = {'source': '', 'target': '', 'name': '合作', 'des': 4}
                temp['source'] = values['name']
            count = count + 1
    return {'data': datas, 'link': link}

def find_type_of_film(film_name):
    ans = graph.run("match (movie:movie{film_names:\""+film_name+"\"})-[:belong_to]->(type:type) return "
                            "{name:movie.film_names,des:movie.index},{name:type.types,des:type.index}").data()
    count = 1
    datas = []
    link = []
    temp = {'source': '', 'target': '', 'name': '类型', 'des': 5}
    for item in ans:
        for key, values in item.items():
            if count % 2 == 0:
                temp['target'] = values['name']
                link.append(temp)
                values['symbolSize'] = 70
                values['category'] = 3
                datas.append(values)
            else:
                temp = {'source': '', 'target': '', 'name': '类型', 'des': 5}
                temp['source'] = values['name']
            count = count + 1
    return {'data': datas, 'link': link}

def find_film_type(type_name):
    ans = graph.run(
        "match (movie:movie)-[:belong_to]->(type:type{types:\"" + type_name + "\"}) return "
                             "{name:type.types,des:type.index},{name:movie.film_names,des:movie.index}").data()
    count = 1
    datas = []
    link = []
    temp = {'source': '', 'target': '', 'name': '电影', 'des': 6}
    for item in ans:
        for key, values in item.items():
            if count % 2 == 0:
                temp['target'] = values['name']
                link.append(temp)
                values['symbolSize'] = 60
                values['category'] = 2
                datas.append(values)
            else:
                temp = {'source': '', 'target': '', 'name': '电影', 'des': 6}
                temp['source'] = values['name']
            count = count + 1
    return {'data': datas, 'link': link}



def find_person(content):
    data1=find_film_of_actor(content)
    data2=find_film_of_director(content)
    data3=find_actor_director(content)
    data4=find_director_actor(content)
    name_set=set()
    person_set=set()
    nodes=[]
    node=graph.run("match (p:person{actor:\""+content+"\"})  return "
                                                      "{name:p.actor,des:p.index}").data()
    for item in node:
        for key,values in item.items():
            values['symbolSize'] = 40
            values['category'] = 0
            nodes.append(values)
    for i in data1['data']:
        if i['name'] not in name_set:
            nodes.append(i)
            name_set.add(i['name'])
    for i in data2['data']:
        if i['name'] not in name_set:
            nodes.append(i)
            name_set.add(i['name'])
    for i in data3['data']:
        if i['name'] not in person_set:
            nodes.append(i)
            person_set.add(i['name'])
    for i in data4['data']:
        if i['name'] not in person_set:
            nodes.append(i)
            person_set.add(i['name'])
    links=[]
    for i in data1['link']:
        links.append(i)
    for i in data2['link']:
        links.append(i)
    for i in data3['link']:
        links.append(i)
    for i in data4['link']:
        links.append(i)
    result={}
    result['data']=nodes
    result['link']=links
    return result

def find_film(content):
    person_set=set()
    type_set=set()
    data1=find_actor_in_film(content)
    data2=find_director_in_film(content)
    data3=find_type_of_film(content)
    nodes=[]
    node = graph.run("match (movie:movie{film_names:\"" + content + "\"})  return "
                                                            "{name:movie.film_names,des:movie.index}").data()
    for item in node:
        for key, values in item.items():
            values['symbolSize'] = 60
            values['category'] = 2
            nodes.append(values)
    for i in data1['data']:
        if i['name'] not in person_set:
            nodes.append(i)
            person_set.add(i['name'])
    for i in data2['data']:
        if i['name'] not in person_set:
            nodes.append(i)
            person_set.add(i['name'])
    for i in data3['data']:
        if i['name'] not in type_set:
            nodes.append(i)
            type_set.add(i['name'])

    links = []
    for i in data1['link']:
        links.append(i)
    for i in data2['link']:
        links.append(i)
    for i in data3['link']:
        links.append(i)
    result = {}
    # itemnodes=[]
    # itemlinks=[]
    # for i in nodes:
    #     itemnodes.append(json2obj(i))
    # for i in links:
    #     itemlinks.append(json2obj(i))
    # result['data'] = itemnodes
    # result['link'] = itemlinks
    result['data']=nodes
    result['link']=links
    return result

def find_type(content):
    data1=find_film_type(content)
    film_set=set()
    nodes=[]
    node = graph.run("match (type:type{types:\"" + content + "\"})  return "
                                                                    "{name:type.types,des:type.index}").data()
    for item in node:
        for key, values in item.items():
            values['symbolSize'] = 70
            values['category'] = 3
            nodes.append(values)
    for x in data1['data']:
        if x['name'] not in film_set:
            nodes.append(x)
            film_set.add(x['name'])
    links=[]
    for y in data1['link']:
        links.append(y)
    result={}
    result['data']=nodes
    result['link']=links
    return result





