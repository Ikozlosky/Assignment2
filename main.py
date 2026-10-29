"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45
INSTRUCTIONAL_WEEKS_PER_SEMESTER = 15


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (CLASS_DAYS_PER_SEMESTER * 2)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return (annual_cost / 2) / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return (annual_cost / 2) / 45 * ((CS1430_CREDITS/credits))

def value_calc(value_score):
    return  (8.0*(1.65 ** value_score)) - 25.0

def is_it_worth(annual_cost, classes_total):
    skipped = int(input("How many classes Will be missed? "))
    cost_of_event = input('How much does this event cost? $')
    value_score = input('On a scale of 1-10, how badly do you want to attend this event? ')
    cost_total = ((skipped / classes_total) * (annual_cost / 2)) + int(cost_of_event)
    event_value = value_calc(int(value_score))
    print(f"Your total event cost will be: ${cost_total:.2f}")
    print(f"Your percieved event value will be: ${event_value:.2f}")
    if cost_total -20 <= event_value and  event_value <= cost_total + 20:
        print("Values are similiar, the choice is up to you.")
    elif event_value >= cost_total:
            print("The event is worth it! you should go!")
    elif event_value <= cost_total:
            print("Event is expensive, not worth the cost.")
    
   



# ---- PROGRAM ----

def main():
    annual_cost = float(input("Total cost for one year: $"))
    credits = int(input("Credits this semester: "))
    classes_total = int(input("How many classes per week? (two hour labs/lectures count as two) ")) * INSTRUCTIONAL_WEEKS_PER_SEMESTER

    while True:
        print("Cost per semester: 1")
        print("Cost per month: 2")
        print("Cost per day: 3")
        print("Cost per credit: 4")
        print('Cost per class: 5')
        print("Quit: Q")
        print('Is it worth it?: 6')
      

        choice = input("Choose an option: ")
    
        if choice == '1':
            print(f"One semester costs: ${cost_per_semester(annual_cost):.2f}")
        if choice == '2':
            print(f"One month costs: ${cost_per_month(annual_cost):.2f}")
        if choice == '3':
            print(f"One class day costs: ${cost_per_day(annual_cost):.2f}")
        if choice == '4':
            print(f"One credit costs: ${cost_per_credit(annual_cost, credits):.2f}")
        if choice == '5':
            print(f"One class costs: ${cost_per_class(annual_cost, credits):.2f}")
        if choice == 'Q':
                     break
        if choice == '6':
            is_it_worth(annual_cost, classes_total)
        else:
            print("Invalid option")


        


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
