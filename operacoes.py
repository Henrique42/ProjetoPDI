"""
    A classe Contagem define os métodos de contagem de figuras
"""
class Contagem:
    """
        Método que marca pixelss adjacentes.
        Recebe a imagem e as coordenadas do pixel em questão.
    """
    @staticmethod
    def marcar_conectados(imagem, i, j):
        # Pilha para saber se ainda existem pixels que precisam ser marcados
        pilha = [(i, j)]
        
        while pilha:
            x, y = pilha.pop()
            # Se o pixel for preto:
            if imagem.pixels[x][y] == 1:
                # Marcar como visitado
                imagem.pixels[x][y] = -1
                # Checagem da vizinhança 4
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    # Obtem as coordenadas do pixel adjacente
                    nx, ny = x + dx, y + dy
                    # Se o pixel adjacente não tiver sido visitado:
                    if 0 <= nx < imagem.altura and 0 <= ny < imagem.largura and imagem.pixels[nx][ny] == 1:
                        # Adiciona o pixel adjacente na pilha
                        pilha.append((nx, ny))


    """
        Método que conta quantas figuras existem na imagem.
        Recebe a imagem e retorna a contagem.
    """
    @staticmethod
    def contarFiguras(imagem):
        # Variável de contagem
        count = 0

        try: 
            # Verificar cada pixel da imagem
            for i in range(imagem.altura):
                for j in range(imagem.largura):
                    # Se o pixel atual for preto, aumentar a contagem e marcar os conectados
                    if imagem.pixels[i][j] == 1:
                        count += 1
                        Contagem.marcar_conectados(imagem, i, j)
        
        except Exception as erro:
            print(f"Erro: {erro}")

        # Step 6: Return count
        return count
    