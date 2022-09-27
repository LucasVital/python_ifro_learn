from imovel import Imovel


class Residencia(Imovel):
    __slots__ = ['__numero_quartos']

    def __init__(self, codigo, regiao, area, disponivel, numero_quartos: int) -> None:
        self.__numero_quartos = numero_quartos
        super().__init__(codigo, regiao, area, disponivel)

    @property
    def numero_quartos(self) -> int:
        return self.__numero_quartos

    @numero_quartos.setter
    def numero_quartos(self, numero_quartos):
        self.__numero_quartos = numero_quartos

    def __eq__(self, other) -> bool:
        if isinstance(other, Residencia):
            if self.codigo == other.codigo and self.regiao == other.regiao and self.area == other.area \
                    and self.disponivel == other.disponivel and self.numero_quartos == other.numero_quartos:
                return True
        return False

    def __str__(self) -> str:
        return super().__str__() + f"Número de quartos: { self.numero_quartos } \n"
