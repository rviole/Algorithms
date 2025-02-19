from LinearSearch import linear_search

def binary_search(arr, target):
    """
    Perform a binary search on the given sorted array to find the target element.

    Parameters:
    arr (Sequence): The sorted array to search through.
    target: The element to search for.

    Returns:
    int: The index of the target element if found, otherwise None.
    """
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            start = middle + 1
        else:
            end = middle - 1

    return None

def binary_search_recursive(arr, target):
    """
    Perform a binary search on the given sorted array to find the target element using recursion.

    Parameters:
    arr (Sequence): The sorted array to search through.
    target: The element to search for.

    Returns:
    int: The index of the target element if found, otherwise None.
    """
    start = 0
    end = len(arr) - 1

    def _binary_search(start, end):
        if start <= end:
            middle = (start + end) // 2
            if arr[middle] == target:
                return middle
            elif arr[middle] < target:
                return _binary_search(middle + 1, end)
            else:
                return _binary_search(start, middle - 1)
        return None

    return _binary_search(start, end)




if __name__ == "__main__":
    
    import time

    arr = range(5_000_0000)
    target = 5_000_0000 - 1
    
    print(f"Array size: {len(arr)}")
    print(f"Target: {target}\n")
    
    start = time.time()
    print(f"Linear Search: {linear_search(arr, target)}")
    print(f"Time taken: {(time.time() - start):.6f}s \n")
    
    start = time.time()
    print(f"Binary Search: {binary_search(arr, target)}")
    print(f"Time taken: {(time.time() - start):.6f}s \n")

    start = time.time()
    print(f"Binary Search Recursive: {binary_search_recursive(arr, target)}")
    print(f"Time taken: {(time.time() - start):.6f}s \n")
    
    # Test cases are in the test directory.
    
