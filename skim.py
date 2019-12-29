import glob
import os

def skim():
    fr = set()
    with open('frwords.txt','r') as f:
        for i in f.readlines():
            s = i.strip('\n')
            if len(s) > 1:
                fr.add(s)

    titles = []
    for file in glob.glob('data/*/*'):
        title = file.split('.')[-2]
        hit = 0
        with open(file, 'r') as f:
            content = f.read()

            for char in 'cquwxèé':
                if char in title:
                    hit += 1
                if char in content:
                    hit += 1
            for w in fr:
                if ' '+w+' ' in content:
                    hit += 1
                if '"'+w+' ' in content:
                    hit += 1
                if ' '+w+'"' in content:
                    hit += 1
                if ' '+w+'.' in content:
                    hit += 1


        if hit > 44:
            #print(hit, file)
            titles.append((hit, file))

    titles.sort()
    for t1,file in titles:
        print(file)
        os.remove(file)

if __name__ == '__main__':
    skim()