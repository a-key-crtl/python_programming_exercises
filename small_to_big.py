

def main():
    numbers = [2,2, 4, 67, 89, 99]
    print(get_smallest(numbers))
    

def get_smallest(numbers):
    if len(numbers) >= 1:
        
        # Variable tracks the smallest value so far, 
        # start off at first value in the list
        smallest = numbers[0]
        
        # Loop through each number in numbers list
        for number in numbers:
            
            # If number smaller than current value, make it
            # new smallest value
            if number <= smallest:
                smallest = number
        
        # Return smallest value found
        return smallest
    
    # If numbers list is empty return None
    else:
        return "None"
        
        
        
if __name__ == "__main__":
    main()