__author__ = 'Trenton Sanders'
"""
Given a year as an input, generates a calendar for that year
"""

def main():
    month_dict = {  # Probably a way to import these from somewhere rather than hardcoding it
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    """Receive input, check for leap year, find starting day"""
    year = input("What year would you like to see? ")
    cal_file = open("calendar" + year, 'w') #Will create if it doesn't exist, overwrite if it does
    if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0):
        month_dict["February"] = 29
    start = start_date(int(year))

    """Print calendar"""
    for m in month_list:
        cal_file.write((m + " " + year).center(27,' ') + "\n") #27 is the number of characters in the Sunday-Saturday line
        cal_file.write("SUN MON TUE WED THU FRI SAT\n")
        start = print_month(start, month_dict[m], cal_file)
        cal_file.write("\n")
    cal_file.close()

def start_date(x):
    """Given a year x, returns the day of January 1st of that year
    0= Sunday, 6 = Saturday"""
    day = x
    day += int((x-1)/4) # Annoyingly, Python 3 auto-casts this division as a double
    day -= int((x-1)/100)
    day += int((x-1)/400)
    return day % 7

def print_month(start, days, f):
    """Given a starting day (0-6, sun-sat), the days of a month, and a file for writing,
    writes the numerical dates for that month in the file"""
    s = ""
    for i in range(0, start):
        s+=" ".rjust(4)
    for d in range(1,days+1):
        s += (str(d).rjust(3) + " ")
        start += 1
        if start > 6:
            f.write(s + "\n")
            start = 0
            s = ""
    if start != 0:
        f.write(s + "\n")
    return start

if __name__ == "__main__":
    main()