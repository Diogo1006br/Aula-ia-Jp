import random

class Objeto:
    def __init__(self, peso, rec):
        self.peso = peso
        self.rec = rec

def cria_populacao(tm_pop, num_objetos):
    return [[random.randint(0, 1) for _ in range(num_objetos)] for _ in range(tm_pop)]

def avalia_populacao(populacao, objetos, capacidade_mochila):
    valores = []
    for individuo in populacao:
        peso_total = sum(objetos[i].peso for i in range(len(individuo)) if individuo[i])
        if peso_total > capacidade_mochila:
            valores.append(0)
        else:
            rec_total = sum(objetos[i].rec for i in range(len(individuo)) if individuo[i])
            valores.append(rec_total)
    return valores

def seleciona_pais(populacao, valores):
    soma_valores = sum(valores)
    probabilidades = [valor / soma_valores for valor in valores]
    pais = []
    for _ in range(len(populacao)):
        pai1 = random.choices(populacao, probabilidades)[0]
        pai2 = random.choices(populacao, probabilidades)[0]
        pais.append((pai1, pai2))
    return pais

def crossover(pais):
    filhos = []
    for pai1, pai2 in pais:
        ponto_corte = random.randint(1, len(pai1) - 1)
        filho = pai1[:ponto_corte] + pai2[ponto_corte:]
        filhos.append(filho)
    return filhos

def mutacao(filhos, taxa_mutacao):
    for i in range(len(filhos)):
        for j in range(len(filhos[i])):
            if random.random() < taxa_mutacao:
                filhos[i][j] = 1 - filhos[i][j]

def algoritmo_genetico(objetos, capacidade_mochila, tm_pop, num_geracoes, taxa_mutacao):
    num_objetos = len(objetos)
    populacao = cria_populacao(tm_pop, num_objetos)

    for geracao in range(num_geracoes):
        valores = avalia_populacao(populacao, objetos, capacidade_mochila)
        melhores_individuos = [populacao[i] for i in range(len(populacao)) if valores[i] == max(valores)]
        melhor_valor = max(valores)
        print(f"Geração {geracao + 1} - Melhor valor: {melhor_valor}")

        pais = seleciona_pais(populacao, valores)
        filhos = crossover(pais)
        mutacao(filhos, taxa_mutacao)
        populacao = melhores_individuos + filhos[:tm_pop - len(melhores_individuos)]

    melhor_solucao = melhores_individuos[0]
    melhor_peso = sum(objetos[i].peso for i in range(len(melhor_solucao)) if melhor_solucao[i])
    melhor_rec = sum(objetos[i].rec for i in range(len(melhor_solucao)) if melhor_solucao[i])

    return melhor_solucao, melhor_peso, melhor_rec

if __name__ == "__main__":
    # Exemplo de uso
    objetos = [Objeto(2, 10), Objeto(3, 8), Objeto(4, 15), Objeto(5, 7), Objeto(9, 6)]
    capacidade_mochila = 10
    tm_pop = 50
    num_geracoes = 100
    taxa_mutacao = 0.1

    melhor_solucao, melhor_peso, melhor_rec = algoritmo_genetico(
        objetos, capacidade_mochila, tm_pop, num_geracoes, taxa_mutacao
    )

    print("Melhor solução encontrada:")
    print("Solução:", melhor_solucao)
    print("Peso:", melhor_peso)
    print("rec:", melhor_rec)
