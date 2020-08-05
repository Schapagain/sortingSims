# Uses Python3

from matplotlib import pyplot as plt
import random
import sorts

def main():

    # Define num of items to sort, and generate a random sample
    numItems = 100
    maxItem = 100
    random_array = random.sample(range(0,maxItem),numItems)

    # Create a list of sorting animations
    selection_animation = sorts.SelectionSortGenerator(random_array.copy())
    quick_animation = sorts.QuickSortGenerator(random_array.copy())
    merge_animation = sorts.MergeSortGenerator(random_array.copy())
    animations =[selection_animation,quick_animation,merge_animation]

    # Create the canvas to plot the animation
    fig,axs = plt.subplots(1,3,figsize=(15,7))

    # Draw initial bar plots to the canvas and
    # initialize attributes for all sorting objects
    for index,animation in enumerate(animations):
        animation.setup_animation(fig,axs[index])

    def updateAnimations():
        not_done = False
        for animation in animations:
            if animation.animating:
                curr_not_done = animation.update_animation()
                not_done = not_done or curr_not_done
        return not_done

    not_done = True
    while(not_done):
        not_done = updateAnimations()
        fig.canvas.draw()
        plt.pause(0.0001)

    plt.show()
if __name__ == '__main__':main()