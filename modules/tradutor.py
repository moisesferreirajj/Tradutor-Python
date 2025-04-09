from deep_translator import GoogleTranslator


class Tradutor:
    def __init__(self):
        pass
    @staticmethod
    def traduzir_texto(texto):
        try:
            translated = GoogleTranslator(source='auto', target='pt').translate(texto)
            return translated
        except Exception as e:
            print(f"Erro ao traduzir: {e}")
            return texto