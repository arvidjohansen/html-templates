from zipfile import ZipFile
import os

dirs = os.listdir()
dirs = [d for d in dirs if d.endswith('.zip')]
print(dirs)

for d in dirs:
    tdir = f'html5up-{d[:-4].lower()}'
    if os.path.exists(tdir):
        print(f'{tdir} exists, skipping..')
        continue
    with ZipFile(d, 'r') as zip:
        # Extract all the contents of zip file in current directory
        zip.extractall(tdir)
        print(f'Unzipped {d} to {tdir}')