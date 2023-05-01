class Imagem_PBM:
    def __init__(self, formato=None, largura=None, altura=None, pixels=None):
        """
        Cria um novo objeto Imagem_PBM.

        :param formato: o formato da imagem (P1)
        :type formato: str

        :param largura: a largura da imagem em pixels
        :type largura: int

        :param altura: a altura da imagem em pixels
        :type altura: int
        
        :param pixels: os pixels da imagem como uma lista de listas de inteiros (0 ou 1)
        :type pixels: list[list[int]]
        """
        self.formato = formato
        self.largura = largura
        self.altura = altura
        self.pixels = pixels if pixels is not None else []

    def __str__(self):
        """
        Retorna uma string que representa a imagem no formato P1.

        :return: a imagem como uma string no formato P1
        :rtype: str
        """
        header = f"{self.formato}\n{self.largura} {self.altura}\n"
        pixels_str = "\n".join(["".join(map(str, linha)) for linha in self.pixels])
        return f"{header}{pixels_str}"
