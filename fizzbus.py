'''

Uppgift

Uppgiften går ut på att skriva ut alla tal mellan 1 och 100, ett tal per rad.

Om talet är jämnt delbart med 3 så ska ordet “Fizz” skrivas ut istället för talet.

Om talet är jämnt delbart med 5 så ska ordet “Buzz” skrivas ut istället för talet.

Om talet är jämnt delbart med både 3 och 5 så ska ordet “Fizzbuzz” skrivas ut istället för någonting annat.

'''

def main():


    for n in range(1, 101):

        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)
        




    input()
if __name__ == "__main__":
    main()
