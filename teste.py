import random
import time

#Lista para armazenar os tempos de execução de cada algoritmo, e cada tamanho de lista
tempos_execucao = []

#Função para ler e validar se a opção escolhida é válida
def ler_opcao(mensagem):
    while True:
        try:
            opcao = int(input(mensagem))
            return opcao
        except ValueError:
            print('Por favor, apenas utilize números!')
            input('Pressione Enter para tentar novamente...')

#Função para criar a lista, de acordo com o tamanho escolhido
def criar_lista(tamanho):
    lista = [random.randint(0, tamanho) for i in range(tamanho)]
    
    nome_arquivo = f'lista_desordenada_{tamanho}.txt'
    
    with open(nome_arquivo, 'w') as arquivo:
        for numero in lista:
            arquivo.write(f'{numero}\n')
    return lista

#Função para, além de manter a lista original, guardar a nova lista ordenada, em .txt
def salvar_lista_ordenada(lista, nome_algoritmo):
    tamanho = len(lista)
    nome_arquivo = f'lista_ordenada_{nome_algoritmo}_{tamanho}.txt'
    
    with open(nome_arquivo, 'w') as arquivo:
        for numero in lista:
            arquivo.write(f'{numero}\n')

#Função para imprimir o menu
def imprimir_menu():
    print('============= TEMPOS DE EXECUÇÃO DOS ALGORITMOS DE ORDENAÇÃO =============')
    print('[1] - Bubble Sort')
    print('[2] - Insertion Sort')
    print('[3] - Selection Sort')
    print('[4] - Merge Sort')
    print('[5] - Ver tempos de execução')
    print('[6] - Sair')
    print('===========================================================================')

#Função para escolher o tamanho da lista, e lógica do menu para o tamanho da lista
def escolha_tamanho():
    print('============= ESCOLHA O TAMANHO DA LISTA =============')
    print('[1] - 1 mil')
    print('[2] - 5 mil')
    print('[3] - 10 mil')
    print('[4] - 50 mil')
    print('[5] - 100 mil')
    print('[6] - Retornar ao menu anterior')

    opcao = ler_opcao('Escolha uma opção:')

    match opcao:
        case 1: return criar_lista(1000)
        case 2: return criar_lista(5000)
        case 3: return criar_lista(10000)
        case 4: return criar_lista(50000)
        case 5: return criar_lista(100000)
        case 6:
            print('Retornando ao menu anterior...')
            return None
        case _:
            print('Opção inválida!')
            return None

#Funções do Bubble Sort
def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def bubble_sort(lista):
    n = len(lista)
    for _ in range(n):
        trocou = False
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                troca(lista, i, i + 1)
                trocou = True
        if not trocou:
            break

#Função do Insertion Sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        pivo = lista[i]
        j = i-1
        while j>=0 and pivo<lista[j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = pivo

#Função do Selection Sort
def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

#Função do Merge Sort
def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        L = lista[:meio]
        R = lista[meio:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1

#Função para calcular o tempo gasto por cada algoritmo
def get_time(funcao, arg, nome_algoritmo):
    inicio = time.time()
    funcao(arg)
    fim = time.time()
    tempo = fim - inicio
    tamanho_lista = len(arg)
    tempos_execucao.append(f'{nome_algoritmo} - {tamanho_lista} itens: {tempo:.3f} segundos')
    salvar_lista_ordenada(arg, nome_algoritmo)
    return tempo

#Função para imprimir os tempos de execução armazenados na lista
def exibir_tempos_execucao():
    if len(tempos_execucao) == 0:
        print('Nenhum algoritmo foi executado ainda.')
    else:
        print('============= TEMPOS DE EXECUÇÃO =============')
        for tempo in tempos_execucao:
            print(tempo)
        print('===============================================')

#Lógica principal do programa
def main():
    while True:
        imprimir_menu()
        opcao = ler_opcao('Escolha uma opção:')

        match opcao:
            case 1:
                print('Bubble Sort')
                lista = escolha_tamanho()
                if lista:
                    print(f'Lista antes da ordenação: {lista[:10]}...')
                    bubble_lista = lista.copy()
                    tempo_execucao = get_time(bubble_sort, bubble_lista, 'Bubble Sort')
                    print(f'Lista após a ordenação: {bubble_lista[:10]}...')
                    print(f'Tempo de execução do Bubble Sort: {tempo_execucao:.3f} segundos')
            case 2:
                print('Insertion Sort')
                lista = escolha_tamanho()
                if lista:
                    print(f'Lista antes da ordenação: {lista[:10]}...')
                    insertion_lista = lista.copy()
                    tempo_execucao = get_time(insertion_sort, insertion_lista, 'Insertion Sort')
                    print(f'Lista após a ordenação: {insertion_lista[:10]}...')
                    print(f'Tempo de execução do Insertion Sort: {tempo_execucao:.3f} segundos')
            case 3:
                print('Selection Sort')
                lista = escolha_tamanho()
                if lista:
                    print(f'Lista antes da ordenação: {lista[:10]}...')
                    selection_lista = lista.copy()
                    tempo_execucao = get_time(selection_sort, selection_lista, 'Selection Sort')
                    print(f'Lista após a ordenação: {selection_lista[:10]}...')
                    print(f'Tempo de execução do Selection Sort: {tempo_execucao:.3f} segundos')
            case 4:
                print('Merge Sort')
                lista = escolha_tamanho()
                if lista:
                    print(f'Lista antes da ordenação: {lista[:10]}...')
                    merge_lista = lista.copy()
                    tempo_execucao = get_time(merge_sort, merge_lista, 'Merge Sort')
                    print(f'Lista após a ordenação: {merge_lista[:10]}...')
                    print(f'Tempo de execução do Merge Sort: {tempo_execucao:.3f} segundos')
            case 5:
                exibir_tempos_execucao()
            case 6:
                break
            case _:
                print('Opção inválida!')

#Executar o programa
if __name__ == '__main__':
    main()