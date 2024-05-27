FROM python:3.11.3-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copia o diretório do aplicativo Django para o contêiner
COPY . /app

# Define o diretório de trabalho para o contêiner
WORKDIR /app

# Exponha a porta 8000
EXPOSE 8000

# Atualiza o pip
RUN pip install --upgrade pip

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Adiciona comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=vercel_app.dev"]