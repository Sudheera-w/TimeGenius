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

daily_hours = {}

for module, hours in study_hours.items():
    daily_hours[module] = hours  # same as weekly (for now)

print("\nDaily study hours:")
for module, hours in daily_hours.items():
    print(f"{module}: {hours} hours on assigned day")


print("\nWeekly timetable:")
for day, modules in timetable.items():
    if modules:
        for m in modules:
            print(f"{day}: {m} ({daily_hours[m]} hours)")
    else:
        print(f"{day}: No modules assigned")
