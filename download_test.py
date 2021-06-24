import urllib.request
import os
import datetime
import csv

#Download spreadsheet
url_csv = 'https://docs.google.com/spreadsheets/d/1X8jb3bc6dVpKDpUkt1XA2x3TWtJaLuDWC2qByocMiFg/export?format=csv'
url_xlsx = 'https://docs.google.com/spreadsheets/d/1X8jb3bc6dVpKDpUkt1XA2x3TWtJaLuDWC2qByocMiFg/export?format=xlsx'
urllib.request.urlretrieve(url_csv, '/Users/carsonmarano/Desktop/SURF2021/Code/CASPARtest/testCASPAR.csv')
urllib.request.urlretrieve(url_xlsx, '/Users/carsonmarano/Desktop/SURF2021/Code/CASPARtest/testCASPAR.xlsx')

#Function to add, commit, and push to git
def uploadToGit():
	message = "Automated update " + str(datetime.datetime.now())
	os.system("git fetch")
	os.system("git add " + "testCASPAR.csv")
	os.system("git commit -m " + "'" + message +"'")
	os.system("git push")

uploadToGit()