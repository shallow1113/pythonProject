import yaml

def read_yaml1():
    with open('../data/token.yaml', encoding='utf-8', mode='r')as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        print(value)
        return value
def read_yaml2():
    with open('../data/hys.yaml', encoding='utf-8', mode='r')as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        print(value)
        return value





if __name__ == '__main__':
    read_yaml1()
    read_yaml2()



