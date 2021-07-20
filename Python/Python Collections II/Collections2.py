#como cruzar listas (trnasformando listas em sets)

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13,23,56,42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)

assistiram = set(assistiram) #set cria um grupo que "contem" elementos de ambos sem repetir, notação é {}.

print(assistiram)

#como utiizar agrupamento em dois sets direto

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13,23,56,42}

assistiram = usuarios_data_science | usuarios_machine_learning # | representa "ou" ou seja pega os "contem" em um ou outro.

assistiram = usuarios_data_science & usuarios_machine_learning # & representa interesecção apenas de ambos

assistiram = usuarios_data_science - usuarios_machine_learning # - representa interesecção apenas de não contem no primeiro grupo

assistiram = usuarios_data_science ^ usuarios_machine_learning # ^ representa ou exclusivo de contem entre os dois grupos.

usuarios_machine_learning.add(80) # add adiciona elementos.

frozenset(usuarios_machine_learning) #congela o set para impedir adição e deleção de elementos.

print (assistiram)