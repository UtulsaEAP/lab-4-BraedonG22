"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Braedon Gehring
Lab Time: Friday, 3:00 pm
"""

def inc_5():
    # Write your code here
    num1 = int(input())
    num2 = int(input())
    sequence = range(num1 , num2 + 1 , 5)
    if num1>num2 :
        print("Second integer can't be less than the first.")
    elif num1 == num2 :
        print(num1)
    else :
        for num in sequence :
            print(f'{str(num)}' , end = ' ' )
        
if __name__ == "__main__":
    inc_5()