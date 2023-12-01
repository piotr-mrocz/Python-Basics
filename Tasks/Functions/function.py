def convertToSecond(hours, minutes):
    seconds = hours * 60 * 60
    seconds += minutes * 60

    print(f"Seconds: {seconds}")


convertToSecond(3, 25)
print()

def convertToHours(minutes):
    hours = minutes / 60

    print(f"Hours: {hours}")


convertToHours(120)