"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Braedon Gehring
Lab Time: Friday, 3:00 pm
"""

def norm():
    task = str("Provide 5 integer values")
    print(task)
    v1 = int(input())
    v2 = int(input())
    v3 = int(input())
    v4 = int(input())
    v5 = int(input())
    if v1>v2 and v1>v3 and v1>v4 and v1>v5 :
        print(f'{v1/v1:.2f}')
        print(f'{v2/v1:.2f}')
        print(f'{v3/v1:.2f}') 
        print(f'{v4/v1:.2f}')
        print(f'{v5/v1:.2f}')
    elif v2>v1 and v2>v3 and v2>v4 and v2>v5 :
        print(f'{v1/v2:.2f}')
        print(f'{v2/v2:.2f}')
        print(f'{v3/v2:.2f}')
        print(f'{v4/v2:.2f}')
        print(f'{v5/v2:.2f}')
    elif v3>v1 and v3>v2 and v3>v4 and v3>v5 :
        print(f'{v1/v3:.2f}')
        print(f'{v2/v3:.2f}')
        print(f'{v3/v3:.2f}')
        print(f'{v4/v3:.2f}')
        print(f'{v5/v3:.2f}')
    elif v4>v1 and v4>v2 and v4>v3 and v4>v5 :
        print(f'{v1/v4:.2f}')
        print(f'{v2/v4:.2f}')
        print(f'{v3/v4:.2f}')
        print(f'{v4/v4:.2f}')
        print(f'{v5/v4:.2f}')
    elif v5>v1 and v5>v2 and v5>v3 and v5>v4 :
        print(f'{v1/v5:.2f}')
        print(f'{v2/v5:.2f}')
        print(f'{v3/v5:.2f}')
        print(f'{v4/v5:.2f}')
        print(f'{v5/v5:.2f}')

if __name__ == "__main__":
    norm()