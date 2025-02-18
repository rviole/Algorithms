#include <stdio.h>
#include "LinearSearch.h"
/**
 * Performs linear search to find target element in array
 * @param arr Array to search in
 * @param size Size of the array
 * @param target Element to find
 * @return Index of target if found, -1 otherwise
 */
int linear_search(int arr[], int size, int target) {
  for (int i = 0; i < size; i++) {
    if (arr[i] == target) {
      return i;
    }
  }
  return -1;
}

// int main(void) {
//   int arr[] = {1, 2, 3, 4, 5};
//   int size = sizeof(arr) / sizeof(arr[0]);
//   int target = 3;

//   int idx = linear_search(arr, size, target);
//   if (idx == -1) {
//     printf("Not found");
//   } else {
//     printf("Element %d found at index %d", target, idx);
//   }

//   return 0;
// }