''''Write a Python program to solve quadratic equation?'''

''' formula : x = [-b ± √(b² - 4ac)] / 2a.
  discriminant = b² - 4ac

#properties
If b² - 4ac is positive (>0), there are two distinct real solutions. 
If b² - 4ac is zero (=0), there is one real solution (a repeated root). 
If b² - 4ac is negative (<0), there are two complex solutions. '''


a=int(input("enter the cofficient of x:  "))
b=int(input("enter the cofficient of y:  "))
c=int(input("enter the constant :  "))

discriminant = (b**2)-(4*a*c)
print(f"discriminant is {discriminant}")

quadratic_equation1 = -b+(discriminant*0.5)/2*a
print(quadratic_equation1)

quadratic_equation2 = -b-(discriminant*0.5)/2*a
print(quadratic_equation2)
