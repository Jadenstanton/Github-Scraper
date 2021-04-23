import requests
from bs4 import BeautifulSoup as bs


#declare variable that collects username of profile
github_user = input("Input Guthub User: ")

#specify url
url = "https://github.com/" +github_user

#send request to url
r = requests.get(url)

#use BeautifulSoup to get specific html source code
soup = bs(r.content, "html.parser")

#declare variable for prof image and find html components
profile_image = soup.find("img", {"alt" : "Avatar"})["src"]

#print
print(profile_image)