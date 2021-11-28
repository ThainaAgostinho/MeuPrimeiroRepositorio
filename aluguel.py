periodo = 0
veiculo_preco = 0.0
seguro = 0.0
taxa_adm = 75.00
opcionais = {}
opcional = -1

periodo = int(input("Quantos dias pretende alugar?: "))

veiculo = int(input('''Qual veículo deseja alugar: 
(1)Economico: R$ 80.95 + seguro 20,50
(2)Sedan: R$ 100.30 + seguro 30,65
(3)SUV: R$ 135.90 + seguro 45,99
Taxa administrativa fixa: R$ 75,00
'''))

if veiculo == 1:
    veiculo = "Econômico"
    veiculo_preco = 80.95
    seguro = 20.50
elif veiculo == 2:
    veiculo = "Sedan"
    veiculo_preco = 100.30
    seguro = 30.65
elif veiculo == 3:
    veiculo = "SUV"
    veiculo_preco = 135.95
    seguro = 45.99

while opcional != 0:
    opcional = int(input('''Deseja algum desses adicinais?:
    (1)GPS: R$ 12,00
    (2)Bebê Conforto: R$ 15,00
    (3)Cadeira de Bebê: R$ 15,00
    (4)Assento de Elevação: R$ 15,00
    (0)Não quero nenhum opcional.
     '''))

    if opcional == 1:
        opcionaldict = {"GPS": 12.00}
        opcionais.update(opcionaldict)
        print("Mais algum?")
    elif opcional == 2:
        opcionaldict = {"Bebê Conforto": 15.00}
        opcionais.update(opcionaldict)
        print("Mais algum?")
    elif opcional == 3:
        opcionaldict = {"Cadeira de Bebê": 15.00}
        opcionais.update(opcionaldict)
        print("Mais algum?")
    elif opcional == 4:
        opcionaldict = {"Assento de Elevação": 15.00}
        opcionais.update(opcionaldict)
        print("Mais algum?")
    elif opcional == 0:
        print("Valores salvos com sucesso!")
    else:
        print("valor incorreto!")

def calculo_aluguel(periodo_aluguel,preco_veiculo, taxa, seguro_veiculo, opc={}):
    adicional = 0.0
    if "GPS" in opc.keys():
        adicional += 12.00
    elif "Bebê Conforto" in opc.keys():
        adicional += 15.00
    elif "Cadeira de Bebê" in opc.keys():
        adicional += 15.00
    elif "Assento de Elevação" in opc.keys():
        adicional += 15.00

    global diaria
    diaria = (preco_veiculo+seguro_veiculo+adicional)
    return (diaria*periodo_aluguel)+taxa

def gravar_NF(periodo_aluguel, veiculo_alugado, preco_veiculo, seguro_veiculo,opc={}):
    file = open('nf.txt', 'w')
    frase="\nTipo do veículo: " + str(veiculo_alugado)
    file.write(frase)
    frase = "\n" + str(periodo_aluguel) + " Diárias            Total"
    file.write(frase)
    frase = "\n" + str(periodo_aluguel) + "x R$ " + str(preco_veiculo) + "         " + \
            str(preco_veiculo*periodo_aluguel)
    file.write(frase)
    file.write("\n--------------------------")
    file.write("\nSeguro do Carro")
    frase = "\n" + str(periodo_aluguel) + "x R$ " + str(seguro_veiculo) + "         " + \
            str(seguro_veiculo * periodo_aluguel)
    file.write(frase)
    file.write("\n--------------------------")

    if "GPS" in opc.keys():
        file.write("\nGPS: R$ 12,00")
    elif "Bebê Conforto" in opc.keys():
        file.write("\nBebê Conforto: R$ 15,00")
    elif "Cadeira de Bebê" in opc.keys():
        file.write("\nCadeira de Bebê: R$ 15,00")
    elif "Assento de Elevação" in opc.keys():
        file.write("\nAssento de Elevação: R$ 15,00")

    file.write("\n--------------------------\n")
    file.write("Taxa Administrativa R$ 75,00")
    file.write("\n--------------------------\n")
    total = calculo_aluguel(periodo_aluguel, preco_veiculo, taxa_adm, seguro, opcionais)
    frase = "Total do Aluguel R$ " + str(total)
    file.write(frase)

    file.close()

def imprimir_nf(file_name):
    file = open(file_name, 'r')
    print(file.read())

gravar_NF(periodo, veiculo, veiculo_preco, seguro, opcionais)

imprimir_nf("nf.txt")

