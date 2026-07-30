# Usa uma imagem oficial do Python leve
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o ficheiro de dependências primeiro (ajuda no cache do Docker)
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código para dentro do container
COPY . .

# Expõe a porta que a aplicação vai usar
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app/app.py"]