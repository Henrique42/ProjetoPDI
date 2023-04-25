from imagem import Imagem_PBM
from operacoes import Contagem
# import numpy as np


"""
  Método que carrega uma imagem .pbm
"""
def carregaImagem(imagem):
  try:
    nome = input('Informe o nome do arquivo (sem a extensão): ')
    filename = 'Recursos/' + nome + '.pbm'
    
    # Abrir imagem
    with open(filename, "r") as file:

      # Obtendo o cabeçalho
      header = []
      for linha in file:
        if linha.startswith("#"):
          continue
        header.append(linha.strip())
        if len(header) == 2:
          break

      # Adicionar informações do cabeçalho ao objeto imagem
      imagem.formato = header[0]
      imagem.largura, imagem.altura = map(int, header[1].split())

      data = file.read()
      bits = [int(bit) for bit in data if bit != "\n"]
      
      # Moldar os bits em uma imagem 2D altura x largura
      for i in range(imagem.altura):
        linha = []
        for j in range(imagem.largura):
          linha.append(bits[i*imagem.largura + j])
        imagem.pixels.append(linha)

      """
      Alternativa:
      imagem.pixels = np.array(bits).reshape((imagem.altura, imagem.largura))
      """
      
      print(f"Imagem {filename} carregada com sucesso!")

      return imagem
  
  except Exception as erro:
    print(f"Erro: {erro}")


"""
  Método que recebe um objeto imagem e o salva como um arquivo .pbm
"""
def salvarImagem(imagem):
  try:
    nome = input('Informe o nome do arquivo (sem a extensão): ')
    filename = 'Resultados/' + nome + '.pbm'

    # Salvando a imagem em um novo arquivo .pbm
    with open(filename, "w") as newFile:
      # Adicionar cabeçalho
      newFile.write(imagem.formato + '\n')
      newFile.write(f"{imagem.largura} {imagem.altura}\n")

      # Adicionar conteúdo
      for pixel in imagem.pixels:
        for p in pixel:
          newFile.write(f"{p}")
        newFile.write("\n")

    print(f"Imagem {filename} salva com sucesso!")
  
  except Exception as erro:
    print(f"Erro: {erro}")


"""
  Inicialização do sistema
"""
if __name__ == '__main__':
  imagem = Imagem_PBM()
  imagem = carregaImagem(imagem)
  
  if imagem is not None:
    #salvarImagem(imagem)
    print(f"Figuras encontradas: {Contagem.contarFiguras(imagem)}")
    