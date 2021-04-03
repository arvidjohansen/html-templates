#from selenium import webdriver
#driver = webdriver.Firefox()
import requests
from bs4 import BeautifulSoup
import os

url = 'https://html5up.net'

r = requests.get(url, verify=False)

html = r.content

soup = BeautifulSoup(html, 'html.parser')

h2s = soup.find_all('h2')

def write(content, filename):
    fsize = 0
    try: 
        fsize = os.stat(filename).st_size
    except FileNotFoundError: pass
    if fsize > 3386:
        print(f'Fsize: {fsize}, skipping {filename}')
    with open(filename, 'wb') as f:
        f.write(content)
        print(f'Finished writing to {filename}')

skip = []
for h2 in h2s:
    fname = f'{h2.text}.zip'
   
    try:
        fsize = os.stat(fname).st_size
        print(f'{fname} = {fsize} bytes')
        if fsize == 3386:
            continue#skip.append(fname)
            print(f'Skipping{fname}')
    except FileNotFoundError as e:
        continue#skip.append(fname)
        print(f'Skipping{fname} -> notfound')
    skip.append(fname)

input(f'skips: {skip}\nContinue?')

for h2 in h2s:
    fname = h2.text+'.zip'
    target = h2.parent.find_all('a')[-1]['href']
    target = url + target
    if fname in skip:
        print(f'Skipping {fname}..')
        continue
    dl = requests.get(target, verify=False)
    write(dl.content,fname)
    
    
