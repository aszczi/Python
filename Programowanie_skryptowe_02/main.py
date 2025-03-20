def writeToFile():
    text = input("Podaj tekst")
    with open("plik.txt", "w") as file:
        file.write(text)
    file = open("plik.bin", "wb")
    binary_text = text.encode("utf-8")
    file.write(binary_text)
    file.close()

if __name__ == "__main__":
    writeToFile()