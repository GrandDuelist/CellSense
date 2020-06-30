import pandas as pd
import geopandas as geopd
from shapely.geometry import Point
from shapely.geometry import LineString
import matplotlib.pyplot as plt
from shapely import wkt
from cpssdk import CPSDistance

class RoadData():
    def __init__(self,data):
        self.data = data
        self.visMethod = 'map'
        self.data = geopd.GeoDataFrame(self.data)
        self.ax = None
        if 'geometry' in self.data:
            self.data['geometry'] = self.data['geometry'].apply(lambda x: wkt.loads(x))
        self.order = 0

    def setBoundaryData(self,boundary):
        self.boundary = boundary

    def addBoundaryLayer(self):
        self.ax = self.boundary.plot()

    def setVisMethod(self,visMethod):
        self.visMethod = visMethod

    def cutRoadInBoundary(self,boundaryPath):
        boundary = geopd.read_file(boundaryPath)['geometry'][0]
        filtering = self.data.apply(lambda x: boundary.contains(Point(x['x1'],x['y1'])) and boundary.contains(Point(x['x2'],x['y2'])),axis=1)
        self.data = self.data[filtering].copy().reset_index(drop=True)
        self.data['geometry'] = self.data.apply(lambda x: LineString([(x['x1'],x['y1']),(x['x2'],x['y2'])]),axis=1)
        self.data = geopd.GeoDataFrame(self.data)

    def exportData(self,outFilePath):
        self.data.to_csv(outFilePath,index=False)

    def visualize(self):
        if self.visMethod == 'map':
            self.visualMap()

    def visualMap(self):
        if self.ax:
            self.ax = self.data.plot(self.ax,)
        else:
            self.ax = self.data.plot()

    def savePlot(self,outFilePath):
        plt.savefig(outFilePath, bbox_inches='tight',dpi=2000)


    def statistics(self):
        cpsdist = CPSDistance()
        self.data['dis'] =  self.data.apply(lambda x: cpsdist.GPSDist((x['x1'],x['y1']),(x['x2'],x['y2'])), axis=1)
        print(self.data['dis'].sum())
        print(len(self.data))


