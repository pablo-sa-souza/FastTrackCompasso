endereco = "Avenida Bento Gonçalves 1428, ap 11, partenon, porto alegre, RS, 90650-000"

import re

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)