# Criando Dashboard Fifa

### Preparando o ambiente
```sh
pip install virtualenv

virtualenv -p python venv

. venv/Scripts/activate
```

### Verificar tudo o que está instalado no ambiente virtual
```sh
pip freeze
```

### Gravando o que estiver instalado em um arquivo
```sh
pip freeze > requirements.txt
```

### Instalando os pacotes salvos no arquivo requiments
```sh
pip install -r requirements.txt
```