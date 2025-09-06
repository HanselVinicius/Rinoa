# Rinoa Analysis Service

## Runing 

### Create a virtual env

```bash
python3 -m venv venv
```


### Activate this env

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

```bash
uvicorn src.main:app --reload 
```

### Formating, Linting, Type-Checking all in one

```bash
make check-all
```


### Migrations 

#### Generate Revision

```bash
alembic revision --autogenerate -m "revision comment"
```


#### Commit Migration

```bash
alembic upgrade head 
```