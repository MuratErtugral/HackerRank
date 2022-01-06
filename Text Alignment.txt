thickness = int(input())
m = 'H'

for i in range(thickness):
    print((m*i).rjust(thickness-1)+m+(m*i).ljust(thickness-1))

for i in range(thickness+1):
    print((m*thickness).center(thickness*2)+(m*thickness).center(thickness*6))

for i in range((thickness+1)//2):
    print((m*thickness*5).center(thickness*6))    

for i in range(thickness+1):
    print((m*thickness).center(thickness*2)+(m*thickness).center(thickness*6))    

for i in range(thickness):
    print(((m*(thickness-i-1)).rjust(thickness)+m+(m*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
