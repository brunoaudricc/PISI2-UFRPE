def ler_matriz(arquivo_txt):
    pontos = {}
    origem = None
    with open(arquivo_txt, 'r') as matriz_txt:
        l, c = matriz_txt.readline().strip().split()
        for i in range(int(l)):
            linha = matriz_txt.readline().strip().split()
            count = 0
            for char in linha:
                if char == 'R':
                    origem = (i, count)
                elif char != '0':
                    pontos[char] = (i, count)
                count += 1
    return origem, pontos

def distancia(x, y):
    x1, y1 = x
    x2, y2 = y
    return abs(x1 - x2) + abs(y1 - y2)

def backtracking(lista_pontos, pontos, origem, caminho_atual, p_visitados, posi_atual, dist_atual, melhor_rota_info, memo):
    melhor_rota, melhor_distancia = melhor_rota_info

    estado = (posi_atual, frozenset(p_visitados))
    if estado in memo:
        if dist_atual >= memo[estado]:
            return
    memo[estado] = dist_atual

    if len(p_visitados) == len(lista_pontos):
        distancia_total = dist_atual + distancia(posi_atual, origem)
        if distancia_total < melhor_distancia[0]:
            melhor_distancia[0] = distancia_total
            melhor_rota[:] = caminho_atual[:]
        return

    for ponto in lista_pontos:
        if ponto not in p_visitados:
            proxima_posicao = pontos[ponto]
            nova_distancia = dist_atual + distancia(posi_atual, proxima_posicao)
            if nova_distancia >= melhor_distancia[0]:
                continue

            p_visitados.add(ponto)
            caminho_atual.append(ponto)

            backtracking(lista_pontos, pontos, origem, caminho_atual, p_visitados, proxima_posicao, nova_distancia, melhor_rota_info, memo)

            p_visitados.remove(ponto)
            caminho_atual.pop()

def menor_rota():
    origem, pontos = ler_matriz('matriz.txt')
    lista_pontos = list(pontos.keys())
    melhor_rota = []
    melhor_distancia = [float('inf')]
    memo = {}

    backtracking(lista_pontos, pontos, origem, [], set(), origem, 0, [melhor_rota, melhor_distancia], memo)

    print(' '.join(melhor_rota),f'\nDistância em Dronômetros: {melhor_distancia[0]}')

if __name__ == "__main__":
    menor_rota()
