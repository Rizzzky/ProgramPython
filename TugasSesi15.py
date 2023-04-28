import pandas as p
import plotly.express as lot

data = p.read_excel('C:/Users/RizkyFauzi/Downloads/Saham.xlsx')

bulan = ['JAN','FEB','MAR','APR','MEI','JUN','JUL','AGU','SEP','OKT','NOV','DES']
p=lot.line(data,x='TAHUN',y=bulan,labels={'TAHUN':'Tahun','value':'Nilai'},title='Grafik Saham')
p.show()
