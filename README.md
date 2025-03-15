## sistema academico web

### Instruções de instalação

#### Criação de ambiente virtual e instalação de dependências 

```bash
git clone https://github.com/JuniorJose-git/sistema-academico-web.git
cd sistema-academico-web
```

#### Criação de ambiente virtual

```bash
python -m venv .venv
```

#### instalação de dependências
Windows:
```bash
.venv\bin\python -m pip install Flask-SQLAlchemy
```

Linux ou Mac:
```bash
python -m venv .venv
.venv/bin/python -m pip install Flask-SQLAlchemy
```

### Rodando ambiente de desenvolvimento

Windows:
```bash
.venv\bin\python -m flask --app sisweb.app run
```

Linux ou Mac:
```bash
.venv/bin/python -m flask --app sisweb.app run
```