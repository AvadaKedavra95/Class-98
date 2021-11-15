def count_words_from_file():
    file_name=input("enter the file name : ")
    file=open(file_name,'r')
    text=(file.read())
    word_count=0
    words=text.split()
    for word in words:
        word_count+=1       
    print(word_count)
count_words_from_file()