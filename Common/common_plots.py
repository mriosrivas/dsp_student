import numpy as np
import matplotlib.pyplot as plt

class Plot:
    
    def __init__(self):
        pass


    def plot_multiple(self, signal):
        """ 
        Function that plots a impulse/step decomposition of a signal.

        Parameters: 
        signal (numpy array): Square matrix of impulse/step decomposition 
        where each row represents a single impulse/step decomposition of each 
        n-th sample.
        """
        plt.rcParams["figure.figsize"] = (15,25)

        delta = 1
        y_min = signal.min() - delta
        y_max = signal.max() + delta

        N = signal.shape[0]

        if (N%2!=0):
            M = N+1
        else:
            M = N

        for i in range(M):
            plt.subplot(int(M/2),2,i+1)
            try:
                plt.stem(signal[i], use_line_collection=True);
                plt.ylim((y_min, y_max))
                plt.title("Sample: {}".format(i))
                plt.grid()
            except:
                pass


    def plot_single(self, signal, title="Signal", style='stem'):
        """ 
        Function that plots stem of a given signal.

        Parameters: 
        signal (numpy array): Array of numbers to be plotted.
        """

        delta = 1
        y_min = signal.min() - delta
        y_max = signal.max() + delta

        plt.rcParams["figure.figsize"] = (10,5)
        
        if(style=='stem'):
            plt.stem(signal[0], use_line_collection=True);
        elif(style=='line'):
            plt.plot(signal[0]);
        plt.ylim((y_min, y_max))
        plt.title(title)
        plt.grid()
        
        
    def plot_three_signals(self, x1, x2, x3, titles=('x1', 'x2', 'x3'), labels=('sample', 'sample', 'sample')):
        
        plt.rcParams["figure.figsize"] = (25,10)
        plt.subplot(2, 2, 1)
        plt.plot(x1)
        plt.title(titles[0])
        plt.xlabel(labels[0])

        plt.subplot(2, 2, 2)
        plt.plot(x2)
        plt.title(titles[1])
        plt.xlabel(labels[1])

        plt.subplot(2, 1, 2)
        plt.plot(x3)
        plt.title(titles[2])
        plt.xlabel(labels[2])

        plt.tight_layout(pad=3.0)

        plt.show()
