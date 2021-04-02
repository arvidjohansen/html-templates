import os
import django
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
from selenium import webdriver
from time import sleep

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['.']#'templates/'],
    }
]
settings.configure(TEMPLATES=TEMPLATES)
django.setup()

template = get_template('index.template.html')



def screenshot(urls, local=True):
    driver = webdriver.Firefox()
    for url in urls:
        if local: 
            full_path = os.path.join(os.getcwd(),f'{url}\\index.html')
            ss_path = os.path.join(os.getcwd(),f'images')
            #import pdb
            #pdb.set_trace()
    
        print(f'Opening url: {full_path}')
        driver.get(full_path)
        sleep(1)
    
        driver.get_screenshot_as_file(f'{ss_path}\\{url}.png')
        
        print(f'Saved screenshot as {ss_path}\\{url}.png')

    driver.quit()


def write(content, filename='index.html'):
	with open(filename, 'w') as f:
		f.write(content)
		print(f'Finished writing to {filename}')


dirs = [d for d in os.listdir('.') if not os.path.isfile(d)]
remove = ['.git','.venv','assets','images','templates']
for r in remove: dirs.remove(r)

print(f'Found {len(dirs)} directories.\n{dirs}')

html = template.render({'dirs':dirs})
write(html)
print('Done')

choice = input('Create images?')
if choice.lower() == 'y':
    screenshot(dirs)
print('Finished')