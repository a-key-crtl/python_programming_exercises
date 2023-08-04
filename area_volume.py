
def main():
    
    choice = input("Choose: area, perimeter, volume, surface area: ").strip()
    match choice.lower():
        case "area":
            length = float(input("Length: "))
            width = float(input("Width: "))    
            print(round(area(length, width), 2))
        case "perimeter":
            length = float(input("Length: "))
            width = float(input("Width: "))
            print(round(perimeter(length, width), 2))
        case "volume":
            length = float(input("Length: "))
            width = float(input("Width: "))
            height = float(input("Enter height: "))
            print(round(volume(length, width, height), 2))
        case "surface area":
            length = float(input("Length: "))
            width = float(input("Width: "))
            height = float(input("Enter height: "))
            print(round(surface_area(length, width, height), 2))
            
    
    
    
def area(length, width):
    return length*width
    
def perimeter(length, width):
    return 2*length + 2*width
    
def volume(length, width, height):
    return length * width * height
    
def surface_area(length, width, height):
    return (length * width * 2) + (length * height * 2) + (width * height * 2)
    
    
if __name__ == "__main__":
    main()