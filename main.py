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


# ---- PROGRAM ----

def main():
    annual_cost = float(input("Total cost for one year: $"))
    credits = int(input("Credits this semester: "))

    while True:
        print("Cost per semester: 1")
        print("Cost per month: 2")
        print("Cost per day: 3")
        print("Cost per credit: 4")
        print('Cost per class: 5')
        print("Quit: Q")

        choice = input("Choose an option: ")
        if choice == 'Q':
             break
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
        else:
            print("Invalid option")


        


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
