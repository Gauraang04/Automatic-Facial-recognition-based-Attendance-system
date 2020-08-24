from openpyxl import *
import pandas as pd
import os

for i in range(1,4):
        s = ['Gauraang','Deep']
        f = pd.DataFrame(s)
        with pd.ExcelWriter('sample.xlsx', mode='a') as writer:
            f.to_excel(writer, sheet_name='Sheet{}'.format(i), index=False)

        i=i+1




'''
col_names =  ['Id','Name']
a=['deep','Gauraang']
ab=pd.Series(a)
fileName="Attendance.csv"
ab = pd.DataFrame(columns = col_names)
ab = pd.DataFrame(columns = a)
ab.to_csv(fileName,index=False)
'''
'''
df = pd.DataFrame({'name':['deep','Gauraang']})
print(df)
fileName="Attendance.csv"
df.to_csv(fileName)
'''
'''
def save_attendance():
        wb = xlwt.Workbook()
        ws = wb.add_sheet("My Sheet")
        for i, row in enumerate(DATA):
            for j, col in enumerate(row):
                ws.write(i, j, col)
        wb.save(e2_2.get()+"_"+e1_2.get()+".xls")
'''
