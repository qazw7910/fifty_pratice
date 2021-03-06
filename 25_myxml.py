#https://www.flag.com.tw/Redirect/F1750/25
def myxml(tag, content='', **kwargs):
    attrs_list = []
    for key, value in kwargs.items():
        attrs_list.append(f' {key} = "{value}"')

    attrs = ''.join(attrs_list)

    return f'<{tag}{attrs}>{content}</{tag}>'


if __name__ == '__main__':
    print(myxml('foo', 'bar', a=1, b=2, c=3))