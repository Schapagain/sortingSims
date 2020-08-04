'''

A collection of sorting generators. 

This is useful if you need the state of the array being sorted
after each sorting step. 

It contains several classes that can be instantiated as generators. 
To get the next array after a sorting step, just call next(object).

INPUTS:
    -> Iterable to be sorted
OUTPUTS:
    Through next(generator object):
    -> Yield the next state of the generator
    -> Return 0 if the generator is exhausted

Classed included:

    QuickSortGenerator
    SelectionSortGenerator


'''


class SortGenerator:

    def __init__(self,arr):
        
        try:
            self.gen = self._sort(0,len(arr)-1)
        except TypeError:
            print("Error: Can only instantiate with an iterable.")
        else:
            self.arr = arr

    def __next__(self):
        try:
            next_val = next(self.gen)
        except StopIteration:
            return 0
        else:
            return next_val
    
    def _sort(self,l,h):
        return 0
    
    def _set_axis_label(self):
        pass

    def setup_animation(self,fig,ax):
        self.animating = True
        self.fig = fig
        self.ax = ax
        self.bar = ax.bar(list(range(len(self.arr))),self.arr)
        self.text = ax.text(len(self.arr)/2 - 10, max(self.arr) , r'Time Elapsed: ', fontsize=10)
        self.timeElapsed = 0
        self._set_axis_label()
    
    def update_animation(self):

        # Get the next state of the array
        # record time taken
        import time
        t_init = time.time()
        next_arr = self.__next__()
        t_curr = time.time()
        self.timeElapsed += t_curr - t_init

        # stop animating if the generator is exhausted
        # else update all bar heights
        if next_arr == 0:
            self.animating = False
            return 0
        else:
            data_range = list(range(len(next_arr)))
            for index,bar_height in zip(data_range,next_arr):
                self.bar[index].set_height(bar_height)
        self.text.set_text(r'Time Elapsed: {:.4f}'.format(self.timeElapsed))

class SelectionSortGenerator(SortGenerator):

    def _find_min_index(self,l,h):
        m = l
        for i in range(l,h):
            if self.arr[i] < self.arr[m]:
                m = i
        return m

    def _sort(self,l,h):
        arr = self.arr
        for i in range(h-l+1):
            yield arr
            m = self._find_min_index(i,h-l+1)
            arr[i],arr[m] = arr[m],arr[i]

    def _set_axis_label(self):
        self.ax.set_title('Selection Sort')

class QuickSortGenerator(SortGenerator):

    def _partition(self,l,h):
        import random
        arr = self.arr
        k = random.randint(l,h)
        arr[l], arr[k] = arr[k], arr[l]

        pivot = arr[l]
        j = l
        for i in range(l+1,h+1):
            if arr[i] <= pivot:
                j += 1
                arr[j],arr[i] = arr[i],arr[j]
        arr[l],arr[j] = arr[j],arr[l]

        return j
    def _sort(self,l,h):
        if l>=h:
            return
        else:
            arr = self.arr
            m = self._partition(l,h)
            yield arr
            yield from self._sort(l,m-1)
            yield from self._sort(m+1,h)

    def _set_axis_label(self):
        self.ax.set_title('Quick Sort')

class MergeSortGenerator(SortGenerator):

    def _merge(self,l,h,m):
        arr = self.arr
        merged = [0]*(h-l+1)
        i=l
        j=m+1
        k=0
        while i<=m and j<=h:
            if arr[i] < arr[j]:
                merged[k] = arr[i]
                i+=1
            else:
                merged[k] = arr[j]
                j+=1
            k+=1
        while i<=m:
            merged[k] = arr[i]
            k+=1
            i+=1
        while j<=h:
            merged[k] = arr[j]
            k+=1
            j+=1
        self.arr[l:h+1] = merged

    def _sort(self,l,h):
        if l<h:
            mid = l + (h-l) // 2
            yield from self._sort(l,mid)
            yield from self._sort(mid+1,h)
            self._merge(l,h,mid)
            yield self.arr

    def _set_axis_label(self):
        self.ax.set_title('Merge Sort')