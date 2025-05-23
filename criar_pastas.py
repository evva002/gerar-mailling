import sys
import os

def criar_nova_pasta():
    if getattr(sys, 'frozen', False):
        diretorio = os.path.dirname(sys.executable)
    else:
        diretorio = os.path.dirname(os.path.abspath(__file__))

    for nome in ['pasta-inicio', 'pasta-fim', 'pasta-lixeira']:
        caminho = os.path.join(diretorio, nome)
        os.makedirs(caminho, exist_ok=True)
