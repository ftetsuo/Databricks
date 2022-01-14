# Databricks notebook source
# os comandos abaixo executam apenas em ambiente Nestlé

# COMMAND ----------

# executar notebook que contém classe para importá-lo para este notebook
%run /sv_utilities/synapses/commons

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC # resgata dados de tabela sqldw para um data frame spark
# MAGIC df = get_data_dw("select * from sys.tables")

# COMMAND ----------

# MAGIC %python 
# MAGIC 
# MAGIC # salva dados de um data frame spark para uma tabela do sqldw
# MAGIC save_data_dw(df, "table_name")

# COMMAND ----------

# MAGIC %python 
# MAGIC 
# MAGIC # executa um comando sql no sqldw, o comando truncate table nao funciona por este framework
# MAGIC execute_stmt_dw("delete from table_name")