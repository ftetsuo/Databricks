# Databricks notebook source
# MAGIC %md
# MAGIC ##### Parametros

# COMMAND ----------

# MAGIC %python
# MAGIC dbutils.widgets.text("var_path", "/mnt/amsbradls2a4a/inbound/sandbox")
# MAGIC dbutils.widgets.text("var_wildcard", ".txt")
# MAGIC dbutils.widgets.text("var_recursive", "True")

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ##### Realiza limpeza de arquivos de log no diretorio da camada bronze da tabela

# COMMAND ----------

import fnmatch
#https://docs.python.org/pt-br/3/library/fnmatch.html

path = getArgument('var_path')
wildcard = getArgument('var_wildcard')
recursive = bool(getArgument('var_recursive'))

files = dbutils.fs.ls(path)
for f in files:
  #print(f)
  if fnmatch.fnmatch(f.name, wildcard):
  #if wildcard in f.name:
    print(f)
    #dbutils.fs.rm(f.path, recursive)