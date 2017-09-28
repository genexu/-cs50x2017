# Week 5 Note
## Week 4 Recap
- What is pointer
- Memory structure stack, heap
```
// Use pointer to prevent var copy
void swap (int *a, int *b) { 
...
}
```
- Images 

```
typedef struct {
  string name;
  string dorml
} student
```

## Limitation of Arrays
Array use contiguous memory, it is not suitable structure if data keep growning.

## Lists
![](https://github.com/genexu/cs50x2017/blob/master/week5/Screenshot-2016-fall-lectures-5-at-11m21s.png)

## Nodes
```c
typedef struct node {
  int n;
  struct node *next;
}
```
```
n
_________
|int    |
---------
|*next  |
---------
```

## Linked List
- delete
- insert
insert to first, Big O = O(1)
- search
we need trav node one by one with pointer *next, and so search Big O = O(n)

Ref http://bigocheatsheet.com/

## List of Humans
![](https://github.com/genexu/cs50x2017/blob/master/week5/Screenshot-2016-fall-lectures-5-at-23m50s.png)

## List Operations
- insert head, middle, tail ...
- remove ...
...

!!! Alway remember don't lose the chain !!!

## Implementing search
```c
bool search(int n, node *list) {
  node *ptr = list;
  while (ptr != NULL) {
    if (ptr->n == n) {
      reutrn true;
    }
    ptr = ptr->next()
  }
  return false;
}
```
## Linked List Tradeoffs
Linked List solve the memory limitation problem, but it also have some other problem, search time, insert operation...etc.

## Stack
- push
- pop
LIFO

## Implementing a Stack
```c
typedef struct {
  int *numbers;
  int size;
} stack

```

## Queues
- enqueue
- dequeue
FIFO

## Implementing a Queue
```c
typedef struct {
  int front;
  int *numbers;
  int size;
}
```
## Abstract Data Types
simple intruction

## Jack Learns the Facts
Funny video about stack and queue
[Video]

## Trees
![](https://github.com/genexu/cs50x2017/blob/master/week5/Screenshot-2016-fall-lectures-5-at-58m36s.png)

## Binary Search Tree
smaller go left, biger go right
!!! balance problem !!!

## Implementing a Tree
```c
typedef struct node {
  int n;
  struct node *left;
  struct node * right;
} node;

bool search (int n, node *tree) {
  if (tree == NULL) {
    return false;
  }
  else if (n < tree->n) {
    return search(n, tree->left);
  }
  else if (n > tree->n) {
    return search(n, tree->right);
  }
  else {
    return true;
  }
}
```

## Huffman Coding
```
ASCII
A  B  C
65 66 67 ...
```
- most proplar letter should use less cost to storge
- intruction morse code and it problem

so how we implement huffman tree
- coculate char frequency of string
- sort by frequency
- combain two node to one ...loop
![](https://github.com/genexu/cs50x2017/blob/master/week5/Screenshot-2016-fall-lectures-5-at-1h21m23s.png)
![](https://github.com/genexu/cs50x2017/blob/master/week5/Screenshot-2016-fall-lectures-5-at-1h22m15s.png)
![](https://github.com/genexu/cs50x2017/blob/master/week5/Screenshot-2016-fall-lectures-5-at-1h23m44s.png)
![](https://github.com/genexu/cs50x2017/blob/master/week5/Screenshot-2016-fall-lectures-5-at-1h24m46s.png)

```c
typedef struct node {
  char symbol;
  float frequency;
  struct node *left;
  struct node *right;
} node
```

## Hash Tables
implement hash function and gen hash code, hash code pointing to address where data be stroged.
!!! same input should always return same hash code !!!
ex: 
input A always return 1
input B always return 2
...

## Buckets
![](https://github.com/genexu/cs50x2017/blob/master/week5/Screenshot-2016-fall-lectures-5-at-1h32m59s.png)

## Linear Probing
Intruction problem when hash function have same code with two deff string
Ex:
hash('Alice') => 1122
hash('Alex') => 1122

## Separate Chaining
![](https://github.com/genexu/cs50x2017/blob/master/week5/Screenshot-2016-fall-lectures-5-at-1h37m12s.png)

## Tries
Big O = O(constant) constant = length of key
![](https://github.com/genexu/cs50x2017/blob/master/week5/Screenshot-2016-fall-lectures-5-at-1h39m9s.png)

## Outro
[Video]
