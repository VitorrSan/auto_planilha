import re

from src.Conexao import conectar_erp
from dotenv import load_dotenv
load_dotenv()
from src.Ultimo_valor_planilha import obter_ultimo_id
from src.InserirDados import inserir_dados_rpa
import pymysql
from openpyxl import load_workbook
import logging

from xlwings import ret



# Configuração global do Diário de Bordo (Logging)
logging.basicConfig(
    filename='automacao_erp.log',
    level=logging.INFO,
    encoding='utf-8',
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

logging.info("Iniciando rotina de busca de Ordens de Servico.")



def iniciar_automacao():
    try: 
        conexao = conectar_erp()
        with conexao.cursor() as c:
            c.execute(f"SELECT * FROM ordem_servico where id >{obter_ultimo_id()}")
            res= c.fetchall()      
        conexao.close()

        if res:
            inserir_dados_rpa(res)
            logging.info(f"Sucesso! {len(res)} novas OSs foram inseridas na planilha.")
            return (f"Sucesso! {len(res)} novas OSs foram inseridas na planilha.")
        else:
            logging.info("Rotina finalizada. Nenhum registro novo encontrado.")
            return ("✅ Não há novos registros para inserir na planilha.")

    except pymysql.OperationalError as e:
        # Erros de conexão, timeout, banco fora do ar ou credenciais incorretas
        logging.error(f"Falha de conexão com o Banco de Dados. Detalhe: {e.args[1]}")
        return(f"Erro Operacional ({e.args[0]}): {e.args[1]}")
    
    except pymysql.ProgrammingError as e:
        # Erros de sintaxe SQL, tabela ou coluna não encontrada             
        logging.error("A planilha estava aberta por outro processo/usuário. Operação cancelada.")
        return(f"Erro de Sintaxe/Programação ({e.args[0]}): {e.args[1]}")
    
    except pymysql.IntegrityError as e:
        # Violação de chaves estrangeiras, chaves primárias duplicadas ou restrições
        logging.error("Erro de integridade de dados ao inserir registros no banco. Verifique se os dados estão corretos.")
        return(f"Erro de Integridade de Dados ({e.args[0]}): {e.args[1]}")
    
    except pymysql.InternalError as e:
        # Erros internos do servidor MySQL (ex: quebra de permissões durante a execução)
        logging.error("Erro interno do servidor MySQL. Verifique o estado do servidor e tente novamente.")
        return(f"Erro Interno do Servidor ({e.args[0]}): {e.args[1]}")

    except pymysql.Error as erro_conexao:
        logging.error(f"Falha de conexão com o Banco de Dados. Detalhe: {erro_conexao}")
        return(f"❌ Ocorreu um erro na conexão com o banco de dados: {erro_conexao}")

    except PermissionError as erro_arquivo:
        logging.error(f"❌ Ocorreu um erro ao abrir o arquivo: {erro_arquivo}")
        return(f"❌ Ocorreu um erro ao abrir o arquivo,Por favor, verifique se o arquivo 'Base de dados_Ordem_de_Serviço_Máquinas.xlsx' está aberto por outro usuário ou por outro programa e tente novamente {erro_arquivo}")
            
    except Exception as erro_geral:
        logging.error(f"❌ Ocorreu um erro na automação: {erro_geral}")
        return(f"❌ Ocorreu um erro na automação: {erro_geral}, \n Por favor contate a equipe de TI!")

