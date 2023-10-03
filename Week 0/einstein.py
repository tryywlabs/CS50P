def main():
    m = int(input("m: "))
    energyConvert = convert(m)
    print("E: ", energyConvert)

def convert(m):
    c = 300000000
    e = m * (c ** 2)
    return e

main()
