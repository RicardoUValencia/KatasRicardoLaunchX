text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C.""".split(".")
 
print(text) # Imprime el texto

#Buscar una palabra en una cadena
palabras_hechos = ['average','temperature','distance']

#Ciclo for para buscar palabras en la cadena
for palabra in palabras_hechos:
    print(palabra, ":", text.count(palabra))

#Ciclo for actualizado para remplazar palabras en la cadena
for texto in text:
    print(texto.replace("C","Celsius"))