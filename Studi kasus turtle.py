import turtle

t = turtle.Turtle()
s = turtle.Screen()
    
print("1. Gambar Persegi")
print("2. Gambar Lingkaran")

a = int(input("pilih opsi : "))

if a == 1 :
    t = turtle.Turtle()
    s = turtle.Screen()

    def draw_square(length):
        for i in range(0,4):
            t.forward(length)
            t.right(90)

    draw_square(100)

elif a == 2 :
    t = turtle.Turtle()
    s = turtle.Screen()

    t.circle(60)

    s.exitonclick
else :
    print("tidak valid")
