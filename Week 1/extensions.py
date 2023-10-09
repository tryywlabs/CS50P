def main():
    fileName = input("File name: ")
    ext = fileName.rsplit('.', 1)[-1].casefold()

    if ext in ('gif', 'jpg', 'jepg', 'png'):
        print(f"image/{ext}")
    elif ext in ('pdf', 'zip'):
        print(f"application/{ext}")
    elif ext in ("txt"):
        print('text/plain')
    else: print("application.octet-stream")

if __name__ == "__main__":
    main()
