def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    omitDollarSign = d.replace("$", "")
    return float(omitDollarSign)


def percent_to_float(p):
    omitPercentSign = p.replace("%", "")
    return float(omitPercentSign)/100

main()
