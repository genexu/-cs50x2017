def main():
    id = input("Number: ")
    card_type = get_type(id);
    if card_type != "INVALID":
        isValid = check_sum(id)
        if isValid:
            print(card_type)
        else:
            print("INVALID")
    else:
        print("INVALID")

def check_sum(id):
    sum = 0
    for i in range(len(id) - 1, -1, -1):
        n = int(id[i])
        if i % 2 == 1:
            n *= 2
            if n > 10:
                n = (n % 10) + 1
        sum += n
    return sum % 10 == 0

def get_type(id):
    AMEX_PREFIX = ["34", "37"]
    MASTERCARD_PREFIX = ["51", "52", "53", "54", "55"]
    if id[:1] == "4":
        return "VISA"
    if id[:2] in AMEX_PREFIX:
        return "AMEX"
    if id[:2] in MASTERCARD_PREFIX:
        return "MASTERCARD"
    return "INVALID";

if __name__ == "__main__":
    main()