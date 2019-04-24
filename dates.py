import os
import datetime as dt
import pandas as pd


os.chdir('C:/Users/bala0/OneDrive/My_Mine/My_Study/My_Python/My_Codes/Fundamentals')
df = pd.read_csv('htmlconv1.csv', na_values=['NA', 'N/A','Na'])
cd = df["Closing Date"]
for da in cd:
    print(da)
    ob=dt.datetime.strptime(da, '%d-%b-%y')
    print(ob)
    st=str(ob)
    st=st[0:10:]
    print(st)
