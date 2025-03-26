frutas = ["maçã", "banana", "pera"]

#aplicando alguns métodos
#adiciona "uva" ao fim
frutas.append("uva")
print("append: ", frutas)

#adiciona "laranja" na segunda posição
frutas.insert(1, "laranja")
print("insert: ", frutas)

#remove "maçã"
frutas.remove("maçã")
print("remove: ", frutas)

#removendo a segunda fruta
frutas.pop(1)
print("pop: ", frutas)

#adicionando "abacaxi" ao fim
frutas.append("abacaxi")
print("append: ", frutas)

#ordenando a lista
frutas.sort()
print("sort: ", frutas)

#invertendo a lista
frutas.reverse()
print("reverse: ", frutas)