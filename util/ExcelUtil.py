#coding=utf-8
__author__ = 'lgx'

import xlrd

def readExcel():
    excel = xlrd.open_workbook('C:/Users/pc/Desktop/test.xls')
    sheet = excel.sheets()[0]
    rows = sheet.nrows
    cols = sheet.ncols
    print([sheet.row_values(index) for index in range(1,rows)])

if __name__ == '__main__':
    readExcel()