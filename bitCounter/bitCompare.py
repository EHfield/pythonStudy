import pandas as pd


def bitCounter(x1):
    count = 0
    for i in range(0, 32):
        count += (x1 >> i) & 1
        # print('i:' + str(i) + 'count: '+ str(count)) # for Debugg
    return count

def bitCmp(x1, x2):
    return bitCounter((x1^x2))


opFileName = 'C:\\Users\\tzin\\Documents\\Python\\csv\\qlc_param_prog_chipNo062.txt'
csv_test = pd.read_csv(opFileName,dtype=object)
print(csv_test) # check 용도
opFileName = 'C:\\Users\\tzin\\Documents\\Python\\csv\\qlc_org.txt'
csv_org = pd.read_csv(opFileName,dtype=object)
print(csv_org) # check 용도

row = len(csv_test.index)
column = len(csv_test.columns)
print(row)
print(column)
# print(int(csv_test.iloc[0, 1], 16))
print(csv_test.iloc[0, 543])

bitDiff = []

for i in range(0, len(csv_test.index)):
    temp = []
    for j in range(0, len(csv_test.columns)):
        try :
            temp.append(bitCmp(int(csv_test.iloc[i, j],16), int(csv_org.iloc[i, j], 16)))
        except:
            print("error!!!! ", i, ", ",j)
        
    print(temp)
    bitDiff.append(temp)
    
    
# print(bitDiff)