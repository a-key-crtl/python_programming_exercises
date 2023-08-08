
def main():
    asc_dict = print_ascii_table()
    
    for number, ascii in asc_dict.items():
        print(number, " ", ascii)
    
    
    
    
    
    
def print_ascii_table():
    asc = {}
    for i in range(32,127):
        asc.update({i: chr(i)})
    return asc
    
    
if __name__ == "__main__":
    main()