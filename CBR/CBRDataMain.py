from  CBRData import CBRData


class CBRDataMain():
    def __init__(self):
        inFilePath = "/common/users/zf72/RawData/signaling-service-req-trace-req-only"
        self.cbr = CBRData(inFilePath=inFilePath)


    def userDistributionOnTowers(self):
        headers = ['user id', 'time_seconds', 'time str', 'time', 'tower id', 'type', 'general type']
        self.cbr.setHeaders(headers)
        self.cbr.setColumns(['user id','tower id'])
        self.cbr.readData()
        self.cbr.towerCDFCount("/common/users/zf72/SignalSense/csv/tower-cdf-count.csv")

    def sampleTowers(self):
        headers = ['user id', 'time_seconds', 'time str', 'time', 'tower id', 'type', 'general type']
        self.cbr.setHeaders(headers)
        self.cbr.setColumns(['tower id'])
        self.cbr.readData()
        self.cbr.sampleTowers(1000,"/common/users/zf72/SignalSense/csv/tower-sample-1000.csv")


if __name__ == '__main__':
    cbrdata = CBRDataMain()
    cbrdata.userDistributionOnTowers()
