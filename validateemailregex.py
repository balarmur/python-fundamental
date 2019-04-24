import os
import re
import numpy as np
import pandas as pd


def setWorkDirectory():
    os.chdir('C:/Users/bala0/OneDrive/My_Mine/My_Study/My_Python/My_Codes/Fundamentals')
    print('\nWorking in the directory: ', os.getcwd())

def readInputFile():
    global totemail, inpfil

    nalist = ['N/A', 'NA', 'n/a', 'na']
    inpfil = pd.read_csv('htmlconv1.csv', na_values=nalist)
    totemail = len(inpfil['Email'])

def printInputFile():
    for i in range(totemail):
        print('The received email is: ', inpfil['Email'][i])

def fillNullEmail():
    inpfil['Email'].fillna('sample@test.com',inplace=True)

def verifyEmail(email):
    vemail=bool(re.findall(r'[a-zA-Z0-9]@[a-zA-Z].[a-z]', email))
    if vemail:
        lstemail.append(str(inpfil['Email'][rec]).lower())
    else:
        lstemail.append('sample@test.com')


def writeOutFile():
    inpfil.to_csv('htmlconv2.csv', index=False)

def mainFunc():
    global rec, lstemail
    lstemail=[]
    setWorkDirectory()
    readInputFile()
    fillNullEmail()
    for rec in range(totemail):
        verifyEmail(inpfil['Email'][rec])

    inpfil['Email'] = lstemail

    #printInputFile()
    writeOutFile()

if __name__ == "__main__":
    mainFunc()
