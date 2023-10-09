def main():
    exp = input("What time is it?: ").strip()
    time = convert(exp)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    time = time.split(":")
    hour = float(time[0])
    minute = float(time[1])/60
    return hour + minute
    # return hour + minute

if __name__ == "__main__":
    main()
