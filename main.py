# 매장 정보 메모 프로그램 v0.2
# Author : Hyuntek Lim

import pandas as pd
import numpy as np
import os
import tkinter as tk
from datetime import datetime


#global variables

workingPath = 'C:\\automation\data'

#functions

def workspace(dirPath):
    try:
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)

        os.chdir(dirPath)

    except OSError:
        print('Error : 저장 디렉토리를 찾을 수 없습니다.')

def dataWrite(csvName,callNum,carNum,memo):
    # csv파일이 존재하면 데이터를 추가하고 존재하지 않으면 생성합니다.
    data = pd.DataFrame([(callNum, carNum, datetime.today().strftime("%Y-%m-%d"), memo)], columns = ['전화번호', '차량번호', '기입날짜', '처리내용'])
    if not os.path.exists(csvName):
        data.to_csv(csvName, index=False, mode='w', encoding='utf-8-sig')
    else:
        data.to_csv(csvName, index=False, mode='a', encoding='utf-8-sig', header=False)

def dataRead(csvName,query):
    try:
        data = pd.read_csv(csvName, header='infer', encoding= 'utf-8-sig')
        return data.query(query)
    except:
        print('Error : 데이터를 읽어올 수 없습니다.')

def createWriteFrame():
    WriteFrame = tk.Toplevel(mainFrame)

def createReadFrame():
    ReadFrame = tk.Toplevel(mainFrame)


#system initiation
workspace(workingPath)
mainFrame = tk.Tk()
mainFrame.title("매장 정보 메모 프로그램")
mainFrame.geometry("260x240+100+100")


#GUI initiation
label = tk.Label(mainFrame, text='매장 정보 메모 프로그램', font='21').pack(pady=5)
Write = tk.Button(mainFrame, text='메모 추가', width=10, height= 3).pack(pady=10)
Read = tk.Button(mainFrame, text='자료 조회', width=10, height= 3).pack(pady=10)

mainFrame.mainloop()



#sample code

#dataWrite('sample.csv', '010-5061-5917', '5354', '한글이 깨질까? 아님 안깨질까?' )

print(pd.read_csv('sample.csv'))
