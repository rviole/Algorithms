#include "../../c/LinearSearch.h"
#include <assert.h>
#include <stdio.h>

// Test function to run all the tests
void test_linear_search() {
  // Test Case 1: Element is present in the array
  int arr1[] = {1, 2, 3, 4, 5};
  int n1 = sizeof(arr1) / sizeof(arr1[0]);
  int x1 = 3;
  int result1 = linear_search(arr1, n1, x1);
  assert(result1 == 2); // Expected index is 2

  // Test Case 2: Element is not present in the array
  int arr2[] = {1, 2, 3, 4, 5};
  int n2 = sizeof(arr2) / sizeof(arr2[0]);
  int x2 = 6;
  int result2 = linear_search(arr2, n2, x2);
  assert(result2 == -1); // Expected result is -1 (not found)

  // Test Case 3: Empty array
  // CAN'T TEST:
  // When we pass an array to a function in C, we are actually passing a
  // pointer to the array. If the array is uninitialized or doesn't exist in
  // memory (e.g., a NULL pointer), the pointer points to nowhere, causing
  // invalid memory access when trying to use it inside the function.

  // Test Case 4: Single-element array, element present
  int arr4[] = {10};
  int n4 = sizeof(arr4) / sizeof(arr4[0]);
  int x4 = 10;
  int result4 = linear_search(arr4, n4, x4);
  assert(result4 == 0); // Expected index is 0

  // Test Case 5: Single-element array, element not present
  int arr5[] = {20};
  int n5 = sizeof(arr5) / sizeof(arr5[0]);
  int x5 = 10;
  int result5 = linear_search(arr5, n5, x5);
  assert(result5 == -1); // Expected result is -1 (not found)
}

int main() {
  // Run tests
  test_linear_search();

  printf("All tests passed!\n");
  return 0;
}
