import pandas as pd
import csv
import glob
import os
import numpy as np

dead_time = []

class data_calculation():
    def __init__(self, folder):
        print('[Calculation] Nano U-Pb Geochronology')
        self.folder = os.getcwd()+'\\'+folder

    def get_csv(self):
        datalist = glob.glob(self.folder +'/*.csv')
        return datalist

    def read_csv(self, filename):
        df = pd.read_csv(filename)
        return df

    def calculate_sum(self, filename):
        df = self.read_csv(filename)
        print(np.sum(df["Hg(202)"])*df["Timestamp"][0])
        print(np.sum(df["Pb(204)"])*df["Timestamp"][0])
        print(np.sum(df["Pb(206)"])*df["Timestamp"][0])
        print(np.sum(df["U(238)"])*df["Timestamp"][0])
        #print(np.sum(df["Pb(208)"])*df["Timestamp"][0])

    def run(self):
        datalist = self.get_csv()
        print(datalist)
        for item in datalist:
            print(item)
            self.calculate_sum(item)

data_calculation = data_calculation("data")
data_calculation.run()
