# Calvin's Calorie + Protein Planner
# Log your meals, calories, and protein to stay on track for your goals

# Dictionary to store meals and their info
meal_log = {}

def display_menu():
    print("""
Calorie + Protein Planner
1. Add a meal
2. View all meals
3. Update a meal
4. Delete a meal
5. Get total calories and protein
6. Exit
""")

def add_meal(name, calories, protein): #Adds a meal to the log
    if name in meal_log:
        print(f"'{name}' already exists. Try updating it instead.")
    else:
        meal_log[name] = {'calories': calories, 'protein': protein}
        print(f"Added '{name}' with {calories} cal and {protein}g protein.")

def view_meals(): #Displays all meals logged.
    if meal_log:
        print("\nLogged Meals:")
        for name, info in meal_log.items():
            print(f"- {name.title()}: {info['calories']} cal, {info['protein']}g protein")
    else:
        print("No meals logged yet. Go eat something!")

def update_meal(name, calories, protein): #Updates a meal's nutrition info.
    if name in meal_log:
        meal_log[name] = {'calories': calories, 'protein': protein}
        print(f"Updated '{name}'.")
    else:
        print(f"Meal '{name}' not found. Try adding it first.")

def delete_meal(name): #Deletes a meal from the log.
    if name in meal_log:
        del meal_log[name]
        print(f"Deleted '{name}'.")
    else:
        print(f"'{name}' not found in your meals.")

def get_totals(): #Calculates total calories and protein from all meals.
    total_cal = sum(info['calories'] for info in meal_log.values())  # Reminder you said i can use this. Learned it from Codecademy. Going to submit proof
    total_pro = sum(info['protein'] for info in meal_log.values())
    print(f"\nTotal: {total_cal} calories, {total_pro}g protein")

def is_valid_number(value): #Checks if the input is a valid positive number.
    return value.replace('.', '', 1).isdigit()

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ").strip()

    if choice == '1':
        name = input("Meal name: ").strip().lower()
        cal = input("Calories: ").strip()
        pro = input("Protein (g): ").strip()
        if is_valid_number(cal) and is_valid_number(pro):
            add_meal(name, float(cal), float(pro))
        else:
            print("Please enter valid numbers for calories and protein.")

    elif choice == '2':
        view_meals()

    elif choice == '3':
        name = input("Meal name to update: ").strip().lower()
        cal = input("New calories: ").strip()
        pro = input("New protein (g): ").strip()
        if is_valid_number(cal) and is_valid_number(pro):
            update_meal(name, float(cal), float(pro))
        else:
            print("Invalid input. Try again.")

    elif choice == '4':
        name = input("Meal name to delete: ").strip().lower()
        delete_meal(name)

    elif choice == '5':
        get_totals()

    elif choice == '6':
        print("Stay strong, Calvin! Logging out.")
        break

    else:
        print("Invalid choice. Pick something from 1-6.")
