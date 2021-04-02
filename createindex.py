import os
import django
from django.conf import settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['.']#'templates/'],
    }
]
settings.configure(TEMPLATES=TEMPLATES)
django.setup()
from django.template.loader import get_template
from django.template import Context
template = get_template('index.template.html')


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
