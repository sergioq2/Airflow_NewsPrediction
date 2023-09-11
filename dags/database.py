import pymongo
import datetime as dtm
import pandas as pd

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['News_colombiano']
collection = db.prediction_collection

class DataBase:
    def __init__(self):
        pass
    
    def savedata(self):
        date = dtm.datetime.now().strftime("%Y-%m-%d")
        news = pd.read_excel('../news/news.xlsx', sheet_name='Sheet1')
        news = news.to_dict('records')
        collection.insert_many(news)
        return "Data saved"

if __name__ == '__main__':
    database = DataBase()
    database.savedata()