# Week 3 Note

## Week 2 Recap
- help50
- eprintf
- debug50
- crypto
- string
- command line arguemts

## Finding 50
sorted or unsorted array  
binary search on sorted array

## Linear Search
```
for each element in array
  if element you're looking for
    return ture
return false
```

## Binary Search
```
look at middle of array
if element you're looking for
  reutrn true
else if element is to left
  search left half of array
else if element is to right
  search right half of array
else
  return false
```
## Memories
[Video] about how student solve same task before

## Sortign Blue Book
chouses one guys to sort the blue book

## Sortign Playing Card
buket type?
how many time will take wheㄙ data go big

## Sorting Humans
[image1]

## Selection Sort
select big(or smial) and switch

## Buble Sort
look two number each time
one loop can make sure one element is at correct position
if no swap, it mean sorting is done

## Insertion Sort
select number one by one, insert and shift

## Buble Sort Pseudocode
```
repeat untile swaps
  for i from 0 to n-2
    if i'th and i+1'th elements out of order
      swap them
```

## Selection Sort Pseudocode
```
for i from 0 to n-1
  find smallest element between i'th and n-1'th
  swap smallest with i'th element
```

## Insertion Sort Pseudocode
```
for i from 1 to n-1
  call 0'th through i-1'th elements the "sorted side"
  remove i'th element
  insert in into sorted side in order
```
## Algorithm Running Time
- buble sort
(n-1)+(n-2)+(n-3)+ ... + 1
= n(n-1)/2 = n^2/2 - n/2
=> O(n^2)

## Big-O Notation
Big O
- O(n^2)
- O(n log n)
- O(n)
- O(log n)
- O(1)
All those sorting solution - O(n^2)
Linear Search - O(n)
Binary Search - O(log n)

## Omega Notation
Linear Search - Omega(1)

## Theta Notation
Same suite Big-O and Omega Notation
Note:
https://cathyatseneca.gitbooks.io/data-structures-and-algorithms/analysis/notations.html

## Visual Sorting
Visual demo about sorting

## Recursion
why merge sort is so fast?
recursion is actually this secret ingredient

## Merge Sort
```
On input of n element
  if n < 2
    return
  else
    sort left half of elements
    sort right half of elements
    merge sorted halves
```
note:
1. use left and right point to handle position of number merge
2. merge will need entrx memory to do
3. merge sort - O(n log n)

##  Sigma0
```c
#include <stdio.h>
#include <cs50.h>
 
int sigma(int m);

int main(void) {
  int n;
  do {
    printf("Positive integer please: ");
    n = get_int();
  } while (n < 1)
  
  int answser = sigma(n);
  printf("%i\n": answser);
}

int sigma(int m) {
  int sum = 0;
  for (int i = i; i<= m; i++) {
    sum += i;
  }
  reutrn sum;
}
```
##  Sigma1
```c
int sigma(int m) {
  if(m <= 0) {
    reutrn 0
  }
  else {
    return (m + sigma(m - 1));
  }
}
```

## Google Interview
[Video]

## Outro
[Outro Video Time]
