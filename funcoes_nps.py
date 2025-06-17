import pandas
import os
import sys
from tkinter import messagebox

def iniciar_processo_conversao(planilha, caminho_original):
    print('Iniciando processamento direto...')

    colunas_alvo = ['COD_CPF_CGC', 'FONE_1', 'FONE_2', 'FONE_3', 'FONE_4']

    # Verifica se a planilha é válida
    if planilha is None or not isinstance(planilha, pandas.DataFrame):
        messagebox.showerror("Erro", "A planilha fornecida é inválida.")
        return None

    # Converte colunas específicas para Int64
    for coluna in colunas_alvo:
        if coluna in planilha.columns:
            planilha[coluna] = pandas.to_numeric(planilha[coluna], errors='coerce')
            planilha[coluna] = planilha[coluna].dropna().astype(int)
            planilha[coluna] = planilha[coluna].astype('Int64')

    # Cria nome do novo arquivo com base no original
    nome_base = os.path.splitext(os.path.basename(caminho_original))[0]
    nome_saida = nome_base + '.csv'

    # Define diretório onde salvar
    if getattr(sys, 'frozen', False):
        pasta_destino = os.path.dirname(sys.executable)
    else:
        pasta_destino = os.path.dirname(os.path.abspath(__file__))

    caminho_saida = os.path.join(pasta_destino, nome_saida)

    try:
        planilha.to_csv(caminho_saida, index=False, sep=';')
        messagebox.showinfo("Sucesso", f"Arquivo salvo com sucesso como:\n{caminho_saida}")
    except Exception as erro:
        messagebox.showerror("Erro", f"Erro ao salvar o arquivo:\n{str(erro)}")

    return planilha  # Retorna a planilha modificada caso outras funções queiram continuar


def processar_nps(planilha):
    # Remove a coluna chamada 'COLUNA', se existir
    if 'COLUNA' in planilha.columns:
        planilha = planilha.drop(columns=['COLUNA'])

    # Tabela de DDDs para conversão em UF
    tabela_ddd = {
        '11': 'SP', '12': 'SP', '13': 'SP', '14': 'SP', '15': 'SP', '16': 'SP', '17': 'SP', '18': 'SP', '19': 'SP',
        '21': 'RJ', '22': 'RJ', '24': 'RJ',
        '27': 'ES', '28': 'ES',
        '31': 'MG', '32': 'MG', '33': 'MG', '34': 'MG', '35': 'MG', '37': 'MG', '38': 'MG',
        '41': 'PR', '42': 'PR', '43': 'PR', '44': 'PR', '45': 'PR', '46': 'PR',
        '47': 'SC', '48': 'SC', '49': 'SC',
        '51': 'CR', '53': 'RS', '54': 'CR', '55': 'CR',
        '61': 'DF',
        '62': 'GO',
        '63': 'TO',
        '64': 'GO',
        '65': 'MT', '66': 'MT',
        '67': 'MS',
        '68': 'AC',
        '69': 'RO',
        '71': 'BA', '73': 'BA', '74': 'BA', '75': 'BA', '77': 'BA',
        '79': 'SE',
        '81': 'PE',
        '82': 'AL',
        '83': 'PB',
        '84': 'RN',
        '85': 'CE',
        '86': 'PI',
        '87': 'PE',
        '88': 'CE',
        '89': 'PI',
        '91': 'PA',
        '92': 'AM',
        '93': 'PA', '94': 'PA',
        '95': 'RR',
        '96': 'AP',
        '97': 'AM',
        '98': 'MA', '99': 'MA',
    }

    # Função para extrair UF a partir do DDD
    def extrair_uf(telefone):
        try:
            telefone_str = str(int(float(telefone)))
            ddd = telefone_str[:2]
            return tabela_ddd.get(ddd, '')
        except:
            return ''

    # Aplica UF baseada no FONE_1
    planilha['COD_FILIAL'] = planilha['FONE_1'].apply(extrair_uf)

    # Cópia da COD_FILIAL na coluna W
    planilha['UF'] = planilha['COD_FILIAL']

    # Data atual na coluna CAMPOX18
    from datetime import datetime
    hoje = datetime.today().strftime('%d/%m/%Y')
    planilha['AT'] = hoje

    return planilha
