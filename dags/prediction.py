import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from transformers import DistilBertTokenizer
from transformers import TextClassificationPipeline
from transformers import TFDistilBertForSequenceClassification, TFTrainer, TFTrainingArguments
import tensorflow as tf
import datetime as dtm
from loadmodel import ModelLoader

class NewsPredictor:
    def __init__(self):
        pass

    def predict_and_save_to_excel(self):
        prediction_list = []
        date = dtm.datetime.now().strftime("%Y-%m-%d")
        df = pd.read_excel(f'../news/news_{date}.xlsx', sheet_name='Sheet1')
        model_loader = ModelLoader()
        for text in df['news'].to_list():
            prediction_value, text = model_loader.load_model(text)
            prediction_list.append(prediction_value)
        df['prediction'] = prediction_list
        df.to_excel(f'../news/news_{date}.xlsx', index=False)
        return "Prediction saved"

if __name__ == '__main__':
    predictor = NewsPredictor()
    predictor.predict_and_save_to_excel()