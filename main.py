from turtle import color
import matplotlib.pyplot as plt
import json
import random

# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()

with open('.\jsons\melgar.json', 'r') as file:
    data = json.load(file)

    def ordenaListas(axisX, axisY):
        # ordene os índices em vez dos elementos em si
        indices = list(range(len(axisX)))
        indices.sort(key=lambda i: axisX[i]) 

        # crie as listas baseado na ordem dos índices
        axisXSort = [axisX[i] for i in indices]
        axisYSort = [axisY[i] for i in indices]

        return axisXSort, axisYSort

    def gerarGraficoLinha(infoX, infoY):
        axisX = [] 
        axisY = []
        for datas in data:
            axisX.append(datas[infoX])
            axisY.append(datas[infoY])
        ordenada = ordenaListas(axisX, axisY)
        
        # plt.plot(ordenada[0], ordenada[1])
        # plt.show()

        plt.figure(figsize=(10, 5), layout='constrained')
        plt.plot(ordenada[0], ordenada[1])
        plt.xlabel(str(infoX))
        plt.ylabel(str(infoY))
        plt.title("INCLUIR TÍTULO")
        plt.legend('legenda de testes');
        plt.show()

    def gerarGraficoLinhaPorProbe(infoX, infoY, probes):
        axisX = [] 
        axisY = []

        plt.figure(figsize=(12, 5))

        for probe in probes:
            for datas in data:
                if probe == datas['probe']:
                    axisX.append(datas[infoX])
                    axisY.append(datas[infoY])
            ordenada = ordenaListas(axisX, axisY)
            plt.plot(ordenada[0], ordenada[1], label=str(probe),)
            axisX = []
            axisY = []
        
        # plt.plot(ordenada[0], ordenada[1])
        # plt.show()
        
        plt.xlabel(str(infoX))
        plt.ylabel(str(infoY))
        plt.title("INCLUIR TÍTULO")
        plt.legend(bbox_to_anchor = (1, 1));
        plt.savefig('.\graficos\meuGrafico.png')
        plt.show()
            
    def gerarGraficoDispescao(infoX, infoY):
        axisX = [] 
        axisY = []
        for datas in data:
            axisX.append(datas[infoX])
            axisY.append(datas[infoY])
        ordenada = ordenaListas(axisX, axisY)
        
        plt.plot(ordenada[0], ordenada[1], 'ro')
        plt.show()

    def gerarGraficoDispercaoPorProbe(infoX, infoY, probes):
        axisX = [] 
        axisY = []
        
        plt.figure(figsize=(12, 5))
        cont = 0
        for probe in probes:
            for datas in data:
                if probe == datas['probe']:
                    axisX.append(datas[infoX])
                    axisY.append(datas[infoY])
            ordenada = ordenaListas(axisX, axisY)

            plt.plot(ordenada[0], ordenada[1], 'ro', label=str(probe), color = ("#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])))
            axisX = []
            axisY = []
        
        plt.xlabel(str(infoX))
        plt.ylabel(str(infoY))
        plt.title("INCLUIR TÍTULO")
        plt.legend(bbox_to_anchor = (1, 1));
        plt.show()
    

    probesIds = []
    for datas in data:
        probesIds.append(datas['probe'])
    probesIds = set(probesIds)
    print(probesIds)

    # gerarGraficoDispescao('rtt','hops')
    # gerarGraficoLinha('timestamp', 'hops')
    gerarGraficoLinhaPorProbe('timestamp', 'hops', probesIds)
    #gerarGraficoDispercaoPorProbe('hops', 'rtt', [19592, 32670])



    
    

    
    

    
