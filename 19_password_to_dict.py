#https://www.flag.com.tw/Redirect/F1750/19
def password_to_dict(filename):
    user = {}
    with open(filename) as f:
        for line in f :
            user_info = line.split(':')
            user.update({user_info[0] : user_info[2]})
    return user

if __name__ == '__main__':
    print(password_to_dict(r'document/password.cfg'))