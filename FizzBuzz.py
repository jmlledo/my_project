# Escribir por pantalla Fizz si es múltiplo de 3, Buzz si es múltipolo de 5 y FizzBuzz
# si es múltiplo de 3 y de 5
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)
