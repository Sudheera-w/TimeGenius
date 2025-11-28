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

print("Modules and credits---------->>>>>>>")
for module,credits in module_credits.items():
    print(f"{module}: {credits}")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
timetable = {day: [] for day in days}

day_index=0
for module in module_credits:
    timetable[days[day_index]].append(module)
    day_index = (day_index + 1) % len(days)

print("Weekly timetable:")
for day, modules in timetable.items():
    print(f"{day}:{', '.join(modules) if modules else 'No modules assigned'}")