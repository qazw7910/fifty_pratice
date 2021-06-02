#https://www.flag.com.tw/Redirect/F1750/23
#https://ithelp.ithome.com.tw/articles/10193094     defaultdict()介紹
import json
from collections import defaultdict

def print_score(filename):
    with open(filename, 'r') as json_file:
        record = json.load(json_file)
        result = defaultdict(list)  #use default to call null list to append()

        print('班級:', record['class'])
        for record in record['score']:
            for subject, record in record.items():
                result[subject].append(record)

        for subject, score in result.items():
            print('科目:', subject)
            print('\t最高分:', max(score))
            print('\t最低分:', min(score))
            print('\t平均分:', sum(score)/len(score))

if __name__ == '__main__':
    print_score('document/9a')




















#json.loads()讀取一串json資料時用的
'''json_str = '{"math": 90, "literacture": 98, "science": 97}'

json_obj = json.loads(json_str)

print(json_obj)
print(type(json_obj))'''

#json.load()讀取json檔案時用的
'''with open('document/9a','r') as json_file:
    print(json.load(json_file))'''

