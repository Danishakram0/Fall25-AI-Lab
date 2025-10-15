print("------------Question no 1------------------")


s = "kuch bhi , kuch bhi  , ; ,', . , . , ] , [ , - , ! , @ , # , $ , % , ^ , & , * ,  ,  , _ , - , + , = , "

for char in s:
    if char.isalpha(): 
        print(char, end=" ")

print("\n------------Question no 2------------------")


s = "me danish"
chars = list(s)

for i in range(len(chars)):
    for j in range(len(chars) - i - 1):
        if chars[j] > chars[j + 1]:
            chars[j], chars[j + 1] = chars[j + 1], chars[j]

sorted_str = "".join(chars)
print("Sorted string is:", sorted_str)

words = s.split()
for i in range(len(words)):
    for j in range(len(words) - i - 1):
        if words[j] > words[j + 1]:
            words[j], words[j + 1] = words[j + 1], words[j]
sorted_words = " ".join(words)
print("Sorted words are:", sorted_words)

print("\n------------Question no 3------------------")



def luhn_check(number):
    number = str(number)[::-1]
    total = 0

    for i, digit in enumerate(number):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return total % 10 == 0


num = "6011111111111117"
if luhn_check(num):
    print(f"{num} is a valid number.")
else:
    print(f"{num} is not a valid number.")
