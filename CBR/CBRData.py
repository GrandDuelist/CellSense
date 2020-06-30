# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np

class CBRData():
    def __init__(self, inDirPath=None, inFilePath=None):
        self.inDirPath = inDirPath
        self.inFilePath = inFilePath
        self.data = None
        self.days = None
        self.prefix = None
        self.headers = None
        self.sampleFilter = False
        self.columns = None

    def setFilter(self):
        self.sampleFilter = True
        self.filterBySampleUsers()

    def setColumns(self,cols):
        self.columns = cols

    def setMultipleDays(self, prefix, days):
        self.prefix = prefix
        self.days = days

    def setHeaders(self, headers):
        self.headers = headers

    def readMultipleDays(self):
        #        self.data = pd.DataFrame()
        result = []
        for day in self.days:
            print(day)
            dateStr = str(day)
            if day < 10: dateStr = "0{}".format(day)
            dateDirName = self.prefix + dateStr
            self.inFilePath = os.path.join(self.inDirPath, dateDirName)
            self.readOneDayFile()
            self.data['date'] = [dateDirName] * len(self.data)
            result.append(self.data)
        self.data = pd.concat(result)
        del result

    def readData(self):
        if not self.inFilePath is None:
            self.readOneDayFile()
        elif not self.days is None:
            self.readMultipleDays()
        elif not self.inDirPath is None:
            self.readOneDir()

    def readCSV(self, filepath):
        print(filepath)
        result = pd.read_csv(filepath, names=self.headers)
        if self.sampleFilter:
            result = result.join(self.samples.set_index("user id"), on='user id', how='inner')
        if self.columns:
            result = result[self.columns]
        self.data = result
        return (result)

    def sampleTowers(self):
        pass
    def readOneDayFile(self):
        if self.inFilePath is None: return
        filenames = os.listdir(self.inFilePath)
        result = []
        for filename in filenames:
            if filename in ['_logs', '_SUCCESS', '_SUCCESS.gz'] or filename.split('.')[-1]=='crc': continue
            filepath = os.path.join(self.inFilePath, filename)
            onedata = self.readCSV(filepath)
            result.append(onedata)
        self.data = pd.concat(result)
        del result


    def readOneDir(self):
        if self.inDirPath is None: return
        dirnames = os.listdir(self.inDirPath)
        for dirname in dirnames:
            pass

    def sampleTowers(self,n,outFile):
        towers = self.data['tower id'].unique()
        r = np.random.choice(len(towers), size=n, replace=False)
        result = [towers[ii] for ii in r]
        samples = pd.DataFrame({'tower id': result})
        samples.to_csv(outFile,index=False)

    def filterBySampleTowers(self):
        self.samples = pd.read_csv('/common/users/zf72/SignalSense/csv/cbr-sample-tower-1000.csv')

    def sampleUsers(self, n, outFile):
        users = self.data['user id'].unique()
        r = np.random.choice(len(users), size=n, replace=False)
        result = [users[ii] for ii in r]
        samples = pd.DataFrame({'user id': result})
        samples.to_csv(outFile, index=False)

    def filterBySampleUsers(self):
        self.samples = pd.read_csv("/common/users/zf72/SignalSense/csv/tele-sample-users-10000.csv")

    def countNewLocations(self, targetDays):
        days = []
        for one in targetDays:
            dateStr = str(one)
            if one < 10: dateStr = "0{}".format(one)
            days.append(self.prefix + dateStr)
        res = self.data.groupby('user id').apply(lambda x: countLocationsInNewDay(x, days))
        res = res.reset_index(name='count')
        return (res)

    def towerCDFCount(self,outFilePath):
        towerCount = self.data.groupby("tower id")['user id'].count().reset_index(name='# of records')
        recordTowerCount = towerCount.groupby('# of records')['tower id'].count().reset_index(name='# of towers')
        recordTowerCount.to_csv(outFilePath,index=False)

