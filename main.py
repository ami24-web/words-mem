words = {
    "кринж" : "Что-то очень странное или стыдное",
    "олд" : "старый",
    "рофл" : "шутка",
    "биас" : "любимый участник"  
}
word = input("какое слово вы хотите перевести")
if word not in words:
    print('я не знаю этого слова')
else: 
    print(words[word])
