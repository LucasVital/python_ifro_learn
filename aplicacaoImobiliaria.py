from imobiliaria import Imobiliaria
from residencia import Residencia
from escritorio import Escritorio

residencia1 = Residencia(1, 'Norte', 34, True, 2)

escritorio1 = Escritorio(1, 'Norte', 20, False, 50)
escritorio2 = Escritorio(3, 'Norte', 20, False, 51)
escritorio3 = Escritorio(5, 'Norte', 10, False, 51)

imob = Imobiliaria()
imob.inserir(residencia1)

imob.inserir(escritorio1)
imob.inserir(escritorio2)
imob.inserir(escritorio3)


#
imob.listar_imoveis()  # lista todos os imóveis. filtra por região ('Sul')

imob.alugar(1)
print('-> ' * 10)
imob.listar_imoveis()
print('-> ' * 10)
imob.devolver(1)
print('-> ' * 10)
imob.listar_imoveis()

print('-> ' * 10)
print()
#
imob.obter_imovel(3)  # listar imóvel com base no código

imob.remover(1)
#
print('-> ' * 10)
print('Após removido')
imob.listar_imoveis()

print('-> ' * 10)




