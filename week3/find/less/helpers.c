/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */

#include <cs50.h>
#include <math.h>

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
    // Bubble sort Big O = O(n^2)
    for (int i = n - 1; i > 1; i--) {
        for (int j = 0; j < i; j++) {
            if (values[j] > values[j + 1]) {
                int tmp = values[j];
                values[j] = values[j + 1];
                values[j + 1] = tmp;
            }
        }
    }
}
