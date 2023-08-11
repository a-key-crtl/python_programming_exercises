# Program converts number of seconds into a string 
# with the number of hours, minutes, and seconds


def main():
    seconds = int(input("Enter number of seconds: "))
    print(get_hours_minutes_seconds(seconds))
    
    
    
    
def get_hours_minutes_seconds(total_seconds):
    # If total seconds is 0, return "0s"
    if total_seconds == 0:
        return "0s"
    
    hours = 0
    while total_seconds >= 3600:
        hours += 1
        total_seconds -= 3600
    
    minutes = 0
    while total_seconds >= 60:
        minutes += 1
        total_seconds -= 60
        
    seconds = total_seconds
    
    hms = []
    
    if hours > 0:
        hms.append(str(hours) + "h")
    if minutes > 0:
        hms.append(str(minutes) + "m")
    if seconds > 0:
        hms.append(str(seconds) + "s")
    
    return " ".join(hms)

if __name__ == "__main__":
    main()    
