import json

obj = []
arquivo = '.\jsons\mamazon2.json'
with open(arquivo, "r") as file:
    data = json.load(file)
    f = open('teste.json', "w")
    rtt = 0
    for dados in data:
        totalHops = len(dados['result'])
        aux = int(totalHops) - 1
        ultimoHop = dados['result'][aux]
        print(aux)

        for hop in dados['result']:
            if hop['hop'] == 255:
                if not('rtt' in hop['result'][1]):
                    if 'rtt' in hop['result'][2]:
                        rtt = hop['result'][2]['rtt']
                    elif 'rtt' in hop['result'][0]:
                        rtt = hop['result'][0]['rtt']
                    else:
                        rtt = 0
                else:
                    rtt = hop['result'][1]['rtt']
                obj.append({
                    "probe": dados["prb_id"],
                    "timestamp": dados["timestamp"],
                    "rtt": rtt,
                    "hops": totalHops
                })

    json.dump(obj, f, indent=4)


# obj = []
# arquivo = 'jsons\melgar.json'
# with open(arquivo, "r") as file:
#     data = json.load(file)
#     f = open(arquivo + str('teste'), "w")
#     rtt = 0
#     for dados in data:
#         totalHops = len(dados['result'])
#         for hop in dados['result']:
#             if hop['hop'] == 255:
#                 if not('rtt' in hop['result'][1]):
#                     if 'rtt' in hop['result'][2]:
#                         rtt = hop['result'][2]['rtt']
#                     elif 'rtt' in hop['result'][0]:
#                         rtt = hop['result'][0]['rtt']
#                     else:
#                         rtt = 0
#                 else:
#                     rtt = hop['result'][1]['rtt']
                
#                 obj.append({
#                     "probe": dados["prb_id"],
#                     "timestamp": dados["timestamp"],
#                     "rtt": rtt,
#                     "hops": totalHops
#                 })

#     json.dump(obj, f, indent=4)