import os
from deep_translator import GoogleTranslator
from tqdm import tqdm

# FUNÇÃO PARA TRADUZIR O TEXTO COMPLETO
def traduzir_texto_completo(texto):
    try:
        # NÃO TRADUZIR PARTES ESPECÍFICAS COMO --- RECORDSEPARATOR ---
        partes = texto.split('--- RECORDSEPARATOR ---')
        partes_traduzidas = []
        for parte in partes:
            if parte.strip():
                # TRADUZ APENAS O TEXTO FORA DO RECORDSEPARATOR
                traduzido = GoogleTranslator(source='auto', target='pt').translate(parte.strip())
                partes_traduzidas.append(traduzido)
            else:
                partes_traduzidas.append('')  # PRESERVA SEÇÃO VAZIA

        # REINSERE O --- RECORDSEPARATOR ---
        return '\n--- RECORDSEPARATOR ---\n'.join(partes_traduzidas)
    except Exception as e:
        print(f"Erro ao traduzir: {e}")
        return texto

# FUNÇÃO PARA PROCESSAR UM ÚNICO ARQUIVO
def processar_arquivo(input_file, output_folder):
    with open(input_file, 'r', encoding='utf-8') as file:
        # LÊ TODO O CONTEÚDO DO ARQUIVO
        texto = file.read()

    # TRADUZ TODO O TEXTO
    texto_traduzido = traduzir_texto_completo(texto)

    # CAMINHO DO NOVO ARQUIVO TRADUZIDO
    output_file = os.path.join(output_folder, os.path.basename(input_file))

    # SALVA O TEXTO TRADUZIDO
    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write(texto_traduzido)

    print(f"Arquivo traduzido salvo em: {output_file}")

# FUNÇÃO PARA PROCESSAR TODOS OS ARQUIVOS DE UMA PASTA
def processar_pasta(input_folder, output_folder):
    # CRIA A PASTA DE SAÍDA SE NÃO EXISTIR
    os.makedirs(output_folder, exist_ok=True)

    # LISTA TODOS OS ARQUIVOS .TXT NA PASTA DE ENTRADA
    arquivos_txt = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.txt')]

    for arquivo in tqdm(arquivos_txt, desc="Traduzindo arquivos", unit="arquivo"):
        print(f"Processando arquivo: {arquivo}")
        processar_arquivo(arquivo, output_folder)

# DEFINA AS PASTAS DE ENTRADA E SAÍDA
input_folder = 'texts'  # PASTA COM OS ARQUIVOS ORIGINAIS
output_folder = 'texts_traduzidos'  # PASTA PARA SALVAR OS ARQUIVOS TRADUZIDOS

# INICIA O PROCESSO DE TRADUÇÃO
processar_pasta(input_folder, output_folder)