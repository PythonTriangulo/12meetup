# Python Triangulo

Aplicação lambda rodando um serviço REST usando bottle e zappa

## Passos

```
virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt

python application.py
```

## AWS e Zappa

É necessário criar e configurar conta na AWS

```
zappa init
zappa deploy dev

# para atualizar o código na AWS
zappa update dev
```
