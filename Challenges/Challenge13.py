import csv
import pandas as pd

def mergeCSV():

    file1 = pd.read_csv('data1.csv')
    file2 = pd.read_csv('data2.csv')

    combined_csv = pd.concat([file1,file2])
    combined_csv.to_csv("combined_csv.csv",index=False)


def main():
        mergeCSV()

if __name__ == '__main__':
    main()