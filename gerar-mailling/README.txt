🚀 Como usar
Abra o arquivo
Dê dois cliques no arquivo gerar_mailling.exe.

Passo 1: Selecione a pasta de saída
Clique no botão Selecionar Pasta de Saída.
Essa será a pasta onde o arquivo final .txt será salvo.

Passo 2: Selecione a campanha
No menu suspenso, escolha uma das campanhas:

TRAT_OS_PEND_FIB_EMP

CRV_ATIVO_NOVA_FIBRA

CRV_MIGRACAO_FIBRA

PESQUISA_NPS_ND

PESQUISA_NPS2_ND

PESQUISA_NPS3_ND

⚠️ Para campanhas NPS, o sistema faz ajustes automáticos nos dados (como UF, data, etc.).

Passo 3: Selecione o arquivo de entrada
Clique em Iniciar Processo e selecione o arquivo .csv, .xlsx ou .zip.

📝 Resultado
O arquivo gerado será salvo com o nome da campanha, data e hora, no formato .txt.

Caso alguma coluna ultrapasse o limite de caracteres permitido, o programa criará um arquivo com os erros, como:

Copy
Edit
CRV_MIGRACAO_FIBRA_erros.txt
Você poderá abrir esse arquivo para corrigir os dados.

📦 Tipos de arquivos aceitos
.csv separado por ponto e vírgula (;)

.xlsx (planilhas Excel)

.zip contendo um único .csv ou .xlsx

❗ Importante
O programa não altera os arquivos originais.

O arquivo .txt gerado segue formato de largura fixa, exigido por sistemas de importação.

Cada coluna tem um limite de caracteres. Valores maiores são cortados ou geram erro.

📁 Exemplo de uso
Selecione: C:\Usuários\Maillings\Saida

Campanha: PESQUISA_NPS_ND

Arquivo: mailling_junho.xlsx

Resultado:

PESQUISA_NPS_ND_18062025_20H30.txt

PESQUISA_NPS_ND_18062025_20H30_erros.txt (se aplicável)