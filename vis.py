import argparse
import os, sys
import os.path as osp
import matplotlib.pyplot as plt
import numpy as np

from baselines.common import plot_util as pu


LOGS = './logs'


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, required=True, help='Sub directory path')

    args = parser.parse_args()

    path = osp.join(LOGS, args.name)

    results = pu.load_results(path)  # return a list of Result object

    # test for 0
    r = results[-1]
    plt.plot(np.cumsum(r.monitor.l), pu.smooth(r.monitor.r, radius=10))
    plt.show()
