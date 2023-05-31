import time

lista_ru = [5, 4, 5, 4, 3, 5, 4, 3, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 5, 3, 5, 3, 5, 5, 5]
lista_ru.sort()

# FUNÇÃO MAXIMO & FUNÇÃO MINIMO
def maximo():
    listainversa = list(reversed(lista_ru))
    print('- o melhor nota para o almoço foi', listainversa[0])
def minimo():
     print('- a pior nota para o almoço foi', lista_ru[0])
# FUNÇÃO MAXIMO & FUNÇÃO MINIMO

# FUNÇÃO PARA DECORAÇÃO
def decorar():
        for cada in range(0, 6):
            print('=' * 35)
            print(f'As Avaliações de numero {cada} foi = {lista_ru.count(cada)}')
            print('=' * 35,  '\n')
# FUNÇÃO PARA DECORAÇÃO         


string = "Avaliação para o almoço do RU.\n"
for letra in string:
        print(letra, end='', flush=True)
        time.sleep(0.2)

time.sleep(1)
print(f'\nPELA ORDEM CRRESCENTE, AS AVALIAÇÕES FORAM: {lista_ru}')
listainversa = list(reversed(lista_ru))
time.sleep(1)
print(f'PELA ORDEM DECRESENTE, AS AVALIAÇÕES FORAM: {listainversa}\n')
time.sleep(1)
maximo()
time.sleep(1)
minimo()
time.sleep(1)
print(f'- o total de pessoas que responderam o formulario foi de {len(lista_ru)}')
time.sleep(1)
print(f'- o almoço tem uma media de {int(sum(lista_ru)/len(lista_ru))} Estrelas\n')
time.sleep(1)
decorar()

# CREDITOS
string = '''            CREDITOS...
        CRIADOR DO CODIGO: ANDRÉ
        DECORADOR: ANDRÉ
        FAZEDOR DO CODIGO: ANDRÉ
        CREDITOS DA MUSICA: ANDRÉ
        DONO DO PYTHON: ANDRÉ
        CRIADOR DO UNIVERSO: ANDRÉ'''
for letra in string:
        print(letra, end='', flush=True)
        time.sleep(0.1)
# CREDITOS
