import glob
import os

for file in glob.glob('data/MidiMadagasikara/*'):
    title = file.split('.')[-2]
    hit = 0
    with open(file, 'r') as f:
        content = f.read()

        for char in 'cquwx':
            if char in title:
                hit += 1
            if char in content:
                hit += 1

    if hit > 5:
        print(hit, file)
        os.remove(file)