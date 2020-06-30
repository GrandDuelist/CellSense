from CDRData import CDRData

class Test():
    def __init__(self):
        pass
    def testSingleFile(self):
        filepath = "/common/users/zf72/RawData/cdr/2013-08-01"
        headers = ['user id', 'time str', 'lon', 'lat', 'location name', '1', '2', '3', '4', '5']
        self.cdr = CDRData(inFilePath=filepath)
        self.cdr.setHeaders(headers)
        self.cdr.readData()

    def testMultiDays(self):
        dirpath = "/common/users/zf72/RawData/cdr"
        self.cdr = CDRData(inDirPath=dirpath)
        self.cdr.setMultipleDays(prefix='2013-08-',days=range(1,9))
        self.cdr.readData()
        print(self.cdr.data)

    def sampleUsers(self):
        filepath = "/common/users/zf72/RawData/cdr/2013-08-01"
        headers = ['user id', 'time str', 'lon', 'lat', 'location name', '1', '2', '3', '4', '5']
        self.cdr = CDRData(inFilePath=filepath)
        self.cdr.setHeaders(headers)
        self.cdr.readData()
        self.cdr.sampleUsers(10000,"/common/users/zf72/SignalSense/csv/tele-sample-users-10000.csv")

    def testSingleFileWithSample(self):
        filepath = "/common/users/zf72/RawData/cdr/2013-08-01"
        headers = ['user id', 'time str', 'lon', 'lat', 'location name', '1', '2', '3', '4', '5']
        self.cdr = CDRData(inFilePath=filepath)
        self.cdr.setHeaders(headers)
        self.cdr.setFilter()
        self.cdr.readData()

    def testMultiDaysWithSample(self):
        dirpath = "/common/users/zf72/RawData/cdr"
        headers = ['user id', 'time str', 'lon', 'lat', 'location name', '1', '2', '3', '4', '5']

        self.cdr = CDRData(inDirPath=dirpath)
        self.cdr.setHeaders(headers)
        self.cdr.setMultipleDays(prefix='2013-08-', days=range(1, 16))
        self.cdr.setFilter()
        self.cdr.readData()
        res = self.cdr.countNewLocations(range(8,16))
        res.to_csv("/common/users/zf72/SignalSense/csv/location-count-per-user.csv",index=False)

if __name__ == "__main__":
    print("start")
    test = Test()
    test.testMultiDaysWithSample()
    print("done")
