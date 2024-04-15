import sys
import pandas as pd

def main():
    df = pd.read_csv(sys.argv[1])
    df = df.groupby(['inputfiles']).agg({ 'filesize': 'sum'})
    print(df.info())

main()

