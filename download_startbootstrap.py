#from selenium import webdriver
#driver = webdriver.Firefox()
import requests
from bs4 import BeautifulSoup
import os
from varinfo import *

url = 'https://startbootstrap.com'
args = '/?showPro=false'
urlargs = url + args

def getsoup(url):
    r = requests.get(url, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

soup = getsoup(urlargs)
titles = soup.find_all('div',class_='h6 mb-0')
exclude = ['Pro HTML Bundle','Pro Angular Bundle']
titles = [t for t in titles if t.text not in exclude]

turls = []
for t in titles:
    turl = url + t.parent.parent.parent.find('a')['href']
    turls.append(turl)

dls = ['https://github.com/startbootstrap/startbootstrap-sb-admin-2/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-sb-admin/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-freelancer/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-agency/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-creative/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-simple-sidebar/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-grayscale/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-clean-blog/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-resume/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-landing-page/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-shop-homepage/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-stylish-portfolio/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-coming-soon/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-modern-business/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-scrolling-nav/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-bare/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-one-page-wonder/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-blog-home/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-business-casual/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-blog-post/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-heroic-features/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-new-age/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-business-frontpage/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-small-business/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-shop-item/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-full-width-pics/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-clean-blog-jekyll/archive/gh-pages.zip',
 'https://github.com/startbootstrap/startbootstrap-the-big-picture/archive/gh-pages.zip']

failed = ['https://startbootstrap.com/theme/sb-admin-pro',
 'https://startbootstrap.com/theme/material-admin-pro',
 'https://startbootstrap.com/theme/sb-ui-kit-pro',
 'https://startbootstrap.com/theme/sb-admin-pro-angular',
 'https://startbootstrap.com/theme/sb-ui-kit-pro-angular',
 'https://startbootstrap.com/theme/sb-ui-kit-pro-vue',
 'https://startbootstrap.com/theme/clean-blog-angular',
 'https://startbootstrap.com/template/sb-admin-angular']

def write(url,filename):
    print(f'Downloading {url}')
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)
    print(f'Finished writing {filename} to disk.')

for dl in dls:
    fname = dl.split('/')[-3]+'-'+dl.split('/')[-1]
    #print(fname)
    write(dl,fname)
"""
for turl in turls:
    soup = getsoup(turl)
    try:
        dl = soup.find_all('a',class_='btn btn-primary btn-lg btn-block font-weight-500')[0]['href']
    except IndexError as e:
        print(e)
        failed.append(turl)
        continue
    dls.append(dl)
"""




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

"""
for h2 in h2s:
    fname = h2.text+'.zip'
    target = h2.parent.find_all('a')[-1]['href']
    target = url + target
    if fname in skip:
        print(f'Skipping {fname}..')
        continue
    dl = requests.get(target, verify=False)
    write(dl.content,fname)
"""
    
