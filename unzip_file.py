# Databricks notebook source
# MAGIC %md Descompacta arquivo zip closeup

# COMMAND ----------

# MAGIC %python
# MAGIC import os 
# MAGIC import zipfile
# MAGIC 
# MAGIC unzip_file_path = "/dbfs/mnt/amsbradls2a4a/inbound/external-files/sellout/closeup/fact/unzipfile/"
# MAGIC 
# MAGIC zip_file_path =  "/dbfs/mnt/amsbradls2a4a/inbound/external-files/sellout/closeup/fact/zipfile/"  ##  caminho do arquivo zip
# MAGIC 
# MAGIC file_list = os.listdir("/dbfs/mnt/amsbradls2a4a/inbound/external-files/sellout/closeup/fact/zipfile/") ##  caminho do arquivo zip
# MAGIC 
# MAGIC for file in file_list:
# MAGIC    if file.endswith('.zip'):    ## listar os arquivos extesão zip
# MAGIC     x = zip_file_path + file
# MAGIC     print (x)
# MAGIC zip = zipfile.ZipFile(x)
# MAGIC zip.extractall(unzip_file_path) 
# MAGIC zip.close()