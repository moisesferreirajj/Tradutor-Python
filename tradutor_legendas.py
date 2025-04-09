import pysubs2
from tqdm import tqdm

from modules.tradutor import Tradutor

tradutor = Tradutor()
EXT_LEGENDAS = ["srt","ass"]
def traduzir_legenda(input_legenda : str):
    try:
        legenda_name_template = "{}.pob.{}"
        ext_legenda = input_legenda.split(".")[-1]
        nome_legenda  = input_legenda.replace(f".{ext_legenda}", "")
        if not ext_legenda in EXT_LEGENDAS:
            print("Formato de arquivo incorreto!")
            quit()
        legenda = pysubs2.load(input_legenda, "utf-8")
        for idx, line in tqdm(enumerate(legenda), desc="Traduzindo", unit=" linha"):
            linha_traduzida = tradutor.traduzir_texto(line.text)
            line.text = linha_traduzida
        legenda_pronta = legenda_name_template.format(nome_legenda, ext_legenda)
        legenda.save(legenda_pronta)
        print("Salvo em: ",legenda_pronta)
    except Exception as e:
        print("Ocorreu um erro: ", e)

if __name__ == "__main__":
    traduzir_legenda("CAMINHO DA LEGENDA")