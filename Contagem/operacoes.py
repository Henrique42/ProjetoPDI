"""
    A classe Contagem define os métodos de contagem de figuras
"""
class Contador:
    """
        Método que marca pixelss adjacentes.
        Recebe a imagem e as coordenadas do pixel em questão.
            Recebe:
                - imagem: objeto Imagem_PBM
                - i: coordenada x da posição na qual se encontra o pixel
                - j: coordenada y da posição na qual se encontra o pixel
                - label: numeração do objeto
                - alvo: valor do pixel a ser considerado
                - resultados: vetor que guarda quantos buracos existem em cada objeto
            Retorna:
                - None
    """
    @staticmethod
    def marcar_conectados(imagem, i = 0, j = 0, label = -1, alvo = 0, resultados = None):
        # Pilha para saber se ainda existem pixels que precisam ser marcados
        pilha = [(i, j)]
        buraco_encontrado = False
        buraco_label = 0
        vizinhaca = []

        # Definição da vizinhaça a ser analisada
        # Caso o alvo seja um objeto:
        if alvo == 1:
            vizinhaca = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, -1), (-1, 1)]
        # Caso o alvo seja o fundo ou um buraco:
        elif alvo == 0:
            vizinhaca = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pilha:
            x, y = pilha.pop()

            # Se o pixel for preto:
            if imagem.pixels[x][y] == alvo:
                # Marcar como visitado
                imagem.pixels[x][y] = label
                
                # Checagem da vizinhança
                for dx, dy in vizinhaca:
                    # Obtem as coordenadas do pixel adjacente
                    nx, ny = x + dx, y + dy
                    # Se o pixel pertence a imagem:
                    if 0 <= nx < imagem.altura and 0 <= ny < imagem.largura:
                        # Se o pixel adjacente não tiver sido visitado:
                        if imagem.pixels[nx][ny] == alvo:
                            # Adiciona o pixel adjacente na pilha
                            pilha.append((nx, ny))
                        # Se estiver ocorrendo uma busca por buracos e for encontrado um objeto
                        elif label == -2 and imagem.pixels[nx][ny] > 0 and buraco_encontrado == False:
                            # Dizer que tem buraco e guardar a label do objeto
                            buraco_encontrado = True
                            buraco_label = imagem.pixels[nx][ny] - 2
        
        # Se um buraco for encontrado:
        if buraco_encontrado == True:
            # Aumentar a contagem de buracos para o devido objeto
            resultados[buraco_label] += 1


    """
        Método que adiciona um padding de 1 na imagem.
            Recebe:
                - imagem: objeto Imagem_PBM
            Retorna:
                - None
    """
    @staticmethod
    def adicionar_padding(imagem):
        imagem_padding = []
        # Adicionar padding de 1
        for i in range(imagem.altura+2):
            if i == 0 or i == imagem.altura+1:
                # Adicionar padding na primeira e na última linha
                imagem_padding.append([0]*(imagem.largura+2))
            else:
                # Adicionar padding na coluna da esquerda e da direita
                row = [0] + imagem.pixels[i-1] + [0]
                imagem_padding.append(row)

        # Substituir os valores da imagem anterior pelos da nova imagem
        imagem.altura += 2
        imagem.largura += 2
        imagem.pixels = imagem_padding


    """
        Método que verifica a quantidade de buracos nos objetos de uma imagem
            Recebe:
                - imagem: objeto Imagem_PBM
                - resultados: vetor que guarda quantos buracos existem em cada objeto
            Retorna:
                - None
    """
    @staticmethod
    def tem_buracos(imagem, resultados):
        # Verificar cada pixel da imagem
        for i in range(imagem.altura):
            for j in range(imagem.largura):
                # Se o pixel atual for preto, aumentar a contagem e marcar os conectados
                 if imagem.pixels[i][j] == 0:
                    Contador.marcar_conectados(imagem, i, j, -2, 0, resultados)


    """
        Método que conta quantas figuras existem na imagem.
            Recebe:
                - imagem: objeto Imagem_PBM
            Retorna:
                - Quantidade de objetos na imagem.
    """
    @staticmethod
    def contarFiguras(imagem):
        # Variável de contagem
        count = 0

        # Verificar cada pixel da imagem
        for i in range(imagem.altura):
            for j in range(imagem.largura):
                # Se o pixel atual for preto, aumentar a contagem e marcar os conectados
                 if imagem.pixels[i][j] == 1:
                    count += 1
                    Contador.marcar_conectados(imagem, i, j, count + 1, 1)

        # Criação e inicialização da matriz de resultados
        resultados = []

        for i in range(count):
            resultados.append(0)

        # Adicionar padding na imagem
        Contador.adicionar_padding(imagem)

        # Preencher o fundo com -1
        Contador.marcar_conectados(imagem)

        # Chamar método de contar buracos
        Contador.tem_buracos(imagem, resultados)

        # Retornar contagem
        return resultados
    