def Shiv(Time):
    Time = convert(Time)

    if Time >= 7.0 and Time <= 8.0: 
        return("Breakfast Time")
    elif Time >= 12.0 and Time <= 13.0:
        return("Lunch Time")
    elif Time >= 18.0 and Time <= 19.0:
        return("Dinner Time")
    else:
        return("No time for meal")

def convert(Time):
    hours, minutes = Time.split(":")
    return float(hours) + float(minutes) / 60

print(Shiv(input("What time is it? ")))