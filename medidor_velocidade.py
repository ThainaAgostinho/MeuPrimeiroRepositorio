
valor1 = 130,16
valor2 = 195,23
Valor3 = 880,41

a = input ("Digite o número da placa: ")
placa = (a)
b = input("Digite a velocidade analisada: ")
velocidade_analisada = float(b)


limite = 40
infracao01 =  48.0
infracao02 =  60.0
infracao03 =  60.4


if velocidade_analisada <= limite:
     print(f'O carro placa: {placa} ' + 'está dentro da velocidade permitida')
elif velocidade_analisada <= infracao01:
 print(f'O carro placa: {placa} ' + 'atingiu a velocidade máxima permitida de 40km para essa rodovia e será multado em ' + f'{valor1}' + 'reais')
elif velocidade_analisada <= infracao02:
 print (f'O carro placa: {placa} ' + 'atingiu a velocidade máxima permitida de 40km para essa rodovia e será multado em ' + f'{valor2}' + 'reais')
elif velocidade_analisada >= infracao03:
 print (f'O carro placa: {placa} ' + 'atingiu a velocidade máxima permitida de 40km para essa rodovia e será multado em ' + f'{Valor3}' + 'reais')
