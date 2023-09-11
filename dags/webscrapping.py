import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import datetime as dtm

class WebScraper:

    def __init__(self, url, path):
        self.url = url
        self.path = path

    @staticmethod
    def remove_accents(text):
        text = text.lower()
        text = text.replace('á', 'a')
        text = text.replace('é', 'e')
        text = text.replace('í', 'i')
        text = text.replace('ó', 'o')
        text = text.replace('ú', 'u')
        translator = str.maketrans('', '', '¿?¡!(),.;:«»"“”…–-—’‘’')
        text = text.translate(translator)
        return text

    def scrape(self):
        pedido_obtenido = requests.get(self.url)
        pedido_obtenido.encoding = 'utf-8'
        html_obtenido = pedido_obtenido.text
        soup = BeautifulSoup(html_obtenido, 'html.parser')
        news = []
        h3_todos = soup.find_all('h3')
        for h3 in h3_todos:
            texto = h3.text.strip()
            texto = self.remove_accents(texto)
            news.append(texto)
        return news

    def create_dataframe(self):
        news = self.scrape()
        df = pd.DataFrame(np.array(news), columns=['news'])
        df.to_excel(self.path, index=False)
        return "Archivo creado"

    def main(self):
        news = self.scrape()
        result = self.create_dataframe()
        return result

if __name__ == '__main__':
    date =     date = dtm.datetime.now().strftime("%Y-%m-%d")
    path = '../news/' + 'news_' + str(date) + '.xlsx'
    scraper = WebScraper('https://www.elcolombiano.com/lo-ultimo', path)
    scraper.main()