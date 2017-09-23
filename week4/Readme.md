# Week 4 Note
## Week3 in Review
search and sort
- linear search
- binary search
- bubble sort
- selection sort
- insertion sort
- merge sort

complex
- n^2
- n log n
- n
- log n
- 1
...

Big O
Mega
theta

## Strings are a Lie
we will going to understand what string aturlly is.

## compare0
```c
#include <stdio.h>
#include <cs50.h>

int main(void) {
  printf("s: ");
  string s = get_string();
  
  printf("t: ");
  string t = get_string();
  
  if (s == t) {
    printf("same\n");
  }
  else {
    printf("diff\n");
  }
}
```
```basg
~$./compare
s = ABC
t = ABC
diff
```

## copy0
```c
#include <stdio.h>
#include <ctype.h>
#include <cs50.h>

int main(void) {
  printf("input s: ");
  string s = get_string();
  if (s == NULL) {
    return 1;
  }
  string t = s;
  
  if (strlen(t) > 0) {
    t[0] = toupper(t[0]);
  }
  
  printf("s: %s\n", s);
  printf("t: %s\n", t);
}
```
```
~$./copy0
input s: gene
s: Gene
t: Gene
```

## noswap
```
#include <stdio.h>

void swap(int a, int b);

int main(void) {
  int x = 1;
  int y = 2;
  printf("x is %i\n", x);
  printf("y is %i\n", y);
  printf("swapping...\n");
  swap(x, y);
  printf("swapped\n");
  printf("x is %i\n", x);
  printf("y is %i\n", y);
}

void swap(int a, int b) {
  int tmp = a;
  a = b;
  b = tmp;
}
```

```bash
~$ ./noswap
x is 1
y is 2
swapping...
swapped
x is 1
y is 2
```

!!! Why those program not work? !!!
A: About Program Memory

