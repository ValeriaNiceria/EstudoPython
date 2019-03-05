# Flask
![alt text](https://cdn-images-1.medium.com/max/438/1*0G5zu7CnXdMT9pGbYUTQLQ.png)

## Gerenciando dependências e ambientes python com pipenv

### Instalando o pipenv
- verificando se o **pip** está instalado: `$ pip -V`
- instalando o **pip** no python 3: `$ sudo apt install python-pip`
- instalando o pipenv: `$ pip install pipenv`

## Criando o arquivo responsável pelo gerenciamento dos pacotes
```sh
pipenv --three
```

## Instalando o flask
```sh
pipenv install flask
```

## Criando o arquivo
```sh
touch app/__init__.py
```

## Como rodar um projeto flask
```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=true
```

```sh
flask run
```

```sh
pipenv install -d requests ipdb
```

```sh
ipython

from requests import get

get('http://127.0.0.1:5000/')
```

```sh

```

```sh

```