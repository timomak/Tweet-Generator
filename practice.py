# list1 = ["item1", "item2", "item3"]
# list2 = ["item4","item5", "item3","item2"]
# list3 = (item for item in list1 if item in list2)
#
#
# print ", ".join(list3)


# a = open('text.txt','rb')
# lines = a.readlines()
# if lines:
#     first_line = lines[:1]
#     last_line = lines[-1]
#     print last_line


# Driver code
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))

# This code is contributed by
# Smitha Dinesh Semwal 
# A binary search based function
# that returns index of a peak element
def findPeakUtil(arr, low, high, n):

     # Find index of middle element
     # (low + high)/2
     mid = low + (high - low)/2
     mid = int(mid)

    # Compare middle element with its
    # neighbours (if neighbours exist)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
       (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid


    # If middle element is not peak and
    # its left neighbour is greater
    # than it, then left half must
    # have a peak element
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)

    # If middle element is not peak and
    # its right neighbour is greater
    # than it, then right half must
    # have a peak element
    else:
        return findPeakUtil(arr, (mid + 1), high, n)


# A wrapper over recursive
# function findPeakUtil()
def findPeak(arr, n):

    return findPeakUtil(arr, 0, n - 1, n)
