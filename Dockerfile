FROM python:3.9-slim

WORKDIR /app

# Copie os arquivos necessários para o contêiner
COPY  . .

# Instale as dependências da aplicação
RUN pip install fastapi uvicorn psycopg2-binary

# Exponha a porta em que a aplicação será executada
EXPOSE 5000

# Comando para executar a aplicação quando o contêiner for iniciado
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]