## Program Memory
![](https://github.com/genexu/cs50x2017/blob/master/week4/Screenshot-2016-fall-lectures-4-at-17m16s.png)

## The Stack
![](https://github.com/genexu/cs50x2017/blob/master/week4/Screenshot-2016-fall-lectures-4-at-21m26s.png)

##  get_string() in Detail
```c
string s = get_string()

s => momery arrow to address 123
_________________
|G   |e   |n|e|\0|
-----------------
123  124  125 ...

string t = get_string()

t => !!! momery will arrow to new address ex: 234 !!!
_________________
|G   |e   |n|e|\0|
-----------------
234  235  236 ...
```

```
string s = get_string();
s => momery arrow to address 123
_________________
|G   |e   |n|e|\0|
-----------------
123  124  125 ...

then...
string t = s;

t => arrow to s address 123

so...
t = toupper(t[0]);
=> toupper char in address 123
that's why s will also been updated

address aka. pointer
```

## Pointer Fun Preview
[Vedio]

## Taking Off the Training Wheels
drop the training wheels

## compare1
```c
#include <stdio.h>
#include <string.h>
#include <cs50.h>

int main(void) {
  printf("s: ");
  char *s = get_string();
  
  printf("t: ");
  char *t = get_string();
  
  if (s != NULL && t != NULL) {
    if (strcmp (s, t)) {
      printf("same\n");
    }
    else {
      printf("diff\n");
    }
  }
```
```
~$ ./compare1
s: Gene
t: gene
diff
s: Gene
t: Gene
same
s: foo
t: boo
diff
```

## char *
string = char *

## strcmp
#include <string.h>
strcmp(str1, str2)

## copy1
```
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void) {
    printf("s: ");
    char *s = get_string();
    if (s == NULL) {
        return 1;
    }

    char *t = malloc((strlen(s) + 1) * sizeof(char));
    if (t == NULL) {
        return 1;
    }

    for (int i = 0, n = strlen(s); i <= n; i++) {
        t[i] = s[i];
    }

    if (strlen(t) > 0) {
        t[0] = toupper(t[0]);
    }

    printf("s: %s\n", s);
    printf("t: %s\n", t);

    free(t);

    return 0;
}
```
```bash
~$ input s: gene
s = gene
t = Gene
```
## malloc
!!! Memory Allocate !!!
![](https://github.com/genexu/cs50x2017/blob/master/week4/Screenshot-2016-fall-lectures-4-at-45m7s.png)

## Introducing Pointers
```
// dont copy, give me x, y address
void swap(int *a, int *b) {
  int tmp = *a;
  *a = *b;
  *b = tmp;
}
```

## swap
```c
#include <stdio.h>

void swap(int *a, int *b);

int main(void) {
    int x = 1;
    int y = 2;

    printf("x is %i\n", x);
    printf("y is %i\n", y);
    printf("Swapping...\n");
    swap(&x, &y); // !!! & get address x, get address y
    printf("Swapped!\n");
    printf("x is %i\n", x);
    printf("y is %i\n", y);
}

void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
```

## Proverbial Lighrbulb
[Story]

## Pointer Arithmetic
What pointer is?

## Pointer
```c
int main (void) {
  char *s = get_string();
  if (s == NULL) {
    reutrn 1;
  }
  
  for (int i = 0, n = strlen(s); i < n; i++) {
    printf("%c\n", *(s+i)); suger => s[i]
  }
}
```

## Pointer Gotchas
```
int main(void) {
  int *x;
  int *y;
  x = malloc(sizeof(int));
  *x = 42;
  *y = 12; // no further, some thing bad will happen
  y = x
  *y = 13;
}
```

## Pointer Fun with Binky
[Vodio]

Pointer Rule
1. Pointer and pointee are separae -- dont forget to set up the pointee
2. Dereference a ponter to access its pointee
3. Assignment (=) between pointers makes them point to the same pointee

## Memory Leak
!!! use and free memory !!!

## valgrind
```
valgrind -- leak-check=full ./memory
```

## memory
```
#include <stdlib.h>
void f(void) {
  int *x = malloc(10 * sizeof(int));
  
  x[10] = 0; // ??? out of index
  

}

int main(void) {
  f();
  return 0;
}
```
when those memory keep been asked, it will slow down your computer for never ask it free
```
  // how to fix it?
  x[9] = 0 // assign to right pointee
  free(x) // and remeber free when you dont use it
```

## Types of Overflow
- stack overflow
- heap overflow
- buffer overflow

## Buffer Overflow
```c
include <string.h>

void foo(char *bar) {
  char c[12];
  memcpy(c, bar, strlen(bar));
  // copy bar memory to c upto strlen(bar);
}

int main (int argc, char *argv[]) {
  foo(argv[1]);
}
```

## Zooming in
simple introduction and video

## Representing Images
"pixel"
"enhance"

## JPEG
compress
255, 216, 255

## Hexadecimal
16bit
0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f

255      216      255
11111111 11011000 11111111
1111 1111 1101 1000 1111 1111
f    f    d    8    f    f
0xff, 0xd8, 0xff

## BMP
![](https://github.com/genexu/cs50x2017/blob/master/week4/Screenshot-2016-fall-lectures-4-at-1h39m14s.png)

## struct
```
typedef struct {
  char *name;
  char *dorm;
}
student;
```
## structs0
```c
#include <cs50.h>
#include <stdio.h>
#include <string.h>

#include "structs.h"

#define STUDENTS 3

int main(void)
{
    student students[STUDENTS];

    for (int i = 0; i < STUDENTS; i++)
    {
        printf("name: ");
        students[i].name = get_string();

        printf("dorm: ");
        students[i].dorm = get_string();
    }

    for (int i = 0; i < STUDENTS; i++)
    {
        printf("%s is in %s.\n", students[i].name, students[i].dorm);
    }
}
```

## structs1
```
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "structs.h"

#define STUDENTS 3

int main(void)
{
    student students[STUDENTS];

    for (int i = 0; i < STUDENTS; i++) {
        printf("name: ");
        students[i].name = get_string();

        printf("dorm: ");
        students[i].dorm = get_string();
    }

    FILE *file = fopen("students.csv", "w");
    if (file != NULL) {
        for (int i = 0; i < STUDENTS; i++) {
          // file print
          fprintf(file, "%s,%s\n", students[i].name, students[i].dorm);
        }
        fclose(file);
    }
}
```
## CSV
Text,Text,Text
Text,Text,Text
Text,Text,Text

## Enhance
[Video]

## Outro
[Video]
