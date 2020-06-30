from RoadData import RoadData
import pandas as pd
import matplotlib.pyplot as plt

class RoadDataMain():
    def __init__(self):
        pass

    def mapInBoundaryMain(self):
        filepath = "/common/users/zf72/SignalSense/csv/hefei-road-ways-export.csv"
        boundaryPath = "/common/users/zf72/SignalSense/csv/hefei-boundary.geojson"

        data = pd.read_csv(filepath)
        self.roadData = RoadData(data)

        self.roadData.cutRoadInBoundary(boundaryPath)
        self.roadData.exportData("/common/users/zf72/SignalSense/csv/hefei-road-ways-in-boundary.csv")
    def visualMapMain(self):
        filepath = "/common/users/zf72/SignalSense/csv/hefei-road-ways-in-boundary.csv"
        data = pd.read_csv(filepath)
        self.roadData = RoadData(data)
        self.roadData.visualize()
        self.roadData.savePlot("/common/users/zf72/SignalSense/plots/hefei-road-map.png")
        plt.show()
    def mapStatisticsMain(self):
        filepath = "/common/users/zf72/SignalSense/csv/hefei-road-ways-in-boundary.csv"
        data = pd.read_csv(filepath)
        self.roadData = RoadData(data)
        self.roadData.statistics()


if __name__ == "__main__":
    roadData = RoadDataMain()
    roadData.mapStatisticsMain()
