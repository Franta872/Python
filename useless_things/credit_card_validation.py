# It checks if a credit card number is valid or not

def card_check(credit_card: str):
    #step 1 – removes spaces and dashes
    clear_credit_card = credit_card.replace("-", "").replace(" ", "")

    #step 2 – sum of all digits in the odd places from right to left
    sum_odd_digits = 0
    for odd_num in clear_credit_card[1::2]: # já jsem to dělal pomocí range, ale toto je lepší
        sum_odd_digits += int(odd_num)

    #step 3 – Double every second digit from right to left (if result is a two digit number, add then together to get a single number)
    sum_even_digits = 0
    for even_num in clear_credit_card[::2]: # tady taky range, ale změnil jsem to
        num = int(even_num)*2
        if num > 9:
            sum_even_digits += int(str(num)[0]) + int(str(num)[1]) # 1 + (num % 10) <-- beter solution, but I'll keep the mine
        else:
            sum_even_digits += num

    #step 4 – sums the total of steps 2 and 3
    even_and_odd = sum_even_digits + sum_odd_digits

    #step 5 – If the sum is divisible by 10, the credit card number is valid
    if even_and_odd % 10 == 0:
        return "VALID"
    else:
        return "INVALID"



if __name__ == "__main__":
    print(card_check("4242424242424242"))

# Visa              4242424242424242
# Mastercard        5555555555554444
# American Express  378282246310005
# Discover          6011111111111117