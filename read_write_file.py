

def main():
    write_to_file('greet.txt', 'Hello!\n')
    append_to_file('greet.txt', 'Goodbye!\n')
    assert read_from_file('greet.txt') == 'Hello!\nGoodbye!\n'
    
    
    
    
def write_to_file(name, text):
    # Open file in write mode:
    with open(name, "w") as file:
        # Write text to the file:
        file.write(text)
    
    

def append_to_file(name, text):
    # Open file in append mode:
    with open(name, "a") as file:
        # Write text to end of file:
        file.write(text)
    
    


def read_from_file(name):
    # Open file in read mode:
    with open(name) as file:
        return file.read()
        
    
    


if __name__ == "__main__":
    main()