import urllib.request
import math, csv
def main():
    
    stock1 = input("Please provide the ticker of any stock: ")
    stock2 = input("Please provide the ticker of another stock: ")
    print("requesting " + 'http://ichart.yahoo.com/table.csv?s=%s'%stock1)
    url1 = 'http://ichart.yahoo.com/table.csv?s=%s'%stock1
    response1 = urllib.request.urlopen(url1)
    print("requesting " + 'http://ichart.yahoo.com/table.csv?s=%s'%stock2)      
    url2 = 'http://ichart.yahoo.com/table.csv?s=%s'%stock2
    response2 = urllib.request.urlopen(url2)
    stock_data1 = response1.readlines()
    stock_data2 = response2.readlines()
    date_list1 = []
    open_list1 = []#remove date_list2
    open_list2 = []
    for i in range(1,31):
        list_of_rows1 = stock_data1[i].decode("utf-8").split(',')
        date_list1.append(list_of_rows1[0])
        open_list1.append(list_of_rows1[1])
        list_of_rows2 = stock_data2[i].decode("utf-8").split(',')
        open_list2.append(list_of_rows2[1])
    new_file_name = stock1 + stock2 + date_list1[0] + ".csv"
    with open(new_file_name, 'w') as csvfile:
        stock_writer = csv.writer(csvfile,delimiter = ",")
        row1 = ['date',stock1,stock2]
        stock_writer.writerow(row1)
        for i in range(len(open_list1)):
            other_row = [date_list1[i],open_list1[i],open_list2[i]]
            stock_writer.writerow(other_row)
        print("Check for new CVS file in the current directory")

main()
