# Databricks notebook source
# MAGIC %python
# MAGIC 
# MAGIC # https://docs.databricks.com/dev-tools/databricks-utils.html#run-command-dbutilsnotebookrun
# MAGIC 
# MAGIC # exemplos
# MAGIC notebook_path = "/Users/fabio.taira@br.nestle.com/utilities/execute_notebook" 
# MAGIC timeout_seconds = 3600
# MAGIC 
# MAGIC # executando outro notebook sem passagem de parametros
# MAGIC dbutils.notebook.run(notebook_path, timeout_seconds)
# MAGIC 
# MAGIC # executando outro notebook com passagem de parametros
# MAGIC dbutils.notebook.run(notebook_path, timeout_seconds, {"variable_01": "any_value_01", "variable_02":"any_value_02"})

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC # obtendo parametros a partir de uma execução pai (notebook ou data factory)
# MAGIC variable = getArgument('variable_01')
# MAGIC 
# MAGIC # adiciona um widget para ajudar a debugar/tester um notebook que recebe parametros
# MAGIC dbutils.widgets.text("variable_01", "any_value_01")
# MAGIC 
# MAGIC # remove um widget para ajudar a debugar/tester um notebook que recebe parametros
# MAGIC dbutils.widgets.remove("var_datalake_ingest_path")

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC -- usando um paramtro recebido numa query sql
# MAGIC select *
# MAGIC from
# MAGIC   $variable_01