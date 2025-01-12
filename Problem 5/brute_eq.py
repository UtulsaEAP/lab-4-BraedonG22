"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name: Braedon Gehring
Lab Time: Friday, 3:00 pm
"""

def brute_eq():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())

    print(str(a) + 'x + ' + str(b) + 'y = ' + str(c))
    print(str(d) + 'x + ' + str(e) + 'y = ' + str(f))
    seq = range(-10, 10, 1)
    check = False
    for x in seq :
        for y in seq :
            if a*x + b*y == c and d*x + e*y == f :
                check = True
                print("x = " + str(x) + " , y = " + str(y))
    if check == False :
        print('There is no solution')

if __name__ == "__main__":
    brute_eq()