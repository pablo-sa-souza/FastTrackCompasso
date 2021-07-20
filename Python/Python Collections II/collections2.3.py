from collections import Counter

texto1 = "Lewis Hamilton foi alvo de manifestações racistas nas suas redes sociais logo depois da vitória no polêmico GP da Inglaterra, décima etapa da temporada 2021 da Fórmula 1, no último domingo (18). A corrida foi marcada pela polêmica causada em razão da batida entre Hamilton e Max Verstappen na primeira volta, com o holandês levando a pior e batendo forte na barreira de proteção. A Mercedes, a FIA (Federação Internacional de Automobilismo) e a Fórmula 1, também por meio das redes sociais, condenaram os ataques sofridos pelo heptacampeão mundial em uma declaração conjunta nesta manhã de segunda-feira. Logo depois, Red Bull, equipe de Max, e a McLaren, também repudiaram as manifestações racistas."

texto2 = "Este estudo será feito em participantes ambulatoriais do sexo masculino com covid-19 leve a moderada e é patrocinado pela empresa chinesa Suzhou Kintor Pharmaceuticals. A pesquisa será realizada na Alemanha, Argentina, África do Sul, Ucrânia, México, Estados Unidos e no Brasil, onde participarão 12 voluntários no Estado de Roraima e outros 38 em São Paulo."


def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))
  mais_comuns = proporcoes.most_common(10)
  for caractere, proporcao in mais_comuns:
    print("{} => {:.2f}%".format(caractere, proporcao * 100))

analisa_frequencia_de_letras(texto1)

analisa_frequencia_de_letras(texto2)