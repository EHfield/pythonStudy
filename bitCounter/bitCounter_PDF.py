import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl

# Function bit Counter
def bitCounter(x1):
    count = 0
    for i in range(0, 32):
        count += (x1 >> i) & 1
        # print('i:' + str(i) + 'count: '+ str(count)) # for Debugg
    return count
rowNum=0

totalbitList = [0 for i in range(34)] # bits counter for All row
figName = 'C:\\Users\\tzin\\Documents\\Python\\qlc_test\\chipNo061_2WL_2kb.png'

opFileName = 'C:\\Users\\tzin\\Documents\\Python\\csv\\QLC_smallVRF_WL0_8Bank.csv'
csvDF = pd.read_csv(opFileName,dtype=object)
print(csvDF) # check 용도


rowNum = len(csvDF.index)
ColumnNum = len(csvDF.columns)
''' Check '''
# print(row)
# print(ColumnNum)
# print(csvDF.iloc[6, 3])
''' Check '''

bitList=[]
vrdList=[]
stepVrd = 50

for i in range(0, rowNum):
    bitSum = 0
    for j in range(1, ColumnNum):
        value = int(csvDF.iloc[i, j], 16)
        bitSum+=bitCounter(value)
    
    vrdList.append(i*stepVrd)
    bitList.append(bitSum)

print(vrdList)
print(bitList)

mpl.clf() # plot clear
mpl.plot(vrdList, bitList)
mpl.show()

bitDiff = []
bitDiff.append(0)
for i in range(0, len(vrdList)-1):
    bitDiff.append(bitList[i+1] - bitList[i])
print(bitDiff)

mpl.clf() # plot clear
mpl.plot(vrdList, bitDiff)
mpl.show()

'''

while rowNum<128:
    addr = int('0x00400000', 16)+rowNum*128
    # format(addr,'08x') # 0x 문구가 붙지 않고 string으로 나온다.
    # print(hex(addr)) # 0x 문구가 붙는다. 앞에 빈자리 없음. hex()에서 argument를 넣어야 할 듯하다
    # print(csvDF.loc[17, format(addr, '08x')]) # for debug

    # value = int(str(csvDF.loc[17, format(addr, '08X')]), 16) # 0x0000000의 경우 자동으로 숫자 0으로(int형으로) 인지해서 강제로 string 형변환하였다.
    # print(value) # for debug

    # print('bit of value',value,'(',hex(value),')',': ',bitCounter(value)) # for debug

    bitList=[]
    vrdList=[]
    for i in range(0,34):
        bitSum = 0
        for addr in range(int(str('00400000'),16)+rowNum*128, int(str('00400080'),16)+rowNum*128, 4): #string 문자열의 숫자가 16진수(40000)인지, 10진수(40000)인지를 명확히 하기 위해 int 함수의 2nd argm 에는 16이 필요하다.
            value = int(csvDF.loc[i, format(addr,'08X')],16)
            # print(value) # code Test
            bitSum+=bitCounter(value)
            # print('bitSum: ',bitSum) # code Test
        vrdList.append(i*100)
        bitList.append(bitSum)
    print('bitList[]',bitList)
    # print('vrdList[]',vrdList)
    # print('totalbitList[]',totalbitList)
    totalbitList = [totalbitList[i] + bitList[i] for i in range(len(bitList))]
    print(rowNum,' completed')
    pltX=[]
    pltY=[]
            ### margin read 그래프 그리기용
    for i in range(0,len(bitList)):
        # print(i,':',bitList[i])
        pltY.append(bitList[i])
        pltX.append(vrdList[i])
    ### margin read 그래프 그리기용
    # print('pltY',pltY,'pltX',pltX)
    mpl.clf() # plot clear
    mpl.plot(pltX, pltY)
    # mpl.scatter(pltX, pltY, c='blue', edgecolor='red',s=50)
    mpl.title('Margin Read @ chip No. 170 WL'+ str(rowNum))
    mpl.xlabel('Threshold Voltage[mV]')
    mpl.ylabel('Number of Bit Cells')
    mpl.xlim([0,3300])
    mpl.ylim([0,1025])
    mpl.xticks(np.arange(0,3301,300))
    mpl.yticks(np.arange(0,1025,50))
    mpl.savefig(opFileName.replace('.txt','.png'))
    # mpl.show()
    rowNum+=1
    # print(rowNum,' completed')
    ### margin read 그래프 그리기용
    
    
    
### total bit word line margin 그래프
print(totalbitList)
pltX=[]
pltY=[]
for i in range(0,len(totalbitList)):
    # print(i,':',bitList[i])
    pltY.append(totalbitList[i])
    pltX.append(vrdList[i])
    # print('bit',bitList[i+1]-bitList[i])
    # print('vrd',(vrdList[i]+vrdList[i+1]-vrdList[i])/2)
### margin read 그래프 그리기용
# print('pltY',pltY,'pltX',pltX)
mpl.figure(figsize=(8,5))
mpl.plot(pltX, pltY)
# mpl.scatter(pltX, pltY, c='blue', edgecolor='red',s=50)
mpl.title('Margin Read (Chip No. 170, Ext_VSREF:200mV, 1MHz)')
mpl.xlabel('Threshold Voltage[mV]',labelpad=5.0)
mpl.ylabel('Number of Bit Cells\n(max. 131,072b)')
mpl.xlim([0,3300])
mpl.ylim([0,132000])
mpl.xticks(np.arange(0,3301,300))
mpl.yticks(np.arange(0,132000,10000))
mpl.savefig(figName)
# mpl.show()

    
    
    
    ### total bit word line margin 그래프
    
    
    
    ### diff 그래프 그리기용
    # for i in range(0,len(bitList)-1):
    #     # print(i,':',bitList[i])
    #     pltY.append(bitList[i+1]-bitList[i])                  # diff 그래프 그리기용 데이터 삽입
    #     pltX.append(vrdList[i]+(vrdList[i+1]-vrdList[i])/2)   # diff 그래프 그리기용 데이터 삽입
    #     # print('bit',bitList[i+1]-bitList[i])
    #     # print('vrd',(vrdList[i]+vrdList[i+1]-vrdList[i])/2)
    ### diff 그래프 그리기용



'''

