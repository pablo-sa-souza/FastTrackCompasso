#!/bin/bash

if [ ! -d log ]							#verifica se existe o diretorio log
then			
	mkdir log							#cria se não houver
fi

processos_memoria(){							#cria função processos_memoria()
processos=$(ps -e -o pid --sort -size | head -n 11 | grep [0-9])	#cria variavel processos com a lista de processos.
for pid in $processos							#cria variavel pid em processos
do 
	nome_processo=$(ps -p $pid -o comm= | sed s/' '/'_'/g)	#cria a variavel nome_processo utilizando a variavel pid para puxar o nome
	echo -n $(date +%F,%H,%M,%S, ) >> log/$nome_processo.log	#imprime a data e hora no arquivo log
	tamanho_processo=$(ps -p $pid -o size | grep [0-9])		#cria a variavel tamanho_processo com os dados.
	echo "$(bc <<< "scale=2;$tamanho_processo/1024") MB" >> log/$nome_processo.log	#imprime o tamanho do processo no log
done
}

processos_memoria
if [ $? -eq 0 ]
then
	echo "operação realizada com sucesso"
else
	echo "houve um problema na operação"
fi
