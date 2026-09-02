import xlwings as xw
import openpyxl as xl

def inserir_dados_rpa(dados_os,caminho_arquivo):
    
    app = xw.App(visible=False)   
    try:   
        wb = app.books.open(caminho_arquivo)
        planilha = wb.sheets['Ordens de Serviço Máquinas']
        
        for os_atual  in dados_os:               
           ultima_linha = planilha.range('A' + str(planilha.cells.last_cell.row)).end('up').row
           linha_vazia = ultima_linha + 1
           lista_os = [os_atual['ID'],os_atual['PLACA'],
                       os_atual['DATA_ABERTURA'],None,None,
                       os_atual['CLASSIFICACAO'],
                       os_atual['TIPO'],None,None,None,None,None,None,None,
                       os_atual['SERVICO_SOLICITADO'],None]
           
           planilha.range(f'A{linha_vazia}').value = [lista_os]
          
        wb.save()
        print("Abrindo o Excel...\n✅ Dados inseridos com sucesso na planilha!")
    finally:
        
        wb.close()
        app.quit()
