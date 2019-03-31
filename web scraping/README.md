# Web Scraping

### virtualenv

### Iniciando o virtualenv
```sh
virtualenv -p python3 venv
```

### executando o ambiente virtual
```sh
. venv/bin/activate
```

### Instalando o requests
```sh
pip install requests
```

### Instalando o Beautiful Soup
```sh
pip3 install beautifulsoup4
```

### Instalando o lxml
```sh
pip install lxml
```

### Gravando o que estiver instalado em um arquivo
```sh
pip3 freeze > requirements.txt
```

### Instalando os pacotes salvos no arquivo
```sh
pip3 install -r requirements.txt
```