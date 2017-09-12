#include <stdio.h>
#include <math.h>
#include <cs50.h>

int main(void) {
    int ans = 0;
    int m = -1;
    while(m < 0) {
        printf("How much change is owed? ");
        m = round(get_float() * 100);
    }

    if (m >= 25) {
        ans = ans + m / 25;
        m = m % 25;
    }
    if (m >= 10) {
        ans = ans + m / 10;
        m = m % 10;
    }
    if (m >= 5) {
        ans = ans + m / 5;
        m = m % 5;
    }
    ans = ans + m;
    printf("%i\n", ans);
}