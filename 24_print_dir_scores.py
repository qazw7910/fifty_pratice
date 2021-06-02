#https://www.flag.com.tw/Redirect/F1750/24
import os
import json
from collections import defaultdict

def print_score(filename):
    with open(filename,'r') as json_file:
        record = json.load(json_file)
        result = defaultdict(list)

        print('班級:',record['class'])
        for record in record['score']:
            for subject, score in record.items():
                result[subject].append(score)

        for subject, score in result.items():
            print('科目:',subject)
            print('\t最高:',max(score))
            print('\t最低:',min(score))
            print('\t平均:',sum(score)/len(score))

def print_dir_scores(dirname):
    for filename in os.listdir(dirname):
        if filename.endswith('.json'):
            print('讀取檔案:', filename)
            print_score(os.path.join(dirname, filename))

if __name__ == '__main__':
    #print_dir_scores('document')
    print_score('document/9a.json')




#print(os.listdir(r'document'))
'''for filename in os.listdir(r'document'):
    if filename.endswith('.json'):
        print(filename)'''

'''for filename in os.listdir(r'document'):
    if filename.endswith('json'):
        print(os.path.join(r'document',filename))'''