### 그림 그리기용
'''
fileNum1 = 40
fileNum2 = 720
fileNum3 = 1100

while fileNum1 <=500:
    fileNum2 = 720
    while fileNum2 <=880:
        fileNum3 = 1100
        while fileNum3 <= 1220:
            opFileName = 'C:\\Users\\tzin\\Documents\\Python\\eflash_5MHz_sweep\\vsref ' + str(fileNum1) + '\\vpp4_' + str(fileNum2)+'\\set vpp1 ' + str(fileNum3) + '.txt'
            csvDF = pd.read_csv(opFileName,dtype=object)
            # print(csvDF) # check 용도

            addr = int('0x00400000', 16)+0
            # format(addr,'08x') # 0x 문구가 붙지 않고 string으로 나온다.
            # print(hex(addr)) # 0x 문구가 붙는다. 앞에 빈자리 없음. hex()에서 argument를 넣어야 할 듯하다
            # print(csvDF.loc[17, format(addr, '08x')]) # for debug

            value = int(str(csvDF.loc[17, format(addr, '08X')]), 16) # 0x0000000의 경우 자동으로 숫자 0으로(int형으로) 인지해서 강제로 string 형변환하였다.
            # print(value) # for debug

            # print('bit of value',value,'(',hex(value),')',': ',bitCounter(value)) # for debug

            bitList=[]
            vrdList=[]
            for i in range(0,34):
                bitSum = 0
                for addr in range(int(str('00400000'),16), int(str('0040001C'),16), 4): #string 문자열의 숫자가 16진수(40000)인지, 10진수(40000)인지를 명확히 하기 위해 int 함수의 2nd argm 에는 16이 필요하다.
                    value = int(csvDF.loc[i, format(addr,'08X')],16)
                    # print(value) # code Test
                    bitSum+=bitCounter(value)
                    # print('bitSum: ',bitSum) # code Test
                vrdList.append(i*100)
                bitList.append(bitSum)

            # print('bitList[]',bitList)
            # print('vrdList[]',vrdList)

            pltX=[]
            pltY=[]

            
            # diff 그래프 그리기용
            # for i in range(0,len(bitList)-1):
            #     # print(i,':',bitList[i])
            #     pltY.append(bitList[i+1]-bitList[i])                  # diff 그래프 그리기용 데이터 삽입
            #     pltX.append(vrdList[i]+(vrdList[i+1]-vrdList[i])/2)   # diff 그래프 그리기용 데이터 삽입
            #     # print('bit',bitList[i+1]-bitList[i])
            #     # print('vrd',(vrdList[i]+vrdList[i+1]-vrdList[i])/2)
            # diff 그래프 그리기용
            

            ### 그래프 그리기용
            for i in range(0,len(bitList)):
                # print(i,':',bitList[i])
                pltY.append(bitList[i])
                pltX.append(vrdList[i])
                # print('bit',bitList[i+1]-bitList[i])
                # print('vrd',(vrdList[i]+vrdList[i+1]-vrdList[i])/2)
            ### 그래프 그리기용

            print('pltY',pltY,'pltX',pltX)

            mpl.clf() # plot clear
            mpl.plot(pltX, pltY)
            # mpl.scatter(pltX, pltY, c='blue', edgecolor='red',s=50)
            mpl.title('Margin Read')
            mpl.xlabel('Threshold Voltage[mV]')
            mpl.ylabel('Number of Bit Cells')
            mpl.xlim([0,3300])
            mpl.ylim([0,300])
            mpl.xticks(np.arange(0,3301,300))
            mpl.savefig(opFileName.replace('.txt','.png'))
            # mpl.show()
            
            fileNum3+=20
        fileNum2+=20
    fileNum1+=20
    
    
'''