'''
print("meow")
print("meow")
print("meow")
'''
'''
i = 3
while i != 0:
    print("meow")
    i = i-1
'''    
'''
i = 0
while i < 3:
    print("meow")
    i = i+1
'''    
'''
i = 0
while i<3:
    print("meow")
    i=i+1
'''
'''
i = 0
while i<3:
    print("meow")
    i+=1
'''
'''
for i in [0,1,2]:
    print("meow")
'''
'''
for i in range(3):
    print("meow")
'''
'''
print("meow"*3)
print("meow\n"*3)
print("meow"*3,end="")
'''
'''
n = int(input('Enter number of time '))

for i in range(n):
    print("meow")
'''
'''
while True:
    n = int(input('Enter number of time '))
    if n > 0:
        break
for _ in range(n):
    print("meow")
'''












def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input('Enter number of time '))    
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()















