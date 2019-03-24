# Aula Flask
![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/1200px-Flask_logo.svg.png)

## Introdução

#### Instalando o Flask
`pip install Flask`

#### Executar o arquivo 
`python app.py`

## Preparando o ambiente
`pip install virtualenv`

#### Iniciando o  virtualenv
`virtualenv -p python3 venv`

#### executando o ambiente virtual
`. venv/bin/activate`

#### Verificar tudo o que está instalado no ambiente virtual
`pip3 freeze`

#### Gravando o que estiver instalado em um arquivo
`pip3 freeze > requirements.txt`

#### Instalando os pacotes salvos no aquivo requiments
`pip3 install -r requirements.txt`

#### Ordenando as pastas (MVC)
> - controllers

> - models

> views: (é divida em duas pastas)
>> - static

>> - templates