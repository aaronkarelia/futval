#futval.py
#  A program to compute thevalue of an investment
#  carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a multi-year investment.")

    principal = eval(input("Enter the yearly investment: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years of the investment: "))

    for i in range(years):
        principal = principal + (principal * (1 + apr))

    print("The value in", years, "years is:", principal)

main()
