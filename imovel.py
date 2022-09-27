class Imovel:
    __slots__ = ['__codigo', '__regiao', '__area', '__disponivel']

    def __init__(self, codigo: int, regiao: str, area: int, disponivel: bool) -> None:
        self.__codigo = codigo
        self.__regiao = regiao
        self.__area = area
        self.__disponivel = disponivel

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo) -> None:
        self.__codigo = codigo

    @property
    def regiao(self) -> str:
        return self.__regiao

    @regiao.setter
    def regiao(self, regiao) -> None:
        self.__regiao = regiao

    @property
    def area(self) -> int:
        return self.__area

    @area.setter
    def area(self, area) -> None:
        self.__area = area

    @property
    def disponivel(self) -> bool:
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, disponivel) -> None:
        self.__disponivel = disponivel

    def __eq__(self, other) -> bool:
        if isinstance(other, Imovel):
            if self.codigo == other.codigo and self.regiao == other.regiao and self.area == other.area \
                    and self.disponivel == other.disponivel:
                return True
        return False

    def __str__(self) -> str:
        return f"Código: { self.codigo } \n" \
              f"Região: { self.regiao } \n" \
              f"Área: { self.area } \n" \
              f"Disponível: { self.disponivel } \n"


