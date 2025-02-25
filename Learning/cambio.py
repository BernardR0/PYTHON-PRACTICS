dolar = 5.94
opcao = int(input("(1) para real e (2) para dolár "))
if opcao == 1:
    reais = float(input("Quantos reais voce tem? "))
    if reais != 0:
        cambio = reais/dolar
        print("A conversão é de {} dólares".format(cambio))
    else:
        print("conversão impossível")    
elif opcao == 2:
    dolares = float(input("Quantos dolares voce tem? "))
    if dolar != 0:
        cambio = dolares*dolar
        print("A conversao é de {} reais".format(cambio))
    else:
        print("conversão impossivel")
    