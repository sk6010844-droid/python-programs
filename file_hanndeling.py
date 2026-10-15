# #exception handling
try:
    a=int(input())
    b=int(input())
    c=a//b
    print(c)
except ZeroDivisionError:
    print("please enter postive number")
except ValueError:
    print("enter integer only")
finally:
    print("java programming")