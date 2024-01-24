with open('const/wordslistUnique.txt', encoding='utf-8') as file:
    words = file.readlines()
    words = [word.strip() for word in words]
    words = [word for word in words if len(word) > 1]

with open('const/korean_word.txt', "w",encoding='utf-8') as file:
    for word in words:
        file.write(word + '\n')   
