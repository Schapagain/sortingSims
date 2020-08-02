# Uses Python3

import matplotlib
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import time
import sorts


n = 100
sample = 500
main_arr = random.sample(range(0,sample),n)
bubble_arr = main_arr.copy()
quick_arr = main_arr.copy()
merge_arr = main_arr.copy()
data_range = [i for i in range(len(main_arr))]

fig,axs = plt.subplots(1,3,figsize=(15,7))
selection_bar = axs[0].bar(data_range,bubble_arr)
quick_bar = axs[1].bar(data_range,quick_arr)
merge_bar = axs[2].bar(data_range,merge_arr)

selection_text = axs[0].text(n/2 - 10, sample, r'Time Elapsed: ', fontsize=7)
quick_text = axs[1].text(n/2 - 10, sample, r'Time Elapsed: ', fontsize=7)
merge_text = axs[2].text(n/2 - 10, sample, r'Time Elapsed: ', fontsize=7)

selection_gen = sorts.SelectionSortGenerator(bubble_arr)
quick_gen = sorts.QuickSortGenerator(quick_arr)
merge_gen = sorts.MergeSortGenerator(merge_arr)

axs[0].set_title("Selection Sort")
axs[1].set_title("Quick Sort")
axs[2].set_title("Merge Sort")

def update_selection(fig,selection_gen,selection_bar,selection_text,data_range):
    bubble_arr = next(selection_gen)
    if bubble_arr == 0: return 0
    else:
        for index,bar_height in zip(data_range,bubble_arr):
            selection_bar[index].set_height(bar_height)
    
        t_curr = time.time()
        selection_text.set_text(r'Time Elapsed: {:.2f}'.format(t_curr-t_init))

def update_quick(fig,quick_gen,quick_bar,quick_text,data_range,t_init):
    quick_arr = next(quick_gen)
    if quick_arr == 0: return 0
    else:
        for index,bar_height in zip(data_range,quick_arr):
            quick_bar[index].set_height(bar_height)
    
        t_curr = time.time()
        quick_text.set_text(r'Time Elapsed: {:.2f}'.format(t_curr-t_init))

def update_merge(fig,merge_gen,merge_bar,merge_text,data_range,t_init):
    merge_arr = next(merge_gen)
    if merge_arr == 0: return 0
    else:
        for index,bar_height in zip(data_range,merge_arr):
            merge_bar[index].set_height(bar_height)
    
        t_curr = time.time()
        merge_text.set_text(r'Time Elapsed: {:.2f}'.format(t_curr-t_init))

bubble_done = False
quick_done = False
merge_done = False
t_init = time.time()

while(True):

    if update_selection(fig,selection_gen,selection_bar,selection_text,data_range) == 0:
        bubble_done = True
    if update_quick(fig,quick_gen,quick_bar,quick_text,data_range,t_init) == 0:
        quick_done = True
    if update_merge(fig,merge_gen,merge_bar,merge_text,data_range,t_init) == 0:
        merge_done = True    
    if quick_done and bubble_done and merge_done:
        break

    fig.canvas.draw()
    plt.pause(0.00000000001)

plt.show()
