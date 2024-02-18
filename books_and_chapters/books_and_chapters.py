max_chapter=int(0)
max_bom_book=''
bom_books=[]
largest_chapters=int(0)
largest_book=''
which_volume=input('Which volume of scriptures would you like to learn about? ').title()
which_chapter=int(0)
which_book=''

with open("books_and_chapters/books_and_chapters.txt") as scriptures:
    for line in scriptures:
        data=line.strip()
        data=data.split(':')
        book=data[0]
        chapter=int(data[1])
        scripture=data[2]
        which_scripture=scripture.title()
        # print(data)
        # print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapter}')
        if chapter>largest_chapters:
            largest_chapters=chapter
            largest_book=book
        if scripture=='Book of Mormon':
            bom_books.append(book)
            if chapter>max_chapter:
                max_chapter=chapter
                max_bom_book=book
        if which_volume==which_scripture:
            if chapter>which_chapter:
                which_chapter=chapter
                which_book=book
    for book in bom_books:
         print(book)
    print()
    print(f'The book with the largest number of chapters in the scriptures is {largest_book} with {largest_chapters} chapters.')
    print()
    print(f'The book in the Book of Mormon with the largest number of chapters is the book of {max_bom_book} with {max_chapter} chapters.')
    print()
    print(f'The largest book in the {which_volume} is {which_book} with {which_chapter} chapters.')