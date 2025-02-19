from typing import Sequence


def linear_search(array: Sequence, target):
    """
    Perform a linear search on the given sequence to find the target element.

    Parameters:
    array (Sequence): The sequence to search through.
    target: The element to search for.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    for idx, element in enumerate(array):
        if element == target:
            return idx
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target = 3
    found_idx = linear_search(arr, target)  # 2
    if found_idx != -1:
        print(f"Element found at index {found_idx} in the array")
    else:
        print(f"Element {target} not found in the array")

    # Test cases are in the test directory.
