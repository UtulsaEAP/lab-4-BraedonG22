"""
Complete the following python code to reverse the string entered by the user.

Name: Braedon Gehring
Lab Time: Friday, 3:00 pm
"""

def reverse_string():
    # YOUR CODE HERE
    word1 = input()
    word2 = input()
    word3 = input()
    if word1 == 'Done' :
        print(" ")
    elif word1 == 'done' :
        print(' ')
    elif word1 == 'd' :
        print(' ')
    else :
        rvrs =  word1[::-1]
        print(rvrs)
    if word2 == 'Done' :
        print(" ")
    elif word2 == 'done' :
        print(' ')
    elif word2 == 'd' :
        print(' ')
    else :
        rvrs2 = word2[::-1]
        print(rvrs2)
    if word3 == 'Done' :
        print(" ")
    elif word3 == 'done' :
        print(' ')
    elif word3 == 'd' :
        print(' ')
    else :
        rvrs3 = word3[::-1]
        print(rvrs3)
if __name__ == "__main__":
    reverse_string()