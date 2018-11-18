'''
插入百万数据检测
Date:2018-11-10
'''
from time import ctime
from pymongo  import MongoClient

client = MongoClient('localhost',27017)
db = client['blog_test']
collection = db['Mass_datas']

try:
    print(ctime())

    #方案一：使用insert_many批量插入
    articles = ({'name':str(i),'title':'python'} for i in range(1,1000000))
    collection.insert_many(articles)


    #方案二：使用insert_one逐个插入
    # i = 1000001   #插入十万数据
    # while i <= 1100000:
    #     article = ({'name': str(i), 'title': 'python basement'})
    #     collection.insert_one(article)
    #     i += 1

    print(ctime())

    #使用Mongoengine
    # article = Article(name=str(i),title='python')
    # article.switch_collection('Mass_datas')
    # article.save()
except Exception as e:
    print(e)
