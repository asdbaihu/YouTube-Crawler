import requests
import os
import webbrowser
from bs4 import BeautifulSoup

os.system('chcp 65001')

def divider():
    print('*-*'*20)

base_url = "https://www.youtube.com"

print("Input your search word")

search_query = input()
search_query = search_query.split()
search_query = '+'.join(search_query)

os.system('cls')
print("[*] Query: {}".format(search_query))
divider()

final_url = base_url + '/results?search_query=' + search_query
req = requests.get(final_url)
html = req.content
soup = BeautifulSoup(html, 'html.parser')
results_div = soup.find('div', attrs={'id': 'results'})
item_section_ol = results_div.find('ol', attrs={'class', 'item-section'})
results = [{'text': li.find('a', attrs={'class': 'yt-uix-tile-link'})['title'], 'href': li.find('a', attrs={'class': 'yt-uix-tile-link'})['href']} for li in item_section_ol.findAll('li') if li.find('a', attrs={'class': 'yt-uix-tile-link'}) is not None]

for result in results:
    print("[{}] {}".format(results.index(result), result['text']))
    divider()

print("[+] Enter Vid Index: ")
vid_index = input()

try:
    vid_index = int(vid_index)
    webbrowser.open_new_tab(base_url + results[vid_index]['href'])
    exit(0)
except Exception as e:
    print("[-] Invalid Index!", str(e))
    exit(1)
