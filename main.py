from Contagem.imagem import Imagem_PBM
from Contagem.operacoes import Contador


"""
  Método que carrega uma imagem .pbm
  Recebe:
    - imagem: objeto Imagem_PBM vazio que será preenchido com os dados da imagem carregada
  Retorna:
    - objeto Imagem_PBM preenchido com os dados da imagem carregada ou None em caso de erro
"""
def carregaImagem(imagem):
  try:
    nome = input('Informe o nome do arquivo (sem a extensão): ')
    filename = 'Testes/' + nome + '.pbm'
    
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
      
      print(f"Imagem {filename} carregada com sucesso!")

      return imagem
  
  except Exception as erro:
    print(f"Erro: {erro}")


"""
  Método que recebe um objeto imagem e o salva como um arquivo .pbm
  Recebe:
    - imagem: objeto Imagem_PBM que será salvo no arquivo
  Retorna:
    - None
"""
def salvarImagem(imagem):
  try:
    nome = input('Informe o nome do arquivo (sem a extensão): ')
    filename = 'Resultados/' + nome + '.pbm'

    # Salvando a imagem em um novo arquivo .pbm
    with open(filename, "w") as newFile:
      # Converte a imagem para string e adiciona no arquivo
      newFile.write(str(imagem))

    print(f"Imagem {filename} salva com sucesso!")
  
  except Exception as erro:
    print(f"Erro: {erro}")


"""
  Inicialização do sistema, carregando uma imagem e retornando a quantidade de figuras presentes.
"""
if __name__ == '__main__':
  imagem = Imagem_PBM()
  # Carregar imagem
  imagem = carregaImagem(imagem)
  # Salvar nova imagem
  #salvarImagem(imagem)
  
  if imagem is not None:
    print("Esperando resultados...\n")
    # Receber resultados da contagem de figuras e buracos
    resultados = Contador.contarFiguras(imagem)
    tamanho = len(resultados)

    # Imprimir resultados
    print("--------------------------------------")
    print(f"=> Total: {tamanho} figura(s)")
    print("--------------------------------------")

    for i in range(tamanho):
      print(f"> A figura {i + 1} contém {resultados[i]} buraco(s)")

    print("--------------------------------------")
    print("\nExecução finalizada!")
    