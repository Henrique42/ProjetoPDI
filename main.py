from imagem import Imagem_PBM
# import numpy as np

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

      # Obter informações do cabeçalho
      imagem.formato = header[0]
      imagem.largura, imagem.altura = map(int, header[1].split())

      data = file.read()
      bits = [int(bit) for bit in data if bit != "\n"]
      
      # Moldar os bits em uma imagem 2D
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
    
def salvarImagem(imagem):
  try:
    nome = input('Informe o nome do arquivo (sem a extensão): ')
    filename = 'Resultados/' + nome + '.pbm'

    # Salvando a imagem em um novo arquivo .pbm
    with open(filename, "w") as newFile:
      # Escrever cabeçalho
      newFile.write(imagem.formato + '\n')
      newFile.write(f"{imagem.largura} {imagem.altura}\n")

      for pixel in imagem.pixels:
        for p in pixel:
          newFile.write(f"{p}")
        newFile.write("\n")

    print(f"Imagem {filename} salva com sucesso!")
  
  except Exception as erro:
    print(f"Erro: {erro}")

if __name__ == '__main__':
  imagem = Imagem_PBM()
  imagem = carregaImagem(imagem)
  
  if imagem is not None:
    salvarImagem(imagem)