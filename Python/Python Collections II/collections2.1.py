#criando dicionarios e funções

pessoas = {
    "pablo" : 1,
    "carlos" : 2,
    "jose" : 3,
}

pessoas ["pablo"] = 4 #altera o valor da chave

pessoas ["lola"] = 7 #add elemento, se a chave ja constar ele substitui o valor

del pessoas ["lola"] #exclui elemento

#pessoas = "pablo" in pessoas #verifica se a chave ta no dic.

#for pessoa in pessoas:  # passa por cada chave e mostra lista.
 #   print(pessoa)

#for pessoa in pessoas.values():  #mostra a lista de valores.
#    print(pessoa)

#for pessoa in pessoas.items(): #mostra cada item em forma de lista
#    print(pessoa)
