#! /opt/homebrew/bin/python3
"""
Date: 2024-02-22
"""
import argparse

# 옵션 설정 --------------------- START
def get_args():
    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
    return parser.parse_args()
# 옵션 설정 --------------------- END
    
def main():
    args = get_args()
    print('Hello, ' + args.name + '!')
    
if __name__ == '__main__':
    main()