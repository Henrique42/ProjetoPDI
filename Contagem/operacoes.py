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
            Retorna:
                - None
    """
    @staticmethod
    def marcar_conectados(imagem, i, j, label, alvo):
        # Pilha para saber se ainda existem pixels que precisam ser marcados
        pilha = [(i, j)]
        
        while pilha:
            x, y = pilha.pop()
            # Se o pixel for preto:
            if imagem.pixels[x][y] == alvo:
                # Para um objeto
                if alvo == 1:
                    # Marcar como visitado
                    imagem.pixels[x][y] = label
                    # Checagem da vizinhança 4
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        # Obtem as coordenadas do pixel adjacente
                        nx, ny = x + dx, y + dy
                        # Se o pixel adjacente não tiver sido visitado:
                        if 0 <= nx < imagem.altura and 0 <= ny < imagem.largura and imagem.pixels[nx][ny] == 1:
                            # Adiciona o pixel adjacente na pilha
                            pilha.append((nx, ny))
                # Para o background
                elif alvo == 0:
                    # Marcar como visitado
                    imagem.pixels[x][y] = -1
                    # Checagem da vizinhança 4
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        # Obtem as coordenadas do pixel adjacente
                        nx, ny = x + dx, y + dy
                        # Se o pixel adjacente não tiver sido visitado:
                        if 0 <= nx < imagem.altura and 0 <= ny < imagem.largura and imagem.pixels[nx][ny] == 0:
                            # Adiciona o pixel adjacente na pilha
                            pilha.append((nx, ny))


    """
        Método que adiciona um padding de 1 na imagem.
            Recebe:
                - imagem: objeto Imagem_PBM
            Retorna:
                - None
    """
    def adicionar_padding(imagem):
        # Adicionar padding de 1
        padded_matrix = []
        for i in range(imagem.altura+2):
            if i == 0 or i == imagem.altura+1:
                # Adicionar padding na primeira e na última linha
                padded_matrix.append([0]*(imagem.largura+2))
            else:
                # Adicionar padding na coluna da esquerda e da direita
                row = [0] + imagem.pixels[i-1] + [0]
                padded_matrix.append(row)

        imagem.altura += 2
        imagem.largura += 2
        imagem.pixels = padded_matrix

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
        Contador.marcar_conectados(imagem, i, j, count + 1, 0)

        # Retornar contagem
        return resultados
    