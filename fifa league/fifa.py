import pandas as pd
import requests
from bs4 import *

# Parameters
names = []
ages = []
ova = []
pot = []
team = []
contract = []
values = []
wages = []
total_stats = []

a = [0, 60, 120, 180, 240, 300, 360, 420, 480, 540]

for i in a:
    url = f"https://sofifa.com/players?offset={i}"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    item_body = soup.findAll('tbody', {'class':'list'})
    #names = [fit.a for fit in soup.findAll('tbody', attrs={'class':'list'})]
    for i in item_body:
        names = [fit['data-tooltip'] for fit in i.find_all('a',{'class':'tooltip'})]
        ages = [fit.text for fit in i.find_all('td',{'class':'col col-ae'})]
        ova = [fit.text for fit in i.find_all('td',{'class':'col col-oa'})]
        pot = [fit.text for fit in i.find_all('td',{'class':'col col-pt'})]
        team = [fit.find('a').text for fit in i.find_all('div',{'class':'bp3-text-overflow-ellipsis'}) if fit.find('a') is not None]
        contract = [fit.text for fit in i.find_all('div',{'class':'sub'})]
        values = [fit.text for fit in i.find_all('td',{'class':'col col-vl'})]
        wages = [fit.text for fit in i.find_all('td',{'class':'col col-wg'})]
        total_stats = [fit.text for fit in i.find_all('td',{'class':'col col-tt'})]
    
        df = pd.DataFrame({
            "Name": names,
            "Age": ages,
            "Ovarall_Rating": ova,
            "Potential": pot,
            "Team_Name": team,
            "Contract": contract,
            "Value(M)": values,
            "Wages(K)": wages,
            "Total_STats": total_stats
            })

df.head()
df.to_csv('fifa1.csv')
