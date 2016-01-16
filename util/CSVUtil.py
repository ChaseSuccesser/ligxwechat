#coding=utf-8
__author__ = 'lgx'

import csv

def readCSV():
    with open('C:/Users/pc/Desktop/sqlResult_358972.csv', encoding='utf-8') as f:
        f_csv = csv.DictReader(f)
        index = 0


        first_row = f_csv.__iter__().__next__()
        for key in first_row:
            print(key.encode('utf-8'), end='\t')

        for row in f_csv:
            index += 1
            if index == 10:
                break
            for key,value in row.items():
                print(value, end='\t')
            print()

if __name__ == '__main__':
    readCSV()

