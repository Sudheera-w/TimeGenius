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