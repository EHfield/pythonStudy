import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl

progVoltage = [100, 350, 500, 700, 850, 1050, 1200, 1350, 1500, 1650, 1750, 1950, 2150, 2300, 2450, 2500]
stateSum = []
opFileName = 'C:\\Users\\tzin\\Documents\\Python\\csv\\qlc_stand_prog_chipNo062_bank0.txt'
csvDF = pd.read_csv(opFileName,dtype=object)
print(csvDF)

startRow = 0
endRow = 0
progVNum = 0

def rangeSumDF(dataFrame, startP, endP):
    if endP > len(csvDF.index):
        endP = csvDF.index
    
    temp = [0 for i in range(15)]
    for row in range(startP, endP):
        for column in range(0, len(dataFrame.columns)):
            temp[column] += int(dataFrame.iloc[row, column])
    # print(temp)


for vrd in range(0, len(csvDF.index)):
    if (int(csvDF.index[vrd]) == progVoltage[progVNum]): 
        print("start Row", startRow, "endRow", vrd)
        rangeSumDF(csvDF, startRow, vrd)
        startRow = vrd
        progVNum = progVNum + 1
        if(progVNum == len(progVoltage)):
            progVNum = len(progVoltage) -1
    
    
