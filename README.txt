GERADOR DE MAILLING - GUIA

COMO USAR

1. Abra o arquivo
   Dê dois cliques no arquivo gerar_mailling.exe

PASSO A PASSO

PASSO 1: SELECIONE A PASTA DE SAÍDA
- Clique no botão "Selecionar Pasta de Saída".
- Essa será a pasta onde o arquivo final .txt será salvo.

PASSO 2: SELECIONE OU EDITE A CAMPANHA
- Use o menu suspenso para selecionar uma campanha já existente.
- OU digite o nome de uma nova campanha personalizada na caixa de texto.

ADICIONAR CAMPANHA PERSONALIZADA
- Digite o nome da nova campanha no campo de texto.
- Clique no botão "+" para adicioná-la à lista.
- A campanha será salva no arquivo "campanhas.txt" e estará disponível nas próximas execuções.

REMOVER CAMPANHA EXISTENTE
- Digite o nome exato da campanha no campo de texto.
- Clique no botão "-" para removê-la da lista.
- A campanha será excluída do arquivo "campanhas.txt".

OBSERVAÇÃO:
A lista de campanhas é carregada automaticamente do arquivo "campanhas.txt", permitindo que suas alterações permaneçam salvas mesmo após fechar o programa.

PASSO 3: SELECIONE O ARQUIVO DE ENTRADA
- Clique no botão "Iniciar Processo".
- Escolha o arquivo .csv, .xlsx ou .zip (com apenas um arquivo dentro).

RESULTADO
- O programa gera um arquivo .txt com o nome da campanha e data/hora, como por exemplo:
    PESQUISA_NPS_ND_18062025_2030.txt

- Se houver colunas com excesso de caracteres, será criado um arquivo com os erros:
    PESQUISA_NPS_ND_18062025_2030_erros.txt

TIPOS DE ARQUIVOS ACEITOS
- .csv (separado por ponto e vírgula ;)
- .xlsx (planilhas do Excel)
- .zip contendo um único .csv ou .xlsx

IMPORTANTE
- O programa não altera os arquivos originais.
- O arquivo .txt gerado segue o formato de largura fixa (colunas com tamanho máximo definido).
- Colunas com texto acima do limite podem ser cortadas ou gerar erros.
- Os erros vão para um arquivo de texto separado com o sufixo "_erros".

EXEMPLO DE USO

Pasta de saída: C:\Usuarios\Maillings\Saida
Campanha: PESQUISA_NPS_ND
Arquivo de entrada: mailling_junho.xlsx

Arquivos gerados:
- PESQUISA_NPS_ND_18062025_2030.txt
- PESQUISA_NPS_ND_18062025_2030_erros.txt (se aplicável)
