import pandas as pd
import numpy as np

DataPath = 'https://brilliantinfotech-my.sharepoint.com/personal/nan_kong_brilliantinfotech_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fnan%5Fkong%5Fbrilliantinfotech%5Fcom%2FDocuments%2FBrilliantInfotech%2FtestingFolder/'
testDat_df = pd.read_csv(DataPath + 'testDat.csv')  # HTTPError: Forbidden???

#####
import cdata.onedrive as mod
conn = mod.connect("User=user@domain.com; Password=password;")
 
#Create cursor and iterate over results
cur = conn.cursor()
cur.execute("SELECT * FROM Files")
 
rs = cur.fetchall()
 
for row in rs:
print(row)

######
import urllib.request

url = 'https://onedrive.live.com/view.aspx?cid=.....app=Excel'
url = 'https://brilliantinfotech-my.sharepoint.com/personal/nan_kong_brilliantinfotech_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fnan%5Fkong%5Fbrilliantinfotech%5Fcom%2FDocuments%2FBrilliantInfotech%2FtestingFolder/'

urllib.request.urlretrieve(url, "testDat.csv")  # HTTPError: Forbidden???







