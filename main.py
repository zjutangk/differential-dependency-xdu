import sys
import argparse
from model import Domino
import pandas as pd


def main(args):
    data = pd.read_csv(args.input_path, index_col=0)
    model = Domino(data)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default="data/iris.csv")

    args = parser.parse_args(args=[])
    main(args)