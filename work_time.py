def map_minutes(minutes):
    if minutes == "08":
        minutes = "05"
    elif minutes == "16":
        minutes = "10"
    elif minutes == "25":
        minutes = "15"
    elif minutes == "33":
        minutes = "20"
    elif minutes == "41":
        minutes = "25"
    elif minutes == "05":
        minutes = "30"
    elif minutes == "58":
        minutes = "35"
    elif minutes == "66":
        minutes = "40"
    elif minutes == "75":
        minutes = "45"
    elif minutes == "83":
        minutes = "50"
    elif minutes == "91":
        minutes = "55"
    return(minutes)


def map_hours_name(hours):
    hours_name_collection = ["часов", "час", "часа"]
    if hours in {"0", "5", "6", "7", "8"}:
        hours_name = hours_name_collection[0]
    if hours == "1":
        hours_name = hours_name_collection[1]
    if hours in {"2", "3", "4"}:
        hours_name = hours_name_collection[2]
    return(hours_name)


try:
    time_work = int(input("Введите количество минут: "))
except ValueError:
    print("Введено не верное значение")
    quit()
if time_work >= 60:
    time_work_split = str(time_work/60).split(".")
    hours = time_work_split[0]
    hours_name = map_hours_name(hours)
    minutes = time_work_split[1]
    minutes = map_minutes(minutes[0:2])
    print(hours + " " + hours_name, minutes + " минут")
else:
    print("0 часов " + str(time_work) + " минут")
