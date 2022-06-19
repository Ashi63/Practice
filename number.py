'''
try:
    
    x = int(input("What's x? "))
    print(f" x is {x}")
except ValueError:
    print("x is not a integer")
'''
'''try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not a integer")

print(f" x is {x}")    
'''
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not a integer")
else:
    print(f"x is {x}")

