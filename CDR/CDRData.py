# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
from functions import *

class CDRData():
    def __init__(self,inDirPath=None,inFilePath=None):
        self.inDirPath = inDirPath
        self.inFilePath = inFilePath
        self.data = None
        self.days = None
        self.prefix = None
        self.headers = None
        self.sampleFilter = False
    def setFilter(self):
        self.sampleFilter = True
        self.filterBySampleUsers()

    def setMultipleDays(self,prefix,days):
        self.prefix = prefix
        self.days = days

    def setHeaders(self,headers):
        self.headers = headers

    def readMultipleDays(self):
#        self.data = pd.DataFrame()
        result = []
        for day in self.days:
            print(day)
            dateStr = str(day)
            if day < 10: dateStr = "0{}".format(day)
            dateDirName = self.prefix+dateStr
            self.inFilePath = os.path.join(self.inDirPath,dateDirName)
            self.readOneDayFile()
            self.data['date'] = [dateDirName] * len(self.data)
            result.append(self.data)
        self.data = pd.concat(result)

    def readData(self):
        if not self.inFilePath is None:
            self.readOneDayFile()
        elif not self.days is None:
            self.readMultipleDays()
        elif not self.inDirPath is None:
            self.readOneDir()

    def readCSV(self,filepath):
        result = pd.read_csv(filepath,compression='gzip',names= self.headers)
        if self.sampleFilter:
            result = result.join(self.samples.set_index("user id"),on='user id',how='inner')
        self.data = result
        return(result)

    def readOneDayFile(self):
        if self.inFilePath is None: return
        filenames = os.listdir(self.inFilePath)
        result = []
        for filename in filenames:
            if filename in ['_logs','_SUCCESS','_SUCCESS.gz']: continue
            filepath = os.path.join(self.inFilePath,filename)
            onedata = self.readCSV(filepath)
            result.append(onedata)
        self.data = pd.concat(result)

    def readOneDir(self):
        if self.inDirPath is None: return
        dirnames = os.listdir(self.inDirPath)
        for dirname in dirnames:
            pass

    def sampleUsers(self,n,outFile):
        users = self.data['user id'].unique()
        r = np.random.choice(len(users),size=n,replace=False)
        result = [users[ii] for ii in r]
        samples = pd.DataFrame({'user id':result})
        samples.to_csv(outFile,index=False)

    def filterBySampleUsers(self):
        self.samples = pd.read_csv("/common/users/zf72/SignalSense/csv/tele-sample-users-10000.csv")


    def countNewLocations(self,targetDays):
        days = []
        for one in targetDays:
            dateStr = str(one)
            if one < 10: dateStr = "0{}".format(one)
            days.append(self.prefix + dateStr)
        res = self.data.groupby('user id').apply(lambda x: countLocationsInNewDay(x,days))
        res = res.reset_index(name='count')
        return(res)


#cdrDirPath = "/common/users/zf72/RawData/cdr"
#
#for ii in range(1,15):
#    dateStr = ii
#    if ii < 10: dateStr = "0{}".format(ii)
#    fileName = "2013-08-{}".format(dateStr)
#    filepath = os.path.join(cdrDirPath,fileName)
#    data = pd.read_csv(filepath)
#


#%%
