# Lisa - API

Repositório da API de consulta de dados.

Após realizar o git clone do repositório, execute o seguinte comando para instalar as dependências do projeto.

```
pip install -r requirements.txt
```

Criar configuração d projeto
```
python setup.py install
```

# Para iniciar o servidor
Linux - Mac
```
gunicorn --reload lisa.app
```

Windows
```
waitress-serve --port=8000 lisa.app:api
```

Enjoy :)