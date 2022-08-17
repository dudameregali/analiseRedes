from pathlib import Path
from turtle import color
import matplotlib.pyplot as plt
import json
import random
from datetime import datetime
from pytz import timezone

probesIds = [1000327, 19592, 6792, 1002506, 22671, 6931, 1002772, 1000473, 32670, 52770, 1002177, 13378, 24523, 32976, 52049, 21614, 1000819, 33661, 33022]
nomesSites = ['google.json', 'mapple.json', 'mamazon.json', 'melgar.json']


def gerarGrafico(sites, graficos, probes):
    # vai percorrer todos os sites, gerando cada gráfico para cada um dos sites
    for site in sites:
        # para cada site, abre o arquivo para leitura
        caminho = Path('.\jsons', str(site))
        #inicia a leitura de cada arquivo
        with open(caminho, 'r') as file:
            data = json.load(file)
            # percorre a lista de graficos que devem ser geradas para gerar cada um.
            for grafico in graficos:
                #inicia as listas que vão ser os pontos de X e Y no grafico
                axisX = [] 
                axisY = []
                # inicia as informações de X e Y para facilitar a leitura
                infoX = grafico[0]
                infoY = grafico[1]
                # inicia a figura de um tamanho padrão
                plt.figure(figsize=(12, 5))
                # percorre todas as probes para gerar linha linha para cada probe
                for probe in probes:
                    # percorre todos os elementos do arquivo json da vez
                    for datas in data:
                        # verifica de a probe selecionada é igual a probe do json
                        if probe == datas['probe']:
                            # verifica de o parametro é o timestamp, se for, converte para data e hora.
                            if infoX == 'timestamp':
                                aux = datetime.fromtimestamp(datas[infoX])
                                axisX.append(aux)
                                axisY.append(datas[infoY])
                            elif infoX == 'timestamp':
                                aux = datetime.fromtimestamp(datas[infoY])
                                axisY.append(aux)
                                axisX.append(datas[infoX])
                            else:
                                # caso a probe corresponda, adiciona na lista de cada eixo a informação correta
                                axisX.append(datas[infoX])
                                axisY.append(datas[infoY])
                    # ordena albas as listas sem perder a relação dos pontos
                    ordenada = ordenaListas(axisX, axisY)
                    # verifica o tipo de grafico
                    # grafico[2] = tipo do grafico que será gerado (linha ou dispercao)
                    if grafico[2] == 'dispercao':
                        # plota os pontos no grafico
                        plt.plot(ordenada[0], ordenada[1], 'ro', label=str(probe), color = ("#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])))
                    elif grafico[2] == 'linha':
                        # plota a linha no grafico
                        plt.plot(ordenada[0], ordenada[1], label=str(probe), color = ("#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])))
                    # reseta as listas dos pontos X e Y para a proxima linha do grafico
                    axisX = []
                    axisY = []
                # nomeia o eixo X
                plt.xlabel(str(infoX))
                # nomeia o eixo Y
                plt.ylabel(str(infoY))
                # coloca o título do gráfico
                plt.title(str(site) + "_" + str(infoX) + " X " + str(infoY))
                # adiciona a legenta no gráfico
                plt.legend(bbox_to_anchor = (1, 1))
                # variavel auxiliar para dar nome ao arquivo png que será gerado
                nomeArquivo = str(site) + "_" + str(infoX) + "_X_" + str(infoY) + '_' + str(grafico[2] + '.png')
                # salva o grafico como uma imagem png
                plt.savefig(str(Path('.\graficos', nomeArquivo)))
                #plt.show()

def ordenaListas(axisX, axisY):
    # ordene os índices em vez dos elementos em si
    indices = list(range(len(axisX)))
    indices.sort(key=lambda i: axisX[i]) 

    # crie as listas baseado na ordem dos índices
    axisXSort = [axisX[i] for i in indices]
    axisYSort = [axisY[i] for i in indices]

    return axisXSort, axisYSort


# Para chamar a função gerarGrafico usar como parametros.
# Parametro 1 - Lista dos momes dos sites que gerão gerados os graficos. Ex: ['google', 'mamazon']
# Parametro 2 - Lista com uma lista dos X,y e probes que devem ser geradas. Ex: [['rtt' , 'hops', linha],['rtt' , 'hops', dispercao]] 
# parametro 3 - Lista com as probes que vão ser geradas os gráficos Ex: probesIds ou [19592, 32670]

gerarGrafico(nomesSites, [['timestamp', 'rtt', 'linha'], ['timestamp','hops','linha'],['rtt', 'hops', 'dispercao']], probesIds)