def main():
    text = input()
    res = convert(text)
    print(res)

def convert(text):
    text2 = text.replace(":)", "🙂").replace(":(", "🙁")
    return text2

main()
