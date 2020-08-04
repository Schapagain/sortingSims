# Uses Python3

from matplotlib import pyplot as plt
import random
import sorts

# Define number of sorting algorithms
numSorts = 1

# Define num of items to sort, and generate a random sample
numItems = 100
maxItem = 200
random_array = random.sample(range(0,maxItem),numItems)

# Create a list of sorting generators
selection_gen = sorts.SelectionSortGenerator(random_array.copy())
quick_gen = sorts.QuickSortGenerator(random_array.copy())
merge_gen = sorts.MergeSortGenerator(random_array.copy())
gens =[selection_gen,quick_gen,merge_gen]

# Create the canvas to plot the animation
fig,axs = plt.subplots(1,3,figsize=(15,7))

# Draw initial bar plots to the canvas and
# initialize attributes for all sorting objects
for index,gen in enumerate(gens):
    gen.setup_animation(fig,axs[index])

# Update animatinos until all are complete
while(True):
    doneCount = 0
    for gen in gens:
        if not gen.animating:
            continue
        if(gen.update_animation())==0:
            doneCount+=1
    if doneCount == 2:
        break
    fig.canvas.draw()
    plt.pause(0.00001)

plt.show()
