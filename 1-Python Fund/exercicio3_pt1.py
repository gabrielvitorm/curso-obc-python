distancia = float(input("Digite a distância que você vai percorrer em km: \n"))

if distancia > 200:
    price = distancia * 0.35
    print(f"Você vai ter que pagar R$ {price}, para viajar {distancia} Km")

else:
    price = distancia * 0.5
    print(f"Você vai ter que pagar R$ {price}, para viajar {distancia} Km")