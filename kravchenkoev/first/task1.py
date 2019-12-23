"""
Вивести слова, які мястять хоча б одну велику букву
"""

text = str(input("Введите текст: "))
words = text.split()
i=0
big_words=[None]*len(words)
for word in words:
    for letter in word:
        if letter.isupper() == True:
            big_words[i] = str (word)
            i+=1
            break
print(big_words)
