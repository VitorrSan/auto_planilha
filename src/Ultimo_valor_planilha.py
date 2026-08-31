from openpyxl import load_workbook

#Abre a planilha , vai até a última linha preenchida e captura o número da coluna ID.
#Retorno: Devolve um número inteiro (ex: 3). Se a planilha estiver vazia, devolve 0.

def obter_ultimo_id():
    wb = load_workbook("C:\\Users\\vitor\\OneDrive\\Documentos\\auto\\Base de dados_Ordem_de_Serviço_Máquinas (1).xlsx")
    planilha = wb["Ordens de Serviço Máquinas"]

    numero_ultima_linha = planilha.max_row

    id_encontrado = planilha.cell(row = numero_ultima_linha,column= 1).value
    Ultima_linha = id_encontrado
    wb.close()
    return Ultima_linha    





