#include <stdio.h>
#include <math.h>
#include <string.h>
#include <cs50.h>

bool check_sum(long long id);
char* get_type(long long id);

int main(void) {
    printf("Number: ");
    long long id = get_long_long();
    char* type = get_type(id);

    if(strcmp(type, "INVALID") != 0) {
        bool isValid = check_sum(id);
        if (isValid) {
            printf("%s\n", type);
        }
    }
    else {
        printf("INVALID\n");
    }
}

bool check_sum(long long id) {
    int size = log10(id) + 1;
    long long x = 10;
    int sum = 0;

    for (int i = 0; i < size; i++) {
        int n = 0;
        if (i == 0) {
            n = (id % x);
        }
        else {
            n = (id % x) / (x / 10);
        }
        if (i % 2 == 1) {
            n = n * 2;
            if (n >= 10) {
                n = (n % 10) + 1;
            }
        }
        sum = sum + n;
        x = x * 10;
    }
    return sum % 10 == 0;
}

char* get_type(long long id) {
    int size = log10(id) + 1;
    int typeNumber = id / pow(10, size - 2);
    if ((typeNumber / 10) == 4) {
        return "VISA";
    }
    switch (typeNumber) {
        case 34:
        case 37:
            return "AMEX";
        case 51:
        case 52:
        case 53:
        case 54:
        case 55:
            return "MASTERCARD";
    }
    return "INVALID";
}