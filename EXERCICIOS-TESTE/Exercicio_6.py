"""
EXERCÍCIO 6 — Sistema de Processamento de Arquivos

Crie uma classe base chamada ProcessadorArquivo.

Essa classe deve possuir o método:
processar(caminho)

Depois crie três classes filhas:

- ProcessadorCSV
- ProcessadorJSON
- ProcessadorXML

Cada classe deve sobrescrever o método processar()
mostrando qual tipo de arquivo está sendo processado.

Exemplo de saída:

Processando CSV...
Processando JSON...
Processando XML...

Crie uma lista com diferentes processadores
e execute todos usando o mesmo método processar().
"""