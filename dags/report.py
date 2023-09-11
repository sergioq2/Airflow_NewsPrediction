import pandas as pd
import datetime as dtm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class DataReporter:
    def __init__(self, news, email, password):
        self.news = news
        self.email = email
        self.password = password

    def report(self):
        negative_news = self.news[self.news['prediction'] == 0]
        positive_news = self.news[self.news['prediction'] == 2]
        negative_news = negative_news['news'].to_list()
        positive_news = positive_news['news'].to_list()
        negative_news = '\n'.join(negative_news)
        positive_news = '\n'.join(positive_news)
        return {
            'negative_news': negative_news,
            'positive_news': positive_news
        }

    def send_email(self):
        date = dtm.datetime.now().strftime("%Y-%m-%d")
        df = pd.read_excel(f'news/news_{date}.xlsx', sheet_name='Sheet1')
        reporte = self.report()
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = self.email
        smtp_password = self.password

        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = to_email
        msg['Subject'] = 'Informe de noticias'

        body = f'''
        Noticias Negativas:
        {reporte['negative_news']}

        Noticias Positivas:
        {reporte['positive_news']}
        '''
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, to_email, msg.as_string())
            server.quit()
            print("Correo enviado con éxito")
        except Exception as e:
            print(f"Error al enviar el correo: {str(e)}")

if __name__ == '__main__':
    date = dtm.datetime.now().strftime("%Y-%m-%d")
    path = '../news/' + 'news_' + str(date) + '.xlsx'
    to_email = 'sergio.quintero.1804@gmail.com'
    password = 'password_dummy'
    visualizer = DataReporter(path, to_email, password)
    visualizer.send_email(to_email)

        


