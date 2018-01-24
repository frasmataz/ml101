from bs4 import BeautifulSoup
import urllib.request

number_of_pages = 10
randomize_link = 'https://www.wikihow.com/Special:Randomizer'

for i in range(number_of_pages):
    http_doc = urllib.request.urlopen(randomize_link).read()
    soup = BeautifulSoup(http_doc)

