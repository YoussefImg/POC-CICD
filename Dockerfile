# Basis Python image
FROM python:3.11-slim

# Werkdirectory binnen de container
WORKDIR /app

# Kopieer het requirements bestand
COPY requirements.txt .

# Installeer de Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Kopieer de applicatiecode
COPY . .

# Stel poort 8000 beschikbaar
EXPOSE 8000

# Startcommando van de applicatie
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
