#python code goes here
#python version :3 
import xlrd
def main():
    workbook=xlrd.open_workbook("sample.xlsx")
    sheet=workbook.sheet_by_index(0)
    total_list=[[sheet.cell_value(row,col) for col in range(sheet.ncols)] for row in range(sheet.nrows)]
    print(total_list)
    print(sheet.nrows)
    print(sheet.ncols)
    print(total_list[1])
    total_list.append(['aaa','mech','aaa@gmail.com','9874563210','N'])
    print(total_list)
    print(len(total_list))
if __name__=='__main__':
    main()
