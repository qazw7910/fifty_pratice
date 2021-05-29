#https://www.flag.com.tw/Redirect/F1750/18
'''
f = open(r'document/login_log','r') # open file, set read (r, read)mode
for line in f.readlines():          # readline() vs readlines() have different
    print(line)
readlines()方法讀取整個檔案所有行，儲存在一個列表(list)變數中，每行作為一個元素，但讀取大檔案會比較佔記憶體。
readline()方法從字面意思可以看出，該方法每次讀出一行內容，所以，讀取時佔用記憶體小，比較適合大檔案，該方法返回一個字串物件。
'''
####################################
'''
f = open(r'document/login_log', 'r')

while True:
    line = f.readline()
    if not line:
        break
    lastline = line
f.close()
print(lastline)
'''
####################################
'''open() 支援走訪協定
f = open(r'document/login_log','r')

for line in f:
    lastline = line

print(lastline)
'''
####################################
'''
def read_final_line(filename):
    f = open(filename,'r')
    for line in f:
        pass    #不做任何事

    f.close()
    return line
if __name__ == '__main__':
    print(read_final_line(r'document/login_log'))
'''
###################################
'''
def read_final_line(filename):
    f = open(filename, 'r')
    try:
        for line in f:
            print(line)
    finally:
        f.close()

if __name__ == '__main__':
    print(read_final_line(r'document/login_log'))
'''
###################################
#with用完直接關掉，省略掉f.close
'''
def read_final_line(filename):
    with open(filename,'r') as f:
        for line in f:
            print(line)

if __name__ == '__main__':
    print(read_final_line(r'document/login_log'))
'''
###################################
def read_final_line(filename):
    with open(filename,'r') as f:
        for line in f:
            pass
        return line

if __name__ == '__main__':
    print(read_final_line(r'document/login_log'))


















