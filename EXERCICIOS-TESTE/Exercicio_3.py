"""
EXERCÍCIO 3 — Sistema de Arquivos

Crie uma classe base chamada Arquivo.

Essa classe deve possuir o método:
abrir()

Depois crie três classes filhas:

- ArquivoTexto
- ArquivoImagem
- ArquivoVideo

Cada classe deve sobrescrever o método abrir()
mostrando um comportamento diferente.

Exemplo de saída:

Abrindo arquivo de texto
Abrindo imagem
Reproduzindo vídeo

Depois crie uma lista com diferentes tipos de arquivos
e percorra essa lista chamando o método abrir() para cada um.
"""

class Arquivo:
    def abrir(self):
        raise NotImplementedError
    
class ArquivoTexto(Arquivo):
    def abrir(self):
        print("Abrindo arquivo de texto")
            
class ArquivoImagem(Arquivo):
    def abrir(self):
        print("Abrindo imagem")
            
class ArquivoVideo(Arquivo):
    def abrir(self):
        print("Reproduzindo video")

arquivos = [ArquivoTexto(), ArquivoImagem(), ArquivoVideo()]

for a in arquivos:
    a.abrir()