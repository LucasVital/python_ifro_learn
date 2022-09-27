from imovel import Imovel


class Escritorio(Imovel):
    __slots__ = ['__area_util']

    def __init__(self, codigo, regiao, area, disponivel, area_util: int) -> None:
        super().__init__(codigo, regiao, area, disponivel,)
        self.__area_util = area_util

    @property
    def area_util(self) -> int:
        return self.__area_util

    @area_util.setter
    def area_util(self, area_util):
        self.__area_util = area_util

    def __eq__(self, other) -> bool:
        if isinstance(other, Escritorio):
            if self.codigo == other.codigo and self.regiao == other.regiao and self.area == other.area \
                    and self.disponivel == other.disponivel and self.area_util == other.area_util:
                return True
        return False

    def __str__(self):
        return super().__str__() + f"Area útil: { self.area_util } \n"
