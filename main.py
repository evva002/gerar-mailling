import tkinter
from tkinter import ttk, filedialog, messagebox
from conversor_mailling import iniciar_processo

# Janela principal
janela_principal = tkinter.Tk()
janela_principal.title('Gerar Mailling')
janela_principal.geometry('350x230')  
janela_principal['background'] = '#B498E6'  # Verde marinho

# Variável para armazenar a pasta de saída
pasta_saida_selecionada = None

def selecionar_pasta_saida():
    global pasta_saida_selecionada
    pasta_saida_selecionada = filedialog.askdirectory(title="Selecione a pasta de destino para o .txt")
    if pasta_saida_selecionada:
        messagebox.showinfo("Pasta selecionada", f"Saída será salva em:\n{pasta_saida_selecionada}")

# Botão para selecionar pasta de saída
label_pasta = tkinter.Label(janela_principal, 
                            text='1. Selecione a pasta de destino:', 
                            bg='#B498E6',
                            fg='white')
label_pasta.pack(pady=5)


botao_selecionar_pasta = tkinter.Button(
    janela_principal,
    text='Selecionar Pasta de Saída',
    command=selecionar_pasta_saida,
    bg='#661CE6',
    fg='white'
)
botao_selecionar_pasta.pack(pady=5)

# Caixa de seleção de campanhas
label_campanha = tkinter.Label(janela_principal, 
                               text='2. Selecione a campanha:',
                               bg='#B498E6',
                               fg='white')
label_campanha.pack(pady=10)

campanhas = ['TRAT_OS_PEND_FIB_EMP', 'CRV_ATIVO_NOVA_FIBRA', 'CRV_MIGRACAO_FIBRA', 'PESQUISA_NPS_ND', 'PESQUISA_NPS2_ND']
campanhas_ordenadas = sorted(campanhas, key=str.lower)
combo_campanhas = ttk.Combobox(janela_principal, values=campanhas_ordenadas, state='readonly')
combo_campanhas.current(0)
combo_campanhas.pack()

# Botão para iniciar o processo (que agora também seleciona o arquivo)
label_processo = tkinter.Label(janela_principal, 
                               text='3. Selecione o arquivo para iniciar o processo de conversão:',
                               bg='#B498E6',
                               fg='white')
label_processo.pack(pady=10)

botao_iniciar = tkinter.Button(
    janela_principal,
    text='Iniciar Processo',
    command=lambda: iniciar_processo(combo_campanhas, pasta_saida_selecionada),
    bg='#661CE6',  
    fg='white',
    width=15
)
botao_iniciar.pack(pady=15)

janela_principal.mainloop()