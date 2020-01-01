import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os

ROOT = os.path.abspath("../../")
DIR_DATA = os.path.join(ROOT, "data")

class Graph:
    def __init__(self, *args):
        with plt.style.context('dark_background'):
            plt.figure(figsize=(len(args), 1))
            gs1 = gridspec.GridSpec(len(args), 1)
            gs1.update(wspace=0.025, hspace=0.0)
            for i in range(len(args)):
                ax1 = plt.subplot(gs1[i])
                ax1.step(args[i][0], args[i][1], 'r')
                plt.yticks(np.arange(0, 1.5, step=1))
                plt.xticks(np.arange(0, 10, step=0.5))

    def show(self):
        plt.show()

    def save(self):
        plt.savefig(os.path.join(DIR_DATA, "graph.png"), quality=75, dpi=1000)