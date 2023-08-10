

def main():
    text = input("Please enter text:")
    old_text = input("Enter word to replace: ")
    new_text = input("Enter new word: ")
    print(find_and_replace(text, old_text, new_text))
    
    

def find_and_replace(text, old_text, new_text):
    word = ""
    i = 0
    while i < len(text):
        if text[i:i + len(old_text)] == old_text:
            word += new_text
            i += len(old_text)
        else:
            word += text[i]
            i += 1
    return word        
            
    
    

if __name__ == "__main__":
    main()