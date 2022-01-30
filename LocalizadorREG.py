import pandas as pd
print("\n| $$                         $$$$$$$$                |__$$                 | $$   | $$/$$$$     /$$$$$$$$ "
      "\n| $$       /$$$$$$  /$$$$$$| $$  \ $$ /$$$$$$  /$$$$$$ /$$ /$$$$$$  /$$$$$$| $$   | $|_  $$    | $$$$\ $$"
      "\n| $$      /$$__  $$/$$_____| $$$$$$$//$$__  $$/$$__  $| $$|____  $$/$$__  $|  $$ / $$/ | $$    | $$ $$ $$"
      "\n| $$     | $$  \ $| $$     | $$__  $| $$$$$$$| $$  \ $| $$ /$$$$$$| $$  \ $$\  $$ $$/  | $$    | $$\ $$$$"
      "\n| $$     | $$  | $| $$     | $$  \ $| $$_____| $$  | $| $$/$$__  $| $$  | $$ \  $$$/   | $$    | $$ \ $$$"
      "\n| $$$$$$$|  $$$$$$|  $$$$$$| $$  | $|  $$$$$$|  $$$$$$| $|  $$$$$$|  $$$$$$/  \  $/   /$$$$$$/$|  $$$$$$/"
      "\n|________/\______/ \_______|__/  |__/\_______/\____  $|__/\_______/\______/    \_/   |______|__/\______/"
      "\n                                             /$$  \ $$"
      "\n                                            |  $$$$$$/"
      "\n                                             \______/")

print("___________________________________░▒▓█►─═ Bʏ Lᴜᴄᴀꜱ Fᴇʀᴇɪʀᴀ ═─►█▓▒░________________________________________________")

#Carregamento de Dados
Base = pd.read_excel('C:/Users/corpo/Desktop/Loc/Base.xlsx')
colunas = Base[['**Microzona**','FILIAL','Cod.','Transportadora','REGIAO','ROTA','|Microzona|','|Dias de frequência|',
                '|FREQ.|','Cod.Mun','Municipio da Microzona','UF','Capital ou Interior(X)?']]
cd1400 = colunas.loc[colunas['FILIAL'] == 1400, ['REGIAO','ROTA','|Dias de frequência|','Transportadora','**Microzona**',
                                                 'Municipio da Microzona','Capital ou Interior(X)?']]
#Seleção de Opções
menu = ("\n*----------------------------------------------* "
        "\n|Selecione uma Opção desejada:                 |"
        "\n|1 - Buscar por Região                         |"
        "\n|2 - Buscar por Rota                           |"
        "\n*----------------------------------------------*")
print(menu)

opcao = input("\n*----> "
                "Digite a Opção: ")

opcao1 = '1'
opcao2 = '2'


escolhad = 1
escolhad = 2


if opcao == '1':
    while opcao1 == '1':
            regiao = int(input('\n*----> Nº da Região: '))
            rst = cd1400.loc[cd1400['REGIAO'] == regiao, ['ROTA','|Dias de frequência|','Transportadora','**Microzona**',
                                                              'Municipio da Microzona','Capital ou Interior(X)?']]
            print(rst)
            escolhad = input('\n Deseja Fazer nova Consulta? '
                                '\n 1 - SIM \n 2 - NÃO'
                                '\n Digite a Opção: ')
            while escolhad == '1':

                break

            else:
                escolhad == '2'
                break

elif opcao == '2':
    while opcao == '2':
            rota = str.upper(input('\n*----> Nº da Rota: '))
            rst1 = cd1400.loc[cd1400['ROTA'] == rota, ['|Dias de frequência|','Transportadora','**Microzona**',
                                                               'Municipio da Microzona','Capital ou Interior(X)?']]
            print(rst1)
            escolhad = input('\n Deseja Fazer nova Consulta? '
                                 '\n 1 - SIM \n 2 - NÃO'
                                 '\n Digite a Opção: ')
            while escolhad == '1':

                break

            else:
                escolhad == '2'
                break


print("___________________________________░▒▓█►─═ Bʏ Lᴜᴄᴀꜱ Fᴇʀᴇɪʀᴀ ═─►█▓▒░________________________________________________"
      "\n______________________________  ░▒▓█►─═ In @teclucasferreira ═─►█▓▒░________________________________________________")

input('\n Precione Enter para sair! ')


