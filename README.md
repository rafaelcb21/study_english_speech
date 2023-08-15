# TREINAR PRONUNCIA EM INGLES COM INTELIGENCIA ARTIFICIAL

Este projeto é para praticar pronuncia em ingles, você insere a frase e pronuncia a frase.
O modelo de Inteligencia Artificial Whisper da OPENAI irá converter a pronuncia em texto.
Dessa forma você poderá verificar se a IA está entendendo o que está sendo dito.

Existe um menu de navegação no qual você pode escutar novamente a frase, repetir, inserir outra frase.

## INSTALAÇÃO

```python
pip install -r requirements.txt

# para mais informações acesse o https://github.com/openai/whisper

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# Se precisar faça o upgrade de alguma lib caso apareca algum erro ao executar o codigo
pip install --upgrade <lib>

# para subir com o Warning
# Adicione 'nopython=True' dentro do decorator '@numba.jit()' no arquivo na linha 58
# *\lib\site-packages\whisper\timing.py:58

# Dessa forma:

@numba.jit(nopython=True)
# https://github.com/openai/whisper/discussions/1409

```