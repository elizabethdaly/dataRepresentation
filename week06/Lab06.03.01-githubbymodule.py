## week06 Lab06.03.01-githubbymodule.py
## From cmder do:
## pip install PyGitHub 

from github import Github
import requests # to send http requests

## comment out - before use,  or leave in when committing
g = Github("b-e4ad8ac2580705e1634fd14ebc10b828283be1-2")

## 3. Get list of repositories
#for repo in g.get_user().get_repos():
#    print(repo.name)

## 4. Get clone url of poems repo
repo = g.get_repo("elizabethdaly/poems")
print(repo.clone_url)

## 5. Get download url for file Heaney1.txt in this repo
fileInfo = repo.get_contents("Heaney1.txt")
urlOfFile = fileInfo.download_url
print(urlOfFile) 

## 7. Use 'urlOfFile' above to get the contents of the file
response = requests.get(urlOfFile)
contentOfFile = response.text
#print(contentOfFile)

## 8. Append the text "more stuff" to the contents of the file with \n
newContents = contentOfFile + "\n more stuff \n"
print(newContents)

## 9. Update the contents of the file on GitHub
gitHubResponse = repo.update_file(fileInfo.path, "Updated by DR program", newContents, fileInfo.sha)
print(gitHubResponse)