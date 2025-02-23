# Tradutor Automático de Arquivos de Texto

<div align="center">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="50" height="50" />
    <br>
</div>

Este é um projeto Python para traduzir arquivos de texto, linha por linha, utilizando a biblioteca **Deep Translator**. O script identifica o idioma de cada linha e traduz automaticamente para o português, mantendo o formato original do arquivo. É ideal para processar arquivos de localização ou conteúdos multilíngues.

## Recursos Principais
- **Detecção Automática de Idiomas**: Usa a biblioteca `langdetect` para identificar o idioma de cada linha.
- **Tradução Precisa**: Utiliza o **Deep Translator** para traduzir conteúdo automaticamente para o português.
- **Processamento em Lote**: Traduz grandes arquivos linha por linha, garantindo que cada progresso seja salvo automaticamente.
- **Interface Simples**: Usa o `tqdm` para exibir uma barra de progresso em tempo real durante a tradução.

## Dependências
O projeto utiliza as seguintes bibliotecas Python:

- **[Deep Translator]**: Para realizar a tradução automática.
- **[Langdetect]**: Para detectar o idioma de cada linha.
- **[TQDM]**: Para exibir uma barra de progresso interativa durante a execução do script.

## Uso
1. Insira o arquivo de texto que deseja traduzir no diretório do projeto.
2. Atualize as variáveis `input_file` e `output_file` no script principal para corresponder ao arquivo de entrada e ao nome do arquivo traduzido.

### Certifique que seu python está instalado com o comando abaixo:<br>
``
python --version
``
Após a certeza, basta seguir o passo-a-passo abaixo:<br>
- Dentro da pasta "Requirements":<br>
``
python -m venv venv
``
- Após isso ainda na pasta "Requirements":<br>
``
pip install -r requirements.txt
``
- Verifique se todas bibliotecas foram instaladas:<br>
``
pip list
``
5. O arquivo traduzido será salvo automaticamente com o nome especificado em `output_file`.

### Exemplo de Entrada
Arquivo: `language.txt`
```txt
Mensagem1: Hello, how are you?
Mensagem2: Hediye etme başarılı
Mensagem3: Olá, tudo bem?
```

### Exemplo de Saída
Arquivo: `Language-pt_br.txt`
```txt
Mensagem1: Olá, como você está?
Mensagem2: Presente bem-sucedido
Mensagem3: Olá, tudo bem?
```

## Funcionalidades do Código
- **Tradução Condicional**: Apenas linhas que não estão em português são traduzidas.
- **Salvamento Contínuo**: O progresso é salvo linha por linha no arquivo de saída, garantindo que mesmo em caso de interrupções o trabalho já realizado não seja perdido.
- **Erro Tratado**: Caso ocorra um erro durante a detecção ou tradução, a linha original é mantida e o processo continua.

## Problemas Conhecidos
- A tradução pode ser lenta para arquivos muito grandes devido à dependência da API de tradução online.
- Traduções podem variar em qualidade dependendo do idioma de origem e do conteúdo.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma [issue](https://github.com/moisesferreirajj/Tradutor-Python) ou enviar um pull request.
