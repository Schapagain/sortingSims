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

class QuickSortGenerator:

    def __init__(self,arr):
        
        try:
            self.gen = self._quick_sort(0,len(arr)-1)
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

    def _quick_sort(self,l,h):
        if l>=h:
            return
        else:
            arr = self.arr
            m = self._partition(l,h)
            yield arr
            yield from self._quick_sort(l,m-1)
            yield from self._quick_sort(m+1,h)

class SelectionSortGenerator:

    def __init__(self,arr):
        try:
            self.length = len(arr)
        except TypeError:
            print("Error: Can only instantiate with an iterable.")
        else:
            self.arr = arr
            self.gen = self._selection_sort()

    def __next__(self):
        try:
            next_val = next(self.gen)
        except StopIteration:
            return 0
        else:
            return next_val

    def _find_min_index(self,l,h):
        m = l
        for i in range(l,h):
            if self.arr[i] < self.arr[m]:
                m = i
        return m

    def _selection_sort(self):
        arr = self.arr
        for i in range(self.length):
            yield arr
            m = self._find_min_index(i,self.length)
            arr[i],arr[m] = arr[m],arr[i]

class MergeSortGenerator:

    def __init__(self,arr):
        try:
            self.gen = self._merge_sort(0,len(arr)-1)
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

    def _merge_sort(self,l,h):
        if l<h:
            mid = l + (h-l) // 2
            yield from self._merge_sort(l,mid)
            yield from self._merge_sort(mid+1,h)
            self._merge(l,h,mid)
            yield self.arr



