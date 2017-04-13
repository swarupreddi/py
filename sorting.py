
def swap(numList, pos1, pos2):
    tmp = numList[pos1]
    numList[pos1] = numList[pos2]
    numList[pos2] = tmp

def quickSort(nums, first, last):

    if first < last:
        # use the last numbers the pivot
        # and reorder the list: less than, pivot, greater or equal
        pivot = nums[last]
        toPos = first
        for i in range(first, last):
            if nums[i] < pivot:
                swap(nums, toPos, i)
                toPos += 1

        # put the pivot in the middle
        # and sort the two sublists
        swap(nums, toPos, last)
        quickSort(nums, first, toPos-1)
        quickSort(nums, toPos+1, last)

def qs(nums):
    quickSort(nums, 0, len(nums)-1)

def isSorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def test():
    l1 = [3, 2, 4, 1]
    l2 = []
    l3 = [0,1,0,1]
    l4 = [1,2,3,4,5]
    for l in [l1, l2, l3, l4]:
        qs(l)
        if not isSorted(l):
            print "!! ", l
        else:
            print l

if __name__ == '__main__':
    test()
