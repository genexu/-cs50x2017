# Week 1 Note

## Recap

## Scratch Vs C
```c
int main(void) {
  printf("hello, world\n");
}
```

## Loops
```c
while(true) {
  printf...
}

for (int i = 0l i < 50; i++) {
  printf...
}
```

## Varibles
int
i = 0;

bollean
i < 50, x < y ... etc

## Conditions
```c
if (x < y) {
  peinrf ... 
}
else if (x > y) {
  printf...
}
else {
  printf ...
}
```

## Arrays
argv[0]

## hello, C
```c
# include <stdio.h>

int main(void) {
  printf("hello, world\n");
}
```

## Compiling
translation our code to...
01010010010101001100101010...........

- Compiler

Source code
|
V
Compiler
|
V
Machine code

## The CS50 IDE
clound9.io

## Commandline

## clang
``` bash
~$ clang hello.c
~$ ./a.out // default name
```
``` bash
// name out file 
~$ clang -o hello hello.c
~$ ./hello
```

```
// Make
~$ ls 
a.out* hello* hello.c
~$ rm a.out -y
~$ make hello
```

## Linux Command
cd, ls, mkdir, rm, rmdir ... etc

## The CS50 Library
get_char
get_double
get_float
...

``` c
#include <cs50.h>
#include <stdio.h>

int main(void) {
  string name = get_string(); // from cs50.h library
  printf("hello, %s\n", name);
}

~$ make string
~$ ./string
Gene
hello, Gene
```

## Improving the UX

```
#include <cs50.h>
#include <stdio.h>

int main(void) {
  printf("Name: ")
  string name = get_string(); // from cs50.h library
  printf("hello, %s\n", name);
}
```

## Layering

## get_int
```c
#include <cs50.h>
#include <stdio.h>

int main(void) {
  int i = get_int(); // from cs50.h library
  printf("hello, %d\n", i);
}
```

## adder.c
```
include <cs50.h>
#include <stdio.h>

int main(void) {
  printf("x is: ")
  int x = get_int();
  printf("y is: ")
  int y = get_int();
  
  printf("%i plus %i is %i\n", x, y, x + y);
}
```

## ints.c

```
include <cs50.h>
#include <stdio.h>

int main(void) {
  printf("x is: ")
  int x = get_int();
  printf("y is: ")
  int y = get_int();
  
  printf("%i plus %i is %i\n", x, y, x + y);
  printf("%i minus %i is %i\n", x, y, x - y);
  printf("%i times %i is %i\n", x, y, x * y);
  printf("%i divided %i is %i\n", x, y, x / y); // how to fix it??
  printf("remainder of %i divided by %i is %i\n", x, y, x % y);
}
```

## float.c

```
include <cs50.h>
#include <stdio.h>

int main(void) {
  printf("x is: ")
  float x = get_float();
  printf("y is: ")
  float y = get_float();
  
  printf("%f plus %f is %f\n", x, y, x + y);
  printf("%i minus %f is %f\n", x, y, x - y);
  printf("%f times %f is %f\n", x, y, x * y);
  printf("%f divided %f is %f\n", x, y, x / y); // how to fix it??
  printf("remainder of %f divided by %f is %f\n", x, y, x % y);
}
```

## Data Type

bool
char
double
float
int
long long
string
...etc

## sizeof.c

```c
#include <cs50.h>
#include <stdio.h>

int main(void) {
  printf("bool is %lu\n", sizeof(bool));            // 1
  printf("char is %lu\n", sizeof(char));            // 1
  printf("double is %lu\n", sizeof(double));        // 8
  printf("float is %lu\n", sizeof(float));          // 4
  printf("int is %lu\n", sizeof(int));              // 4
  printf("long long is %lu\n", sizeof(long long));  // 8
  printf("string is %lu\n", sizeof(string));        // 8
}
```

## Memory
is finite, what will happen when it out of memory

## integer overflow
11111111
plus 1
=> 00000000
10000000 but only can get the 8 bit, so become 00000000

overflow.c
```c
#include <cs50.h>
#include <stdio.h>

int main(void) {
  int n = 0;
  while (true) {
    printf ("n is %i\n", n)
    n++;
  }
}
```
```
#include <cs50.h>
#include <stdio.h>

int main(void) {
  int n = 0;
  for (int i = 0; i < 64; i++) {
    printf ("n is %i\n", n) // printf ("n is %lld\n", n) for long long
    n = n * 2;
  }
}

1
2
4
6
8
.
.
.
1073741824
-2147483648  // what happen over there? overflow
0
0
0
0
0
```

## Bugs
The plane model 787 story

## Floating-Point Imprecision

## imprecises.c
```c
#include <cs50.h>
#include <stdio.h>

int main(void) {
  print("%.10f\n", 1.0 / 10.0);
}
// %f => 0.10000
// %.10f => 0.1000000000
// %.55f => 0.10000....555111512...???? what happen?
// computer is finite, so it show us the appx number   
```

## Imprecision in the real world
[Video]

## Varible ReCap
%c
%f
%i
%lu
%ll
%s
...

## Escape Sequences
\a
\n
\r
\t
\'
\"
\\
\0
...

## consition.c
if
else
switch
for
while
do ... while
...

```c
#include <cs50.h>
#include <stdio.h>

int main(void) {
  int i = get_int();
  if (i < 0) {
    printf ("negative\n");
  }
  else if (i > 0) {
    printf("positive\n");
  }
  else {
    printf ("zero\n");
  }
}
```

## logical.c
```c
#include <cs50.h>
#include <stdio.h>

int main(void) {
  int c = get_char();
  
  if (c == 'y' || c == 'Y') {
    printf("yes\n");
  }
  else if (c == 'n' || c == 'N') {
    printf("no\n");
  }
  else {
    printf("error\n");
  }
}
```

## switch.c
```
#include <cs50.h>
#include <stdio.h>

int main(void) {
  int c = get_char();
  
  switch(c) {
    case 'y':
    case 'Y':
      printf("yes\n");
      break;  // let code leave switch, if no break, it will keep execute
    case 'n':
    case 'N':
      printf("no\n");
      break;
    default:
      printf("error\n");
      break;  
  }
```

## prototype.c
```c
#include <cs50.h> h for head
#include <stdio.h>

void print_name(string name);

int main(void) {
  string s = get_string();
  print_name(s);
}

void print_name(string name) {
  printf("hello, %s\n", name);
}
```

## return
```c
#include <cs50.h> h for head
#include <stdio.h>

int square(int n);

int main(void) {
  string x = get_int();
  printf("x^2 is %i", square(x));
}

int square(int n) {
  return n * n;
}
```

## get.c
void function_name
int function_name
string function_name
... etc
define what should we get return

## cough.c
```c
#include <cs50.h> h for head
#include <stdio.h>

void say(string s, int n);
void cough(int n);
void sneese(int n);

int main(void) {
  cough(3);
}

void say(string s, int n) {
  for (int i = 0; i < n; i++) {
    printf("%s\n", s);
  }
}

void cough(int n) {
  say("sough", 3);
}

void sneese(int n) {
  say("sneese", 3);
}
```

## Compling in Detail

1. Preprocessing
Example:
#incluse <cs50.h>
#incluse <stdio.h>
2. Compling
source code => assembly code
```bash
~$ clang -S hello.c
generate assembly code
```
3. Assembling
assembly code => machain code 01010100010
4. Linking
combain all machain code 0101001010100 into hello

## Takeaways
Say something

## Outro
Play Video
