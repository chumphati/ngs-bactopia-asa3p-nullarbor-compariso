FROM pansapiens/nullarbor
COPY entrypoint.sh /opt/entrypoint.sh
#copie du dossier contenant un dossier data avec les fichiers fastq et fasta et un fichier de configuration dans l'image
COPY nullarbor /app
WORKDIR /app
ENTRYPOINT ["/bin/bash", "/opt/entrypoint.sh"]
