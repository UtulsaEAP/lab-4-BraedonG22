"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Braedon Gehring
Lab Time: Friday, 3:00 pm
"""

def norm():
    x = int(input())
    if x >= 1 :
        v1 = float(input())
    else :
        v1 = False
    if x >= 2 :
        v2 = float(input())
    else :
        v2 = False
    if x >= 3 :
        v3 = float(input())
    else :
        v3 = False
    if x >= 4 :
        v4 = float(input())
    else :
        v4 = False
    if x >= 5 :
        v5 = float(input())
    else :
        v5 = False
    if x >= 6 :
        v6 = float(input())
    else :
        v6 = False
    if x >= 7 :
        v7 = float(input())
    else :
        v7 = False
    if v1>v2 and v1>v3 and v1>v4 and v1>v5 and v1>v6 and v1>v7 :
        print('')
        print(f'{v1/v1:.2f}')
        print(f'{v2/v1:.2f}')
        print(f'{v3/v1:.2f}') 
        print(f'{v4/v1:.2f}')
        print(f'{v5/v1:.2f}')
        print(f'{v6/v1:.2f}')
        print(f'{v7/v1:.2f}')
    elif v2>v1 and v2>v3 and v2>v4 and v2>v5 and v2>v6 and v2>v7:
        print('')
        print(f'{v1/v2:.2f}')
        print(f'{v2/v2:.2f}')
        print(f'{v3/v2:.2f}')
        print(f'{v4/v2:.2f}')
        print(f'{v5/v2:.2f}')
        print(f'{v6/v2:.2f}')
        print(f'{v7/v2:.2f}')
    elif v3>v1 and v3>v2 and v3>v4 and v3>v5 and v3>v6 and v3>v7:
        print('')
        print(f'{v1/v3:.2f}')
        print(f'{v2/v3:.2f}')
        print(f'{v3/v3:.2f}')
        print(f'{v4/v3:.2f}')
        print(f'{v5/v3:.2f}')
        print(f'{v6/v3:.2f}')
        print(f'{v7/v3:.2f}')
    elif v4>v1 and v4>v2 and v4>v3 and v4>v5 and v4>v6 and v4>v7:
        print('')
        print(f'{v1/v4:.2f}')
        print(f'{v2/v4:.2f}')
        print(f'{v3/v4:.2f}')
        print(f'{v4/v4:.2f}')
        print(f'{v5/v4:.2f}')
        print(f'{v6/v4:.2f}')
        print(f'{v7/v4:.2f}')
    elif v5>v1 and v5>v2 and v5>v3 and v5>v4 and v5>v6 and v5>v7 :
        print('')
        print(f'{v1/v5:.2f}')
        print(f'{v2/v5:.2f}')
        print(f'{v3/v5:.2f}')
        print(f'{v4/v5:.2f}')
        print(f'{v5/v5:.2f}')
        print(f'{v6/v5:.2f}')
        print(f'{v7/v5:.2f}')
    elif v6>v1 and v6>v2 and v6>v3 and v6>v4 and v6>v5 and v6>v7 :
        print('')
        print(f'{v1/v6:.2f}')
        print(f'{v2/v6:.2f}')
        print(f'{v3/v6:.2f}')
        print(f'{v4/v6:.2f}')
        print(f'{v5/v6:.2f}')
        print(f'{v6/v6:.2f}')
        print(f'{v7/v6:.2f}')
    elif v7>v1 and v7>v2 and v7>v3 and v7>v4 and v7>v5 and v7>v6 :
        print('')
        print(f'{v1/v7:.2f}')
        print(f'{v2/v7:.2f}')
        print(f'{v3/v7:.2f}')
        print(f'{v4/v7:.2f}')
        print(f'{v5/v7:.2f}')
        print(f'{v6/v7:.2f}')
        print(f'{v7/v7:.2f}')

if __name__ == "__main__":
    norm()