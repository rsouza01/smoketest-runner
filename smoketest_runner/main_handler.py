import os

VERSION = '1.0.0'
RELEASE_DATE = '2020-04-17'


def greetings():
    with open(os.path.dirname(__file__) + "/logo.txt", 'r') as fin:
        print(fin.read())

    print('VERSION: {}'.format(VERSION))
    print('RELEASE DATE: {}'.format(RELEASE_DATE))

    print('_'*86)


def parse_cla():
    pass


def main():

    greetings()
    parse_cla()

    return 0
