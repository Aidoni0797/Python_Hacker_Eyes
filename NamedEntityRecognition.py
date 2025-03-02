import spacy

# Загружаем уже обученную модель
nlp = spacy.load("en_core_web_sm")

# Даем ей текст
text = "Aidana was born in 1997 in Kazakhstan."
doc = nlp(text)

# Выводим, какие слова модель нашла
for ent in doc.ents:
    print(ent.text, ent.label_)

#Heh iDONi, ты это понимаешь, прикольно


