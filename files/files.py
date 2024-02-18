with open("files/books.txt") as books:
    for line in books:
        line=line.strip()
        print(line)