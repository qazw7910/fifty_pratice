#https://www.flag.com.tw/Redirect/F1750/22
import csv
'''def passwd_to_csv(filename):
    with open(filename,'r') as f:
        csv_reader = csv.reader(f, delimiter = ',')
        for line in csv_reader:
            print(line)
if __name__ == '__main__':
    passwd_to_csv('document/contacts-sample.csv')'''

'''with open('document/contacts-sample.csv','w') as f:
    csv_writer = csv.writer(f, delimiter = '\t')
    for line in data:
        csv_writer.writerow(line)'''

data = [
['First Name', 'Last Name', 'Full Name', 'Title', 'Company', 'Department', 'Job Title', 'Primary Email', 'Business Fax', 'Business Phone', 'Home Phone', 'Mobile Phone', 'Groups'],
['娜美', '蒙奇第', '蒙奇第', '先生', '海賊王工作室', '動畫組', '船長', 'ruffy@onepiece.com', '855 566 677', '888 888 888', '999 999 999', '0988 888 888', '演員'],
['索龍', '娜美', '娜美', '先生', '海賊王工作室', '動畫組', '副船長', 'zoro@onepiece.com', '856 566 677', '777 777 777', '121 232 343', '0988 777 777', '演員'],
['娜美', '娜美', '娜美', '先生', '海賊王工作室', '動畫組', '廚師', 'sunkys@onepiece.com', '857 566 677', '666 666 666', '', '0988 666 666', '演員'],
['娜美', '香吉士', '香吉士', '小姐', '海賊王工作室', '動畫組', '航海士', 'nomy@onepiece.com', '858 566 677', '555 555 555', '', '0988 555 555', '演員']
]


with open('document/contacts-sample.csv', 'w') as f:
    csv_writer = csv.writer(f, delimiter = '\t', lineterminator = '\n')
    csv_writer.writerows(data)