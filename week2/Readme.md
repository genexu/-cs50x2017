# Week 2 Note

## Week1 Review
review week 1

## Debuggubg
How to debug your code?

## buggy0
```c
int main(void) {
  printf("hello, world\n");
}
```
```
~$ make buggy0
show some error message
```
So, first, understand your error message.  
=> In this case, include head libery stdio
```c
#include <stdio.h>
```
Node: help50 can help you in cs50 IDE

## buggy1
 ```c
 #include <stdio.h>
 
 int main(void){
  string s = get_string();
  printf("hello, %s", s);
 }
 ```
 ```
 ~$ make buggy1
 show some error mesage
 ```
 => In this case, include cs50 head libery
 ```c
#include <cs50.h>
 ```

## buggy2
```c
#include <stdio.h>
 
int main(void) {
  for (int 1 = 0; i<= 10; i++) {
    printf("#\n");
  }
}
```

```bash
~$ make buggy2
no error show, compling success
~$ ./buggy2
show 11 #
```
```c
eprintf("i is now %i\n", i);
```
Note: eprintf help you whoe debug error message

## buggy3
```c
#include <stdio.h>
#include <cs50.h>

int get_negative_int(void)

int main(void) {
  int i = get_nagative_int();
  printf("%i is a nagative integer\n", i);
}

int get_negative_int(void) {
  int n;
  do {
    n = get_int();
  } while(n>0);
  return n;
}
```
```bash
~$ make buggy3
~$ ./buggy3
```bash


## debug50
help you debug line by line
!!!put stop point on IDE!!!
```
~$ debug50 ./buggy3
```

## Rubber-Duck Debugging
working you self through your code, and ask you self what happen, what your code working.

## Problem Sets Overview
- scope
- correctness
- design
- style

1    2    3    4      5
poor fair good better best

scope x (correctness x 3 + design x 2 + style x 1)

## Academic Honesty
show some chart and staticate

'Be reseanable'
'The essence of all work that you submit to this course must be your own'
'...when asking for help, you may show your code to others, but you may not view thiers'

## Puppies
[Video Time]

## Cryptography
ex: a => b , b => c ...

## Ralphie
[Video]
encode <=> decode

## Secret-Key Cryptography
Inputs -> ... -> Outputs
```
key ->        |---|
planittext -> |   | -> ciphertext
              |---|
             
             
              |---| <- key
planittext <- |   | <- ciphertext
              |---|
```

## Strings
```
-------------------------
| Z | a | m | y | l | a |
-------------------------
```
## string0
```c
#include <stdio.h>
#include <string.h>
#include <cs50.h>

int main(void) {
  string s = get_string();
  if (s != NULL) {
    for (int i = 0; i < strlen(s); i++) {
      printf("%c\n", s[i]);
    }
  }
}
```

## string1
```c
#include <stdio.h>
#include <string.h>
#include <cs50.h>

int main(void) {
  // make sure get string returned string
  string s = get_string();
  if (s != NULL) {
    for (int i = 0, n = strlen(s); i < n; i++) { // better design for performence
      printf("%c\n", s[i]);
    }
  }
}
```
Note: use comment to let other understand your code easierly

## typecasting
ASCII
A  B  C
65 66 67 ... 

a  b  c
97 98 99 ...

## ascii0
```c
#include <stdio.h>

int main(void) {
  for (int i = 65; i < 91; i++) { // 91 = 65 + 26
    printf("%c is %i\n", (char)i, i)
    // printf("%c is %i\n", i, i) also good, c will auto trans it
  }
}
```

## ascii1
```c
#include <stdio.h>

int main(void) {
  for (char c = 'A'; c < 'Z'; c++) { // 91 = 65 + 26
    printf("%c is %i\n", c, (int)c)
  }
}
```

## capitalize0
#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void) {
  string s = get_string();
  if (s != NULL) {
    for (int i = 0, n = strlen(s); i < n; i++) {
      if (s[i] >= 'a' && s[i] <= 'z') {
        printf("%c", s[i] - 32);
      }
      else {
        printf("%c", s[i]);
      }
    }
    printf("\n");
  }
}

## capitalize2
```c
#include <stdio.h>
#include <cs50.h>
#include <cypto.h>
#include <string.h>

int main(void) {
  string s = get_string();
  if (s != NULL) {
    for (int i = 0, n = strlen(s); i < n; i++) {
      printf("%c\n", toupper(s[i]));
    }
  }
}
```

```
~$ man toupper
```

## strlen.c
```c
#include <stdio.h>
#include <cs50.h>

int main(void) {
  string s = get_string();
  int n = 0;
  while (s[n] != '\0') {
    n++;
  }
}
```

## more on strings
man
reference.cs50.net

!!! \0 !!!
help computer know where to begain in memery

## more on strlen
About \0
https://stackoverflow.com/questions/16955936/string-termination-char-c-0-vs-char-c-0

## Command-Line Arguments
```c
int main (int argc, string argv[])
```

## argv0
```c
#include <stdio.h>
#include <cs50.h>

int main (int argc, string argv[]) {
  if (argc == 2) {
    printf("hello, %s\n", argv[1]);
  }
  else {
    printf("hello, world\n");
  }
}
```
```
~$ ./argv0
hello, world
~$ ./argv0 Gene
hello, Gene
```
```
!!! argc vs argv !!!
--Argv----------------------
| --Argc-----  --Argc----- |
| |A|B|C|\0 |  |A|B|C|\0 | |
| -----------  ----------- |
|---------------------------
```

## argv1
#include <stdio.h>
#include <cs50.h>

int main (int argc, string argv[]) {
  for (int i = 0; i < argc; i++) {
    printf("%s\n", argv[i]);
  }
}
## argv2
```c
#include <stdio.h>
#include <string.h>
#include <cs50.h>

int main (int argc, string argv[]) {
  for (int i = 0; i < argc; i++) {
    for (int j =0, n = strlen(argv[i]); j < n; j++) {
      printf("%s\n", argv[i][j]);
    }
  }
}
```

## exit
```c
#include <stdio.h>
#include <cs50.h>

int main (int argc, string argv[]) {
  if (argc != 2) {
    printf('missing command line argument\n');
    return 1;
  }
  printf("hello, %s\n", argv[1]);
  reutrn 0;
}
```
```bash
~$ ./exit $? // get reutrn value 
```

## Array in Summery
```
----------------------
|  |  |  |  |  |  |  |
----------------------
```

## Outro
[Video]
