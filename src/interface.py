import customtkinter as ctk
import threading
from Main import iniciar_automacao
from tkinter import filedialog

#  Configurações visuais 
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Cor do botão


# Cria a janela principal (a base)
janela = ctk.CTk()
janela.geometry("400x250") # Largura x Altura
janela.title("Robô de Manutenção - ERP")

janela.iconbitmap('src\images\logo.ico')  # Ícone da janela (substitua pelo caminho do seu ícone)

#  Adiciona textos (Labels)
texto_titulo = ctk.CTkLabel(janela, text="Robô de Manutenção - ERP", font=("Arial", 20, "bold"))
texto_titulo.pack(pady=20) # O .pack() "joga" o elemento na tela. O pady dá um espaço (margem)

texto_instrucao = ctk.CTkLabel(janela, text="Clique no botão abaixo para buscar \nnovas Ordens de Serviço no sistema.")
texto_instrucao.pack(pady=10)

caminho_planilha_selecionada = ""

def escolher_arquivo():
    global caminho_planilha_selecionada
    caminho = filedialog.askopenfilename(
        title="Selecione a planilha de Ordens de Serviço",
        filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
    )
    if caminho:
        caminho_planilha_selecionada = caminho
        # Atualiza um texto na tela para mostrar que o arquivo foi carregado
        texto_resultado.configure(text=f"Arquivo selecionado: {caminho.split('/')[-1]}")

        # Variável global para armazenar o caminho da planilha selecionada


# Botão para abrir o explorador de arquivos
botao_arquivo = ctk.CTkButton(janela, text="Selecionar Planilha", command=escolher_arquivo)
botao_arquivo.pack(pady=5)

def executar_2_plano():
    if not caminho_planilha_selecionada:
        texto_resultado.configure(text="Erro: Selecione uma planilha primeiro!")
        return

    # Passa o caminho escolhido pelo usuário para o robô
    resultado = iniciar_automacao(caminho_planilha_selecionada)
    texto_resultado.configure(text=resultado)
   
    texto_resultado.configure(text=resultado)
def executar_com_feedback():
    hilo_robo = threading.Thread(target=executar_2_plano)
    
        # Dispara a thread para correr em segundo plano
    hilo_robo.start()
        # Exibe o resultado na tela

#  Adiciona o botão
botao_executar = ctk.CTkButton(janela, text="Buscar OS", command=executar_com_feedback, font=("Arial", 14))
botao_executar.pack(pady=10)

#  Adiciona um label para exibir o resultado
texto_resultado = ctk.CTkLabel(janela, text="", font=("Arial", 12))
texto_resultado.pack(pady=10)

# Inicia o loop da interface gráfica
janela.mainloop()



