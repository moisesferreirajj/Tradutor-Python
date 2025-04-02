import pyodbc
from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException
from tqdm import tqdm
import re

def conectar_ao_banco():
    try:
        # CONFIGURE OS DADOS DE CONEXÃO DO SQL SERVER
        conexao = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=MOISES-PC\\SQL;"
            "DATABASE=Db_Tank;"
            "UID=sa;"
            "PWD=251425"
        )
        print("Conexão com o banco estabelecida!")
        return conexao
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None

def traduzir_texto(texto):
    try:
        if not texto or not re.search(r'\w', texto):  # Verifica se o texto está vazio ou contém apenas caracteres não alfanuméricos
            return texto
        # TRADUZIR AUTOMATICAMENTE O TEXTO PARA PORTUGUÊS
        translated = GoogleTranslator(source='auto', target='pt').translate(texto)
        # Garante que a primeira letra seja maiúscula
        translated = translated[0].upper() + translated[1:] if translated else translated
        return translated
    except Exception as e:
        print(f"Erro ao traduzir: {e}")
        return texto

def traduzir_colunas(conexao, tabela, colunas):
    try:
        cursor = conexao.cursor()
        # SELECIONA TODAS AS LINHAS DA TABELA PARA AS COLUNAS QUE DEVEM SER TRADUZIDAS
        query_select = f"SELECT ActiveID, {', '.join(colunas)} FROM {tabela}"
        cursor.execute(query_select)
        registros = cursor.fetchall()

        for registro in tqdm(registros, desc="Traduzindo registros", unit="registro"):
            id_atual = registro[0]
            valores_traduzidos = []

            for i, texto in enumerate(registro[1:], 1):
                if texto and len(texto) > 1:  # Garante que o texto tenha mais de 1 caractere
                    try:
                        if detect(texto) != 'pt':  # Detecta idioma e verifica se precisa traduzir
                            texto_traduzido = traduzir_texto(texto)
                            valores_traduzidos.append(texto_traduzido)
                        else:
                            valores_traduzidos.append(texto)  # Mantém o valor original se não precisar traduzir
                    except LangDetectException:
                        print(f"Não foi possível detectar o idioma para o texto: {texto}")
                        valores_traduzidos.append(texto)  # Adiciona o texto original caso não consiga detectar o idioma
                else:
                    valores_traduzidos.append(texto)  # Adiciona o texto original se for vazio ou curto demais

            # ATUALIZA OS VALORES TRADUZIDOS NO BANCO
            query_update = f"UPDATE {tabela} SET {', '.join([f'{col} = ?' for col in colunas])} WHERE ActiveID = ?"
            cursor.execute(query_update, (*valores_traduzidos, id_atual))
            conexao.commit()
            print(f"Registro ID {id_atual} atualizado com sucesso!")

        cursor.close()
    except Exception as e:
        print(f"Erro ao traduzir colunas: {e}")

# CONFIGURAÇÕES
tabela = "Active"
colunas = ["Title", "Description", "Content", "AwardContent", "ActionTimeContent"]  # Colunas que serão traduzidas

# EXECUÇÃO
conexao = conectar_ao_banco()
if conexao:
    traduzir_colunas(conexao, tabela, colunas)
    conexao.close()
