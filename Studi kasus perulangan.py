t=5
for i in range (1, t+1):
    print (((t-i+11)*" ")+(i * "*")+((i-1) * "*"))
for i in range (1, t+1):
    print (((i * " ")+(t-i+20)*"*")+((t-i)*"*"))
for i in range (t+1):
    print ((((t-i) * " ")+(t-i+4)*"*")+((i) * " ")+((i+1) * " ")+((t+4+i)*"*"))
