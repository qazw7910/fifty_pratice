with open(f'document/password.cfg','r') as f:

    print({word[0]:word[2]
           for word
           in [line.split(':') for line in f]})