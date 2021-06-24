import urllib.request
import os
import datetime
import csv

#Download spreadsheet
url = 'https://docs.google.com/spreadsheets/d/1X8jb3bc6dVpKDpUkt1XA2x3TWtJaLuDWC2qByocMiFg/export?gid=871681305&format=csv'
urllib.request.urlretrieve(url, '/Users/carsonmarano/Desktop/SURF2021/Code/CASPARtest/testCASPAR.csv')

#Function to add, commit, and push to git
def uploadToGit():
	message = "Automated update " + str(datetime.datetime.now())
	#os.system("cd ~/Desktop/SURF2021/Code/CASPARtest")
	os.system("git fetch")
	os.system("git add " + "testCASPAR.csv")
	os.system("git commit -m " + "'" + message +"'")
	os.system("git push")

uploadToGit()