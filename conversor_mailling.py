import os
import sys
import pandas 
from tkinter import messagebox
from criar_pastas import criar_nova_pasta
import chardet

def ler_arquivo_csv():
    if getattr(sys, 'frozen', False):
        diretorio_atual = os.path.dirname(sys.executable)
    else:
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    pasta_inicio = os.path.join(diretorio_atual, 'pasta-inicio')
    arquivos_csv = [arquivo for arquivo in os.listdir(pasta_inicio) if arquivo.lower().endswith('.csv')]

    if not arquivos_csv:
        messagebox.showerror('Erro', 'Nenhum arquivo .csv encontrado na pasta-inicio')
        return None, None

    caminho_arquivo = os.path.join(pasta_inicio, arquivos_csv[0])

    try:
        with open(caminho_arquivo, 'rb') as f:
            resultado = chardet.detect(f.read(10000))
            encoding_detectado = resultado['encoding']
            print(f"Encoding detectado: {encoding_detectado}")
    except Exception as erro:
        messagebox.showerror('Erro', f'Erro ao detectar codificação:\n{str(erro)}')
        return None, None

    try:
        planilha = pandas.read_csv(caminho_arquivo, encoding=encoding_detectado, sep=';', dtype=str)
        messagebox.showinfo('Sucesso', f'Arquivo lido com sucesso: {arquivos_csv[0]}')
        return planilha, encoding_detectado
    except Exception as erro:
        messagebox.showerror('Erro', f'Erro ao ler o arquivo:\n{str(erro)}')
        return None, None


def exportar_para_txt(planilha: pandas.DataFrame, campanha: str, encoding: str):
    if getattr(sys, 'frozen', False):
        diretorio = os.path.dirname(sys.executable)
    else:
        diretorio = os.path.dirname(os.path.abspath(__file__))

    pasta_saida = os.path.join(diretorio, 'pasta-fim')
    os.makedirs(pasta_saida, exist_ok=True)

    caminho_arquivo = os.path.join(pasta_saida, f'{campanha}.txt')
    caminho_log_erros = os.path.join(pasta_saida, f'{campanha}_erros.txt')

    larguras = [
        20, 1, 14, 10, 15, 2, 15, 15, 60, 11, 11, 11, 11, 100, 15, 100, 5, 100, 50,
        100, 5, 8, 2, 3, 10, 5, 20, 4
    ] + [50] * 20

    erros = []

    for idx, (_, linha) in enumerate(planilha.iterrows(), start=2):
        for i, largura in enumerate(larguras):
            if i >= len(planilha.columns):
                continue
            valor = str(linha.iloc[i]) if not pandas.isna(linha.iloc[i]) else ""
            if len(valor) > largura:
                nome_coluna = planilha.columns[i]
                erros.append(
                    f"Linha {idx} (Excel), Coluna '{nome_coluna}': "
                    f"{len(valor)} caracteres (máximo {largura})."
                )

    if erros:
        with open(caminho_log_erros, 'w', encoding='utf-8') as f:
            f.write('\n'.join(erros))
        messagebox.showerror(
            "Erro de validação",
            f"Não foi possível exportar. Existem campos com excesso de caracteres.\n"
            f"Veja detalhes em:\n{caminho_log_erros}"
        )
        return

    with open(caminho_arquivo, 'w', encoding=encoding) as arquivo_saida:
        for _, linha in planilha.iterrows():
            colunas_formatadas = []
            for i, largura in enumerate(larguras):
                valor = str(linha.iloc[i]) if i < len(linha) and not pandas.isna(linha.iloc[i]) else ""
                valor = valor[:largura].ljust(largura)
                colunas_formatadas.append(valor)

            linha_txt = ''.join(colunas_formatadas)
            arquivo_saida.write(linha_txt + '\n')

    messagebox.showinfo("Sucesso", f"Arquivo '{campanha}.txt' exportado com sucesso para a pasta-fim.")


def conversor_normal(combo_campanhas):
    criar_nova_pasta()
    campanha = combo_campanhas.get()
    print(f'Campanha selecionada: {campanha}')

    planilha, encoding_detectado = ler_arquivo_csv()
    if planilha is not None and encoding_detectado is not None:
        exportar_para_txt(planilha, campanha, encoding_detectado)
        print('Processo concluído com sucesso.')
    else:
        print('Processo interrompido.')