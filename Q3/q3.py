import json


def ler_json(arquivo):
    with open(arquivo, 'r') as arq:
        dados = json.load(arq)
        return dados


def media(lista):
    return round(sum(lista) / len(lista), 2)


def qtd_valores_acima_da_media(lista):
    media_lista = media(lista)
    return len(list(filter(lambda val: val > media_lista, lista)))


def remover_dias_sem_faturamento(lista):
    if 0 in lista:
        qtd_dia_faturamento = list(filter(lambda val: val > 0, lista))
        return qtd_dia_faturamento
    else:
        return lista


def tratamento_dados(lista):
    tratado = []
    for x in range(1, len(lista)):
        if x < 10:
            x = "0" + str(x)
            tratado.append(lista[str(x)])
        else:
            tratado.append(lista[str(x)])
    zero_removido= remover_dias_sem_faturamento(tratado)
    return zero_removido


def mostrar_faturamento(arquivo):
    faturamento_json = ler_json(arquivo)['faturamento_diario']
    faturamento = tratamento_dados(faturamento_json)
    print('Menor valor: ', min(faturamento))
    print('Maior valor: ', max(faturamento))
    #print('Média: ', media(faturamento))
    print('Quantidade de valores acima da média: ', qtd_valores_acima_da_media(faturamento))
    return True


print(mostrar_faturamento('faturamento.json'))
