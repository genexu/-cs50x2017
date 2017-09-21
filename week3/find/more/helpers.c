/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */

#include <cs50.h>
#include <math.h>
#include <stdio.h>

#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = round((left + right) / 2);
        if (values[mid] > value) {
            right = mid - 1;
        }
        else if (values[mid] < value) {
            left = mid + 1;
        }
        else {
            return true;
        }
    }
    return false;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    // Non-comparison sorts
    // Counting sort Big O = O(n)
    // Can use when you are sorting integers with a limited range
    const int MAX_SIZE = 65536;
    static int *tmp_array;
    tmp_array = malloc(MAX_SIZE * sizeof(int));
    for (int i = 0; i < n; i++) {
        int index = values[i];
        tmp_array[index]++;
    }
    int pos = 0;
    for (int i = 0; i < MAX_SIZE; i++) {
        if (tmp_array[i] != 0) {
            // Show counting result
            // printf("index %i count = %i\n", i, tmp_array[i]);
            // Asign index into result array
            for (int j = 0; j < tmp_array[i]; j++) {
                values[pos] = i;
                pos++;
            }
        }
    }

}
