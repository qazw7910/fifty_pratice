import pathlib
import os
from collections import defaultdict
import json

def print_scores(filename):
    with open(filename,'r') as json_file:
        record = json.load(json_file)#loads vs load
        result = defaultdict(list)

        print('班級: ', record['class'])
        for record in record['score']:
            for subject, score in record.items():
                result[subject].append(score)

        for subject, score in result.items():
            print('科目:', subject)
            print('\t最高:', max(score))
            print('\t最低:', min(score))
            print('\t平均:', sum(score)/len(score))

def print_dir_score(dirname):
    p = pathlib.Path(dirname)
    for filename in p.iterdir():
        if filename.suffix == '.json':
            print('讀取檔案', filename)
            print_scores(filename)

'''def print_dir_score(dirname):
    for filename in os.listdir(dirname):
        if filename.endswith('.json'):
            print('讀取檔案', filename)
        print_scores(os.path.join(dirname, filename))'''

if __name__ == '__main__':
    print_dir_score(r'document')