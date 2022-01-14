# Databricks notebook source
import zipfile  
import os
import shutil

# COMMAND ----------

# movendo para diretorio onde o arquivo que será compactado se encontra
os.chdir('/dbfs/mnt/amsbradls2a4a/inbound/external-files/sellout/pesquisa/archive/')

# COMMAND ----------

# cria arquivo zip em diretorio temporario do Databricks e adiciona arquivo desejado no arquivo zip
with zipfile.ZipFile('/tmp/sample2.zip', 'w', zipfile.ZIP_DEFLATED) as zipObj2:
  zipObj2.write('SELLOUT_PESQUISA_BARCELOS & CIA_C38_20210929114223.csv')

# COMMAND ----------

# move do diretorio temporario do Databricks para diretorio onde arquivo original estava no Databricks
shutil.move('/tmp/sample2.zip','SELLOUT_PESQUISA_BARCELOS & CIA_C38_20210929114223.csv.zip')

# COMMAND ----------

# apaga arquivo original
os.remove('SELLOUT_PESQUISA_BARCELOS & CIA_C38_20210929114223.csv')