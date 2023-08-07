

def main():
    number = input("Enter a natural number: ")
    print(ordinal_suffix(str(number)))
    
    
    
    
def ordinal_suffix(n):
             
    if n[-2:] in ("11", "12", "13"): 
        return n + "th"
    elif n[-1:] == "1":
        return n + "st"
    elif n[-1:] == "2":
        return n + "nd"
    elif n[-1:] == "3":
        return n + "rd"
    else:
        return n + "th"
    
    



if __name__ == "__main__":
    main()