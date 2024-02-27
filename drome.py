def find_palindrome(number):
    num_str = str(number)
    reverse_num_str = num_str[::-1]

    if num_str == reverse_num_str:
        return int(num_str)
    return int(reverse_num_str + num_str)
number = int(input("Whats your number:"))
palindrome = find_palindrome(number)
print = ("Palindrome", number, "is:",palindrome)