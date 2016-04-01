import csv
import re
import sqlite3

def genInfos(file):    
    csvfile = open(file, 'r')
    reader = csv.reader(csvfile)
    seeds = []

    for seed in reader:
        seeds.append(seed)
    
    csvfile.close()
    return seeds

def showInfos(infos):
    result = open("result.txt", 'w')
    
    tmplist = []
    result.write("total count: " + str(len(infos)) + "\n")
    #print ("total count: " + str(len(infos)))
    for seed in infos:
        if seed in tmplist:
            continue
        tmplist.append(seed)

    result.write("unique count: " + str(len(tmplist))  + "\n")
    #print ("unique count: " + str(len(tmplist)))

    for seed2 in tmplist:
        line = str(seed2) + "\t\t\t\t" + str(infos.count(seed2)) + "\n"
        result.write(line)
        #print("%s      %d" %(seed2,infos.count(seed2)))        
    result.close();
 
    
def init(csv):
    infos = genInfos(csv)
    showInfos(infos)
    
def main():
    init("seed.csv")

if __name__ == '__main__':
    main()
