def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answerCase = answer.casefold().strip()
    match answerCase:
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")


main()
