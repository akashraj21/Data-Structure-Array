def pairInSortedRotated(arr, n, x):
    # Find the pivot element
    for i in range(0, n - 1):
        if (arr[i] > arr[i + 1]):
            break;

            # l is now index of smallest element
    l = (i + 1) % n
    # r is now index of largest element
    r = i

    # Keep moving either l
    # or r till they meet
    while (l != r):

        # If we find a pair with
        # sum x, we return True
        if (arr[l] + arr[r] == x):
            return True;

            # If current pair sum is less,
        # move to the higher sum
        if (arr[l] + arr[r] < x):
            l = (l + 1) % n;
        else:

            # Move to the lower sum side
            r = (n + r - 1) % n;

    return False;


# Driver program to test above function
arr = [11, 15, 26, 38, 9, 10]
sum = 16
n = len(arr)

if (pairInSortedRotated(arr, n, sum)):
    print("Array has two elements with sum 16")
else:
    print("Array doesn't have two elements with sum 16 ")