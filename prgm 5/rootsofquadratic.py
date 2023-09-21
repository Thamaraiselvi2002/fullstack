[2:00 pm, 21/09/2023] CT: # of a quadratic equation
import math
 
# Prints roots of quadratic equation
# ax*2 + bx + x
def findRoots(a, b, c):
 
    # If a is 0, then equation is
    # not quadratic, but linear
    if a == 0:
        print("Invalid")
        return -1
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))
 
    if d > 0:
        print("Roots are real and different ")
        print((-b + sqrt_val)/(2 * a))
        print((-b - sqrt_val)/(2 * a))
    elif d == 0:
        print("Roots are real and same")
        print(-b / (2*a))
    else:  # d<0
        print("Roots are complex")
        print(- b / (2*a), " + i", sqrt_val / (2 * a))
        print(- b / (2*a), " - i", sqrt_val / (2 * a))
 
 
# Driver Program
if _name_ == '__main__':
    a = 1
    b = -7
    c = 12
     
    # Function call
    findRoots(a, b, c)
 
# This code is contributed by Sharad Bhardwaj.
[2:00 pm, 21/09/2023] CT: Start
Read the values of a, b, c
Compute d = b2 – 4ac
If d > 0
    calculate root1 = {-b + √(b2 – 4ac)}/2a
    calculate root2 = {-b – √(b2 – 4ac)}/2a
else If d = 0
    calculate root1 = root2 = (-b/2a)
else
    calculate root1 = {-b + i√-(b2 – 4ac)}/2a
    calculate root2 = {-b + i√-(b2 – 4ac)}/2a
print root1 and root2
End