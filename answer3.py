def split(number, text):
    if number >= len(text):
        print(text)
    elif text[number] != " ":
        for j in range(number, 0, -1):
            if j == 1:
                for i in range(len(text)):
                    if text[i] == " " or i == len(text):
                        print(text[:i])
                        # print("the word is too long than your index")
                        return split(number, text[i + 1:])
            if text[j] == " ":
                print(text[:j])
                text = text[j + 1:]
                return split(number, text)

    else:
        print(text[:number])
        text = text[number + 1:]
        return split(number, text)


if __name__ == "__main__":
    text = "this is a text"
    number = 12
    split(number, text)