from openpyxl import load_workbook
import openpyxl 

#Abre a planilha , vai até a última linha preenchida e captura o número da coluna ID.
#Retorno: Devolve um número inteiro (ex: 3). Se a planilha estiver vazia, devolve 0.

wb = load_workbook('Base de dados_Ordem_de_Serviço_Máquinas.xlsx')
planilha = wb["Ordens de Serviço Máquinas"]

def obter_ultimo_id():
    numero_ultima_linha = planilha.max_row

    id_encontrado = planilha.cell(row = numero_ultima_linha,column= 2).value
    return id_encontrado
    

Ultima_linha = obter_ultimo_id()

print(Ultima_linha)

