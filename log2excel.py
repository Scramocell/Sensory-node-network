import xlwt

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Sheet_1')

with open('teraterm.txt', 'r') as myfile:
    row = 0
    plots = []
    while True:
        newdata = myfile.read().split('\n')
        data = newdata[:-1]
        currentLength = len(data)
        
        if currentLength > 0:
            for x in range(currentLength):
                print(data[x][6:])
                row = row + 1
                sheet.write(row, 0, int(data[x][6:]))
            
            print('-----------------------------------------------')

        workbook.save('teraterm.xls')
