import pandas as pd
import csv
import glob
import os

csvlist = glob.glob('*.csv')

class data_processing():
    def __init__(self, folder):
        print('[Welcome] Nano U-Pb Geochronology')
        self.folder = os.getcwd()+'/'+folder
        os.mkdir(folder)

    def get_csv(self):
        datalist = glob.glob(os.getcwd()+'/*.csv')
        return datalist

    def output_csv(self, filename):
        f = open(filename,'r').readlines()
        ls = []
        for line in f:
            a = line.split(',')
#            print(a)
            if a[0] != "\n":
                if a[0] != "Raw Data\n":
                    if a[0] != "========\n":
                        if  a[0] != "Yoshikuni\n":
                            ls.append(a)
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
#        print(ls)
        csvname = filename.split("\\")[6]
        g = open(self.folder + "\output_" + csvname, 'w')
        writer = csv.writer(g, lineterminator='\n')
        for i in range(len(ls)):
            csvlist = ls[i]
            writer.writerow(csvlist)
        g.close()

    def run(self):
        datalist = self.get_csv()
        print(datalist)
        for item in datalist:
            self.output_csv(item)

data_processing = data_processing("data")
data_processing.run()
