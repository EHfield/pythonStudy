import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl

opFileName = 'marginRead.txt'
csvDF = pd.read_csv(opFileName,dtype=object)

print(csvDF)

def bitCounter(x1):
    count = 0
    for i in range(0, 32):
        count += (x1 >> i) & 1
        # print('i:' + str(i) + 'count: '+ str(count)) # for Debugg
    return count


addr = int('0x00400000', 16)+0
# format(addr,'08x') # 0x 문구가 붙지 않고 string으로 나온다.
# print(hex(addr)) # 0x 문구가 붙는다. 앞에 빈자리 없음. hex()에서 argument를 넣어야 할 듯하다
print(csvDF.loc[17, format(addr, '08x')])

value = int(str(csvDF.loc[17, format(addr, '08X')]), 16) # 0x0000000의 경우 자동으로 숫자 0으로(int형으로) 인지해서 강제로 string 형변환하였다.
print(value)

print('bit of value',value,'(',hex(value),')',': ',bitCounter(value))

bitList=[]
vrdList=[]
for i in range(0,51):
    bitSum = 0
    for addr in range(int(str('00400000'),16), int(str('00400040'),16), 4): #string 문자열의 숫자가 16진수(40000)인지, 10진수(40000)인지를 명확히 하기 위해 int 함수의 2nd argm 에는 16이 필요하다.
        value = int(csvDF.loc[i, format(addr,'08X')],16)
        # print(value) # code Test
        bitSum+=bitCounter(value)
        # print('bitSum: ',bitSum) # code Test
    vrdList.append(i*50)
    bitList.append(bitSum)

print('bitList[]',bitList)
print('vrdList[]',vrdList)

pltX=[]
pltY=[]

for i in range(0,len(bitList)-1):
    # print(i,':',bitList[i])
    pltY.append(bitList[i+1]-bitList[i])
    pltX.append(vrdList[i]+(vrdList[i+1]-vrdList[i])/2)
    # print('bit',bitList[i+1]-bitList[i])
    # print('vrd',(vrdList[i]+vrdList[i+1]-vrdList[i])/2)
    

print('pltY',pltY,'pltX',pltX)

mpl.clf() # plot clear
mpl.plot(pltX, pltY)
mpl.scatter(pltX, pltY, c='blue', edgecolor='red',s=50)
mpl.title('Margin Read (virgin @ #21)')
mpl.xlabel('Threshold Voltage[mV]')
mpl.ylabel('Number of Bit Cells')
mpl.xlim([0,2500])
mpl.ylim([0,100])
mpl.xticks(np.arange(0,2501,250))
mpl.savefig(opFileName.replace('.txt','.png'))
mpl.show()