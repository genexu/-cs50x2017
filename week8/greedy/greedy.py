import cs50
import math

m = -1
ans = 0
while m < 0:
    print("O hai! How much change is owed?")
    m = round(cs50.get_float() * 100)

if m >= 25:
    ans += math.floor(m / 25)
    m %= 25

if m >= 10:
    ans += math.floor(m / 10)
    m %= 10

if m >= 5:
    ans += math.floor(m / 5)
    m %= 5

ans = ans + m;
print(ans)