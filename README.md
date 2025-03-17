## sistema academico web

### Instruções de instalação

###  Criação de ambiente virtual e instalação de dependências 
---
#### Clonagem de repositório
```bash
git clone https://github.com/JuniorJose-git/sistema-academico-web.git
cd sistema-academico-web
```

#### Criação de ambiente virtual

```bash
python -m venv .venv
```
---
#### instalação de dependências
Windows:
```bash
.venv\scripts\python -m pip install Flask-SQLAlchemy pymysql
```

Linux ou Mac:
```bash
.venv/bin/python -m pip install Flask-SQLAlchemy pymysql
```
---
### Rodando ambiente de desenvolvimento

Windows:
```bash
.venv\scripts\python -m flask --app sisweb.app run
```

Linux ou Mac:
```bash
.venv/bin/python -m flask --app sisweb.app run
```