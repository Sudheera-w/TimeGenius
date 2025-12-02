print("Welcome to TimeGenius!")

module_credits = {}

while True:
    module_name = input("Enter module name (type 'done' to stop) : ")
    if module_name.lower() == 'done':
        break

    while True:
        try:
            credits = int(input(f"Enter credits of {module_name}: "))
            break
        except ValueError:
            print("Please enter a valid number")

    module_credits[module_name] = credits

print("\nModules and credits---------->>>>>>>")
for module,credits in module_credits.items():
    print(f"{module}: {credits}")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
timetable = {day: [] for day in days}  # Reset timetable
daily_load = {day: 0 for day in days}  # To track total hours per day

study_hours = {}

for module, credit in module_credits.items():
    hours = credit * 2  # for 1 credit module, 2 hours
    study_hours[module] = hours

print("\nStudy hours per module (per week):")
for module, hours in study_hours.items():
    print(f"{module}:{hours} hours")

#Ask from user about daily study limit

while True:
    try:
        max_daily_hours = int(input("\nHow many hours can you study per day? (Recommended: 3–4): "))
        break
    except ValueError:
        print("Enter a valid number.")

for module, hours in study_hours.items():
    remaining = hours   # total hours -> to place

    for day in days:
        if remaining <= 0:
            break
        
        available = max_daily_hours - daily_load[day]
        if available > 0:
            hours_to_assign = min(available, remaining)
            timetable[day].append((module, hours_to_assign))
            daily_load[day] += hours_to_assign
            remaining -= hours_to_assign

print("\nWeekly Timetable:")
for day in days:
    print(f"\n{day}:")
    if timetable[day]:
        for module, hrs in timetable[day]:
            print(f"  - {module}: {hrs} hours")
    else:
        print("   No study sessions")
