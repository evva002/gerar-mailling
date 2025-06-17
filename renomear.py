from datetime import datetime

def renomear_campanha(nome_base: str):

    agora = datetime.now()
    data_formatada = agora.strftime("%d%m%Y") 
    hora_formatada = agora.strftime("%HH%MM")   
    hora_formatada = hora_formatada.replace("%", "")  
    
    return f"{nome_base}_{data_formatada}_{hora_formatada}"