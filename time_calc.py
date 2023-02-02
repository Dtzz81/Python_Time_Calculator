def add_time(start, duration, day = None):

    #current time

    time = start.split(" ")[0]
    mer = start.split(" ")[1]
    h = time.split(":")[0]
    m = time.split(":")[1]

    current_time = h + ":" + m + mer

    # what we are adding


    h_added = duration.split(":")[0]
    m_added = duration.split(":")[1]

    # new time
    new_h = int(h) + int(h_added)
    new_m = int(m) + int(m_added)

    #n days later
    n = 0

    #hour and min adjustement

    if new_m > 59:
        new_m -= 60
        new_h += 1

    while new_h > 11:
        new_h -= 12

        if mer == "AM":
            mer = mer.replace("AM", "PM")
        elif mer == "PM":
            mer = mer.replace("PM", "AM")
            n = int(n) + 1
    while new_h == 0 and mer == "PM":
        new_h = 12
    while new_h == 0 and mer == "AM":
        new_h = 12

    #adding days in the week:

    days_of_week = { "monday" : 0,
        "tuesday" : 1,
        "wednesday" : 2,
        "thursday" : 3,
        "friday" : 4,
        "saturday" : 5,
        "sunday" : 6}

    if day:
        value = (days_of_week[day.lower()])
        day_value = int(value + n) % 7
        for k, v in days_of_week.items():
            if v == day_value:
                new_day = k


    #Finishing:
        if n == 1:
            n = "next day"
            new_time = str(new_h) + ":" + f"{new_m:02}" + " " + mer + ", " + str(new_day.capitalize()) + " (" + str(n) + ")"
        elif n == 0:

                new_time = str(new_h) + ":" + f"{new_m:02}" + " " + mer + ", " + str(new_day.capitalize())
        else:

            new_time = str(new_h) + ":" + f"{new_m:02}" + " " + mer + ", " + str(new_day.capitalize()) + " (" + str(n) + " "+ "days later" + ")"

    #without a day
    else:
        if n == 1:
            n = "next day"
            new_time = str(new_h) + ":" + f"{new_m:02}" + " " + mer + " (" + str(n) + ")"
        elif n == 0:

                new_time = str(new_h) + ":" + f"{new_m:02}" + " " + mer
        else:

            new_time = str(new_h) + ":" + f"{new_m:02}" + " " + mer + " (" + str(n) + " "+ "days later" + ")"


    return new_time
