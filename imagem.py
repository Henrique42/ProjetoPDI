"""
    A classe Imagem_PBM define os atributos para uma imagem binária do tipo .pbm
"""
class Imagem_PBM:
    def __init__(self):
        self.formato = None
        self.largura = None
        self.altura = None
        self.pixels = []