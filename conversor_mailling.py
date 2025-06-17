import os
import pandas
from tkinter import messagebox, filedialog
import chardet
from funcoes_nps import processar_nps
from funcoes_nps import iniciar_processo_conversao
from renomear import renomear_campanha
import zipfile
import io

def iniciar_processo(combo_campanhas, pasta_saida):
    if not pasta_saida:
        messagebox.showerror("Erro", "Primeiro selecione a pasta de destino!")
        return

    campanha = combo_campanhas.get()
    print(f'Campanha selecionada: {campanha}')

    planilha, encoding_detectado = ler_arquivo_csv()
    if planilha is None:
        return

    # Processamento especial para NPS (seja de ZIP ou não)
    if 'NPS' in campanha.upper():
        planilha = iniciar_processo_conversao(planilha)
        planilha = processar_nps(planilha)

    exportar_para_txt(planilha, campanha, encoding_detectado, pasta_saida)


def ler_arquivo_csv():
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo (.csv, .xlsx ou .zip)",
        filetypes=[("Arquivos suportados", "*.csv *.xlsx *.zip")]
    )

    if not caminho_arquivo:
        return None, None

    try:
        # Verifica se é um arquivo ZIP
        if caminho_arquivo.lower().endswith('.zip'):
            with zipfile.ZipFile(caminho_arquivo, 'r') as zip_ref:
                # Lista arquivos no ZIP
                arquivos_no_zip = [f for f in zip_ref.namelist() if f.lower().endswith(('.csv', '.xlsx'))]
                
                if not arquivos_no_zip:
                    messagebox.showerror('Erro', 'Nenhum arquivo .csv ou .xlsx encontrado no ZIP')
                    return None, None
                
                # Pega o primeiro arquivo válido (ou pode implementar uma seleção)
                arquivo_no_zip = arquivos_no_zip[0]
                
                # Detecta encoding
                with zip_ref.open(arquivo_no_zip) as f:
                    conteudo = f.read(10000)
                    resultado = chardet.detect(conteudo)
                    encoding_detectado = resultado['encoding']
                    print(f"Encoding detectado: {encoding_detectado}")
                
                # Lê o arquivo
                with zip_ref.open(arquivo_no_zip) as f:
                    if arquivo_no_zip.lower().endswith('.csv'):
                        planilha = pandas.read_csv(io.BytesIO(f.read()), encoding=encoding_detectado, sep=';', dtype=str)
                    else:
                        planilha = pandas.read_excel(io.BytesIO(f.read()), dtype=str)
                
                return planilha, encoding_detectado

        # Fluxo normal para arquivos não-ZIP
        with open(caminho_arquivo, 'rb') as f:
            resultado = chardet.detect(f.read(10000))
            encoding_detectado = resultado['encoding']
            print(f"Encoding detectado: {encoding_detectado}")

        if caminho_arquivo.lower().endswith('.csv'):
            planilha = pandas.read_csv(caminho_arquivo, encoding=encoding_detectado, sep=';', dtype=str)
        else:
            planilha = pandas.read_excel(caminho_arquivo, dtype=str)
        
        return planilha, encoding_detectado

    except Exception as erro:
        messagebox.showerror('Erro', f'Erro ao ler o arquivo:\n{str(erro)}')
        return None, None, None

def exportar_para_txt(planilha: pandas.DataFrame, campanha: str, encoding: str, pasta_saida: str):
    if not pasta_saida:
        messagebox.showerror("Erro", "Nenhuma pasta de destino selecionada!")
        return

    nome_campanha = renomear_campanha(campanha)

    caminho_arquivo = os.path.join(pasta_saida, f'{nome_campanha}.txt')
    caminho_log_erros = os.path.join(pasta_saida, f'{nome_campanha}_erros.txt')

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

    messagebox.showinfo("Sucesso", 
        f"Arquivo '{nome_campanha}.txt' exportado com sucesso para:\n{pasta_saida}")