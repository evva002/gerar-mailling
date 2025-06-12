def processar_nps(planilha):
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

    def extrair_uf(telefone):
        try:
            telefone_str = str(int(float(telefone)))  # garante conversão para string sem .0
            ddd = telefone_str[:2]  # pega os dois primeiros dígitos
            return tabela_ddd.get(ddd, '')  # retorna UF correspondente ou string vazia
        except:
            return ''

    planilha['F'] = planilha['J'].apply(extrair_uf)  

    # Coluna W: cópia da coluna F
    planilha['W'] = planilha['F']

    # Coluna AT: data atual
    from datetime import datetime
    hoje = datetime.today().strftime('%d/%m/%Y')
    planilha['AT'] = hoje

    return planilha