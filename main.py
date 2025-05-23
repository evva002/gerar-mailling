import tkinter
from tkinter import ttk
from criar_pastas import criar_nova_pasta
from conversor_mailling import conversor_normal

# janela principal
janela_principal = tkinter.Tk()
janela_principal.title('Gerar Mailling')
janela_principal.geometry('300x140')

# caixa de texto campanhas
label = tkinter.Label(janela_principal, text='Selecione a campanha:')
label.pack(pady=10)

# campanhas cadastradas para conversao
campanhas = ['Campanha_A', 'Campanha_B', 'Campanha_C']
combo_campanhas = ttk.Combobox(janela_principal, values=campanhas, state='readonly')
combo_campanhas.current(0)
combo_campanhas.pack()

# botao iniciar processo
botao_iniciar = tkinter.Button(janela_principal, text='Iniciar processo', command=lambda: conversor_normal(combo_campanhas))
botao_iniciar.pack(pady=20)

janela_principal.mainloop()