from deep_translator import GoogleTranslator
from langdetect import detect
from tqdm import tqdm

def traduzir_texto(texto):
    try:
        #TRADUZIR AUTOMATICAMENTE BUSCANDO A TRADUÇÃO DA LINHA
        translated = GoogleTranslator(source='auto', target='pt').translate(texto)
        return translated
    except Exception as e:
        print(f"Erro ao traduzir: {e}")
        return texto

def processar_arquivo(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    #ABRE UM ARRAY PARA TRADUZIR AS LINHAS UMA POR UMA
    translated_lines = []

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for idx, line in tqdm(enumerate(lines), desc="Traduzindo", unit="linha"):
            if ':' in line:
                prefix, text_to_translate = line.split(':', 1)
                try:
                    #DETECTA O IDIOMA DEPOIS DO SPLIT
                    detected_language = detect(text_to_translate.strip())
                    if detected_language != 'pt':
                        translated_text = traduzir_texto(text_to_translate.strip())
                        translated_line = f"{prefix}: {translated_text}\n"
                    else:
                        translated_line = line
                except Exception as e:
                    print(f"Erro ao detectar idioma: {e}")
                    translated_line = line
            else:
                translated_line = line

            translated_lines.append(translated_line)

            #SALVA AUTOMATICAMENTE O QUE ELE JÁ TRADUZIR
            out_file.writelines([translated_line])

    print(f"Arquivo traduzido gerado: {output_file}")


input_file = 'language.txt'
output_file = 'Language-pt_br.txt'
processar_arquivo(input_file, output_file)
