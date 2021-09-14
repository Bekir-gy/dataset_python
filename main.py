import matplotlib.pyplot as plt
import numpy as np
import re


class Plot:
    def plot_latlon_street(self):
        path = "Logs\\KNN_plots"
        for StreetName in ["WideStreet", "MiddleWideStreet", "NarrowStreet"]:
            fig = plt.figure(figsize=(15, 8))
            plt.suptitle('Latitude and Longitude data of the ' + StreetName)
            plt.xlabel('Latitude')
            plt.ylabel('Longitude')
            for x in ["LeftSide", "RightSide"]:
                InputFile = 'Dataset\\StreetData\\' + StreetName + '\\' + x + '\\' + x + '.gpx'
                data = open(InputFile).read()
                lat = np.array(re.findall(r'lat="([^"]+)', data), dtype=float)
                lon = np.array(re.findall(r'lon="([^"]+)', data), dtype=float)
                plt.scatter(lat, lon, label=x)

            plt.legend()
            plt.show()
            fig.savefig(f"{path}\\{StreetName}.png")
            plt.close()

if __name__ == '__main__':
    plot = Plot()
    plot.plot_latlon_street()