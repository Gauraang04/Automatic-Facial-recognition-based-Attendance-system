import openpyxl 
import pandas as pd
import os
import datetime
import time


'''
def attend(s):
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    sheet=date#+'_'+Hour+':'+Minute
    mode = 'a' if os.path.exists('Attendance.xlsx') else 'w'
    f = pd.DataFrame(s)
    with pd.ExcelWriter('Attendance.xlsx', mode=mode) as writer:
        f.to_excel(writer, sheet_name=sheet, index=False)

'''
s=['Deep','Gauraang','satya']
co=['name']
att=pd.DataFrame(columns=co)
print(len(s))
for i in range (0,len(s)):
    att.loc[len(att)]=s[i]
att.drop_duplicates(['name'],keep='first')
print(att)
with pd.ExcelWriter('tets.xlsx',mode='a') as w:
    att.to_excel(w,sheet_name='10')

