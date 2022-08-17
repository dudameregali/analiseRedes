from distutils.log import info
import matplotlib.pyplot as plt
import json

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
            print(datas)
            axisX.append(datas[infoX])
            axisY.append(datas[infoY])
        ordenada = ordenaListas(axisX, axisY)
        
        # plt.plot(ordenada[0], ordenada[1])
        # plt.show()

        plt.figure(figsize=(40, 20), layout='constrained')
        plt.plot(ordenada[0], ordenada[1])
        plt.xlabel(str(infoX))
        plt.ylabel(str(infoY))
        plt.title("INCLUIR TÍTULO")
        plt.legend('legenda de testes');
        plt.show()

    def gerarGraficoLinhaPorProbe(infoX, infoY, probes):
        axisX = [] 
        axisY = []
        
        plt.figure(figsize=(10, 5))
        
        for probe in probes:
            for datas in data:
                if probe == datas['probe']:
                    print(datas)
                    axisX.append(datas[infoX])
                    axisY.append(datas[infoY])
            ordenada = ordenaListas(axisX, axisY)
            plt.plot(ordenada[0], ordenada[1], label=str(probe))
            axisX = []
            axisY = []
        
        # plt.plot(ordenada[0], ordenada[1])
        # plt.show()
        
        plt.xlabel(str(infoX))
        plt.ylabel(str(infoY))
        plt.title("INCLUIR TÍTULO")
        plt.legend(bbox_to_anchor = (1.05, 0.6));
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

    probesIds = []
    for datas in data:
        probesIds.append(datas['probe'])
    probesIds = set(probesIds)
    print(probesIds)



    # gerarGraficoDispescao('rtt','hops')
    #gerarGraficoLinha('timestamp', 'hops')
    gerarGraficoLinhaPorProbe('timestamp', 'hops', probesIds)




    
    

    
    

    
