# Flask-lab

## Como subir 
Rode o comando na raiz do projeto `docker compose up`.
Ele construirá a imagem dentro do /app e iniciára primeiro o banco postgres e depois a aplicação em si.


### Notas
[blueprint](https://flask.palletsprojects.com/en/stable/blueprints/) é um mecanismo do flask pelo qual permite-se que isolem-se as rotas da aplicação por contexto como em evento#5 e depois a registre na aplicação principal como em app:16

Já o schemas.py permite-se que se separe a lógica do ORM (construção de queries) da lógica da aplicação aplicanod-se restrições, no caso de usuário, que seu número de identificação seja múltiplo de 2.

Já no modelos.py, criam-se os modelos dentro do banco e também aidiconam-se referencias no modelo presença. Especificamente sua relação com objetos usuario e evento. O backref cria a relação no sentido contrário também