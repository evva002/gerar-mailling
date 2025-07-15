import tkinter
from tkinter import ttk, filedialog, messagebox
from conversor_mailling import iniciar_processo
import os
import sys

# Caminho base (onde está o .exe ou o .py)
BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
CAMINHO_CAMPANHAS = os.path.join(BASE_DIR, 'campanhas.txt')

janela_principal = tkinter.Tk()
janela_principal.title('Gerar Mailling')
janela_principal.geometry('370x370')  
janela_principal['background'] = '#B498E6'

pasta_saida_selecionada = None
campanhas = []

def carregar_campanhas():
    """Carrega a lista de campanhas do arquivo campanhas.txt"""
    global campanhas
    if not os.path.exists(CAMINHO_CAMPANHAS):
        campanhas_padrao = [
            'TRAT_OS_PEND_FIB_EMP',
            'CRV_ATIVO_NOVA_FIBRA',
            'CRV_MIGRACAO_FIBRA',
            'PESQUISA_NPS_ND',
            'PESQUISA_NPS2_ND',
            'PESQUISA_NPS3_ND'
        ]
        with open(CAMINHO_CAMPANHAS, 'w', encoding='utf-8') as f:
            f.write('\n'.join(campanhas_padrao))
        campanhas = campanhas_padrao
    else:
        with open(CAMINHO_CAMPANHAS, 'r', encoding='utf-8') as f:
            campanhas = [linha.strip() for linha in f if linha.strip()]

def salvar_campanhas():
    """Salva as campanhas no arquivo"""
    with open(CAMINHO_CAMPANHAS, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(campanhas, key=str.lower)))

def selecionar_pasta_saida():
    global pasta_saida_selecionada
    pasta_saida_selecionada = filedialog.askdirectory(title="Selecione a pasta de destino para o .txt")
    if pasta_saida_selecionada:
        messagebox.showinfo("Pasta selecionada", f"Saída será salva em:\n{pasta_saida_selecionada}")

def adicionar_campanha():
    nova = entrada_nova_campanha.get().strip()
    if nova and nova not in campanhas:
        campanhas.append(nova)
        salvar_campanhas()
        atualizar_combobox()
        entrada_nova_campanha.delete(0, tkinter.END)
    else:
        messagebox.showwarning("Aviso", "Nome inválido ou campanha já existente.")

def remover_campanha():
    nome = entrada_nova_campanha.get().strip()
    if nome in campanhas:
        campanhas.remove(nome)
        salvar_campanhas()
        atualizar_combobox()
        entrada_nova_campanha.delete(0, tkinter.END)
    else:
        messagebox.showwarning("Aviso", "Digite o nome exato da campanha que deseja remover.")

def atualizar_combobox():
    campanhas_ordenadas = sorted(campanhas, key=str.lower)
    combo_campanhas['values'] = campanhas_ordenadas
    if campanhas_ordenadas:
        combo_campanhas.current(0)

# --- Layout ---
label_pasta = tkinter.Label(janela_principal, text='1. Selecione a pasta de destino:', bg='#B498E6', fg='white')
label_pasta.pack(pady=5)

botao_selecionar_pasta = tkinter.Button(janela_principal, text='Selecionar Pasta de Saída', command=selecionar_pasta_saida, bg='#661CE6', fg='white')
botao_selecionar_pasta.pack(pady=5)

label_campanha = tkinter.Label(janela_principal, text='2. Selecione ou edite a campanha:', bg='#B498E6', fg='white')
label_campanha.pack(pady=10)

combo_campanhas = ttk.Combobox(janela_principal, state='readonly')
combo_campanhas.pack()

entrada_nova_campanha = tkinter.Entry(janela_principal)
entrada_nova_campanha.pack(pady=5)

frame_botoes = tkinter.Frame(janela_principal, bg='#B498E6')
frame_botoes.pack()

botao_adicionar = tkinter.Button(frame_botoes, text='+', command=adicionar_campanha, width=4, bg='#28A745', fg='white')
botao_adicionar.pack(side='left', padx=5)

botao_remover = tkinter.Button(frame_botoes, text='-', command=remover_campanha, width=4, bg='#DC3545', fg='white')
botao_remover.pack(side='left', padx=5)

label_processo = tkinter.Label(janela_principal, text='3. Selecione o arquivo para iniciar o processo de conversão:', bg='#B498E6', fg='white')
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

# Inicialização
carregar_campanhas()
atualizar_combobox()
janela_principal.mainloop()