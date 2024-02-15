"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Braedon Gehring
Lab Time: Friday, 3:00 pm
"""


def reverse_binary():
    user_num = int(input("Please provide a positive integer: "))
    # YOUR CODE HERE
    x = user_num
    while x > 0 :
        remainder = x % 2
        print(f'{str(remainder)}' , end = '')
        x = int(x / 2)

if __name__ == "__main__":
    reverse_binary()