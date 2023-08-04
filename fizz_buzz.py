"""
    Fizz buzz is a word game you can implement as a simple program. 
    It became famous as a screening question in coding interviews 
    to quickly determine if candidates had any programming ability 
    whatsoever, so being able to solve it quickly leads to a good first impression.
    This exercise continues our use of the modulo operator to 
    determine if numbers are divisible by 3, 5, or both 3 and 5.
"""




def main():
    number = int(input("Enter a number greater than two: "))
    print(fizz_buzz(number))
    
    
    
    
def fizz_buzz(up_to):
    word = ""
    for i in range(1, up_to + 1):
        if i % 3 == 0 and i % 5 == 0:
            word = word + " " + "FizzBuzz"
        elif i % 3 == 0:
            word = word + " " + "Fizz"
        elif i % 5 == 0:
            word = word + " " + "Buzz"
        else:
            word = word + " " + str(i) 
    return f"{word}"
    




if __name__ == "__main__":
    main()