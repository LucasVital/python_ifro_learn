class Imobiliaria:
    __slots__ = ['__quantidade', '__imoveis']

    def __init__(self) -> None:
        self.__quantidade = 0
        self.__imoveis = []

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade) -> None:
        self.__quantidade = quantidade
        
    @property
    def imoveis(self):
        return self.__imoveis
    
    @imoveis.setter
    def imoveis(self, imovel):
        self.__imoveis = imovel

    def inserir(self, imovel):
        for obj in self.imoveis:
            if obj == imovel:
                return False
        if self.valida_codigo(imovel):
            self.imoveis.append(imovel)
            self.quantidade += 1
        return False

    def valida_codigo(self, imovel):
        for obj in self.imoveis:
            if obj.codigo == imovel.codigo:
                return False
        return True

    def remover(self, imovel):
        for obj in self.imoveis:
            if obj.codigo == imovel:
                self.imoveis.remove(obj)
                self.quantidade -= 1
                return True

    def alugar(self, cod_imovel) -> bool:
        for obj in self.imoveis:
            if obj.codigo == cod_imovel:
                obj.disponivel = False
        return True

    def devolver(self, cod_imovel) -> bool:
        for obj in self.imoveis:
            if obj.codigo == cod_imovel:
                obj.disponivel = True
        return True

    def obter_imovel(self, codigo):
        for imovel in self.imoveis:
            if imovel.codigo == codigo:
                print(imovel)
        return f'Imóvel não encontrado.'

    def listar_imoveis(self, filtro: str = ''):
        for imovel in self.imoveis:
            if imovel.regiao == filtro:
                print(imovel)
            if filtro == '':
                print(imovel)
