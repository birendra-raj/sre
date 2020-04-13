#import openpyxl
import xlrd
from builtins import range
#loc="D:\Selenium_with_python\PLearn\Lesson\biru.xls"
my_wb= xlrd.open_workbook('biru.xls')
sheet=my_wb.sheet_by_index(0)
print(sheet.cell_value(1,1))
print(sheet.nrows)
print(sheet.ncols)

for i in range(0,sheet.ncols):
    print(sheet.cell_value(0,i))
print(sheet.row_values(1))
print(sheet.col_values(1))