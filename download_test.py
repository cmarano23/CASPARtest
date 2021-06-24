#Download spreadsheet
import urllib.request
import os
import datetime

url = 'https://docs.google.com/spreadsheets/d/1X8jb3bc6dVpKDpUkt1XA2x3TWtJaLuDWC2qByocMiFg/export?gid=871681305&format=csv'
urllib.request.urlretrieve(url, '/Users/carsonmarano/Desktop/SURF2021/Code/CASPARtest/testCASPAR.csv')

import csv
from pushToGit import push_file_to_github_repo_branch as push

gitHubFileName = "testCASPAR.csv"
fileName = "/Users/carsonmarano/Desktop/SURF2021/testCASPAR.csv"
repo_slug = "cmarano23/CASPARtest"
branch = "main"
user = "cmarano23"
token = "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"

def commit():
	message = "Automated update " + str(datetime.datetime.now())
	os.system("cd ~/Desktop/SURF2021/Code/CASPARtest")
	os.system("git add " + "testCASPAR.csv")
	os.system("git commit -m " + message)
	os.system("git push")

commit()

#push.push_to_repo_branch(gitHubFileName, fileName, repo_slug, branch, user, token)



#Upload to github
#from github import GitHub
#self = "cmarano23"
#password = "#44Cjm2019"
#g = GitHub(password)
#repo = g.get_user.get_repo(cmarano23/CASPARtest)
#all_files = []
#contents = repo.get_contents("")
#while contents:
#    file_content = contents.pop(0)
#    if file_content.type == "dir":
#        contents.extend(repo.get_contents(file_content.path))
#    else:
#        file = file_content
#        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))
#
#with open('/Users/carsonmarano/Desktop/SURF2021/testCASPAR.csv', 'r') as file:
#    content = file.read()
#
## Upload to github
#git_prefix = 'main/'
#git_file = git_prefix + 'testCASPAR.csv'
#if git_file in all_files:
#    contents = repo.get_contents(git_file)
#    repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
#    print(git_file + ' UPDATED')
#else:
#    repo.create_file(git_file, "committing files", content, branch="master")
#    print(git_file + ' CREATED')