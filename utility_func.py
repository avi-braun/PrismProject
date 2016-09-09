
import math as m, math
import numpy as np
import matplotlib.pyplot as plt

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def frangeV(start, stop, step):
    iV=[]
    i = start
    while i < stop:
        iV.append(i)
        i += step
    return (iV)

def get_cmap(N):
    '''Returns a function that maps each index in 0, 1, ... N-1 to a distinct
    RGB color.'''
    color_norm  = colors.Normalize(vmin=0, vmax=N-1)
    scalar_map = cmx.ScalarMappable(norm=color_norm, cmap='hsv')
    def map_index_to_rgb_color(index):
        return scalar_map.to_rgba(index)
    return map_index_to_rgb_color
     # using:
    # for i in range(N):
    #     col = cmap(i)
    #     rect = plt.Rectangle((i, -0.5), 1, 1, facecolor=col)
    #     ax.add_artist(rect)