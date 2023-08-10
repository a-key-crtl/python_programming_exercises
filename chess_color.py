# Program determines a pattern to the color of chess squares based on their
# column and row


def main():
    column = int(input("Enter column number 0-7: "))
    row = int(input("Enter row number 0-7: "))
    print(get_square_color(column, row))
    
    

def get_square_color(column, row):
    if column % 2 == 0 and row % 2 == 0:
        return "white"
    elif row % 2 != 0 and column % 2 != 0:
        return "white"
    elif row > 7 or column > 7:
        return ""
    else:
        return "black"
    

if __name__ == "__main__":
    main()