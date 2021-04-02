pre = """
<html>

<ul>
"""

post = """
</ul>
</html>
"""
import os

DEBUG = False
if DEBUG:
	from varinfo import *



def create_html(dirs):
	html = ''
	for d in dirs:
		html += f'\t<li><a href="{d}/"><h1>{d}</h1></a></li>\n'
	return html

def write(content, filename='index.html'):
	with open(filename, 'w') as f:
		f.write(pre)
		f.write(content)
		f.write(post)
		print(f'Finished writing to {filename}')

dirs = [d for d in os.listdir('.') if not os.path.isfile(d)]
dirs.remove('.git')
choice = input(f'Found {len(dirs)} directories: {dirs}\nContinue?(Y/n)')
if choice.lower != 'n':
	html = create_html(dirs)
	write(html)
print('Exiting')