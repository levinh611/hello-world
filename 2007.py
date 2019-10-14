import requests
from bs4 import BeautifulSoup
url = requests.get('http://vietbao.vn/vn/thoitiet/Ho-Chi-Minh-City/').text
soup = BeautifulSoup(url, 'html.parser')
hello = soup.find('div', class_='body rows')
period1 = [hello1.find('div', class_='col col-time').get_text() for hello1 in hello]
period2 = [hello2.find('div',class_='col col-summary').get_text() for hello2 in hello]
period3 = [hello3.find('div',class_='col col-temp').get_text() for hello3 in hello]
period4 = [hello4.find('div',class_='col col-humidity').get_text() for hello4 in hello]
period5 = [hello5.find('div',class_='col col-wind').get_text() for hello5 in hello]
period6 = [hello6.find('div',class_='col col-pressure').get_text() for hello6 in hello]
period7 = [hello7.find('div',class_='col col-visibility').get_text() for hello7 in hello]
period8 = [hello8.find('div',class_='col col-amountrain').get_text() for hello8 in hello]
import pandas as pd
wheathers = pd.DataFrame(
	{
		'Time': period1,
		'Summary':period2,
        'Temp':period3,
        'Humidity':period4,
        'Wind':period5,
        'Pressure':period6,
        'Visibility':period7,
        'Amountrain':period8
	})
import sqlalchemy
database_username = 'root'
database_password = '123456'
database_ip       = '127.0.0.1'
database_name     = 'sys'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password,
                                                      database_ip, database_name))
wheathers.to_sql(con=database_connection, name='table_name_for_df', if_exists='replace')
