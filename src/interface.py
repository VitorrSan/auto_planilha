import customtkinter as ctk
from src.Main import iniciar_automacao

#  Configurações visuais 
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Cor do botão

# Cria a janela principal (a base)
janela = ctk.CTk()
janela.geometry("400x250") # Largura x Altura
janela.title("Robô de Manutenção - ERP")

#  Adiciona textos (Labels)
texto_titulo = ctk.CTkLabel(janela, text="Sincronizador de OS", font=("Arial", 20, "bold"))
texto_titulo.pack(pady=20) # O .pack() "joga" o elemento na tela. O pady dá um espaço (margem)

texto_instrucao = ctk.CTkLabel(janela, text="Clique no botão abaixo para buscar \nnovas Ordens de Serviço no sistema.")
texto_instrucao.pack(pady=10)

# O parâmetro 'command' é onde você liga o botão à função. 
# ATENÇÃO: É command=iniciar_automacao (SEM OS PARÊNTESES no final). 
# Se colocar parênteses, ele roda sozinho!
botao_iniciar = ctk.CTkButton(janela, text="▶ Atualizar Planilha",command=iniciar_automacao, width=200, height=40) 

botao_iniciar.pack(pady=20)


janela.mainloop()