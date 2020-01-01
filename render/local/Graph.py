import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np


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
        plt.savefig("test.png", quality=75, dpi=1000)


if __name__ == "__main__":
    g = Graph(([0, 2.24, 4.32, 5.45, 10], [1, 0, 1, 1, 1]),
              ([0, 1.23, 1.46, 2.49, 10], [0, 1, 0, 1, 1]),
              ([0, 1.35, 2.12, 4.49, 10], [1, 0, 1, 1, 1]),
              ([0, 1.13, 3.46, 8.49, 10], [1, 1, 1, 0, 0]),
              ([0, 0.53, 5.12, 7.54, 10], [1, 0, 1, 1, 0]),
              ([0, 2.24, 3.54, 5.24, 10], [0, 1, 0, 0, 0]))
    g.show()