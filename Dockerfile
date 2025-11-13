# Utiliser une image officielle Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Commande exécutée au lancement du conteneur
CMD ["python", "app.py"]
