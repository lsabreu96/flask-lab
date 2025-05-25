# Usa imagem oficial Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia só a pasta app/
COPY app/ /app

# Copia também o requirements.txt
COPY requirements.txt /app

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define variáveis de ambiente
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expõe a porta padrão do Flask
EXPOSE 5000

# Comando para rodar o Flask
CMD ["flask", "run"]
