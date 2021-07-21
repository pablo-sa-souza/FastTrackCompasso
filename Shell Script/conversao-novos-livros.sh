#!/bin/bash

converte_imagem(){		 #declara a funcção converte_imagem
	local caminho_imagem=$1 #variavel caminho_imagem recebe o primeiro parametro (varrer_diretorio declarado na linha 23)
	local imagem_sem_extensao=$(ls $caminho_imagem | awk -F. '{ print $1 }')	#Imagem_sem_extensao recebe valor antes do "." se houver
	convert $imagem_sem_extensao.jpg $imagem_sem_extensao.png			#Converte imagem_sem_extensao de jpg para png.
}

varrer_diretorio(){
	cd $1			#recebe o valor do parametro declarado na linha 23.
	for arquivo in *	#iniciar o for criando variavel arquivo.
		do
		local caminho_arquivo=$(find ~/Downloads/imagens-novos-livros -name "$arquivo") #variavel caminho_arquivo recebe caminho (linha11)
		if [ -d $caminho_arquivo ]  						#verifica se o caminho é um diretorio
		then
			varrer_diretorio $caminho_arquivo				#varre diretorio abaixo.
		else
			converte_imagem $caminho_arquivo				#inicia a função de converter o arquivo.
		fi
done
}

varrer_diretorio ~/Downloads/imagens-novos-livros   					#parametro

if [ $? -eq 0 ]		#verifica se foi realizada conversão com sucesso.
then
	echo "Conversao realizada com sucesso"
else
	echo "houve uma falha"
fi
	
