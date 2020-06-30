from CDRPlotter import CDRPlotter
import pandas as pd

class CDRPlotterMain():
    def plotCDRNewLocationMain(self):
        inFilepath = "../csv/location-count-per-user.csv"
        outFilePath = "../plots/location-count-per-user.pdf"
        data = pd.read_csv(inFilepath)
        cdr = CDRPlotter(data)
        cdr.locationCountToCDF()
        cdr.plotNewLocationCDF(outFilePath)

if __name__ == '__main__':
    cdr = CDRPlotterMain()
    cdr.plotCDRNewLocationMain()
