# Databricks notebook source
# DBTITLE 1,Criar temp view com sql a partir de um file path de tabela delta no data lake
# MAGIC %sql
# MAGIC create or replace temporary view view_name 
# MAGIC as
# MAGIC select *
# MAGIC from
# MAGIC   delta.`/mount/...`

# COMMAND ----------

# DBTITLE 1,Criar temp view com sql a partir de uma tabela no dbfs
# MAGIC %sql
# MAGIC create or replace temporary view view_name 
# MAGIC as
# MAGIC select *
# MAGIC from
# MAGIC   table_name

# COMMAND ----------

# DBTITLE 1,Criar temp view com python a partir de um arquivo
# MAGIC %python
# MAGIC 
# MAGIC v_format = '' #delta | csv | json
# MAGIC v_option = '' #Header=True/False | inferSchema=True/False | delimiter=""
# MAGIC v_load   = '' #full file path
# MAGIC df = spark.read.format(v_format).option(v_option).load(v_load)
# MAGIC 
# MAGIC df.createOrReplaceTempView("view_name")

# COMMAND ----------

# DBTITLE 1,Criar temp view com python a partir de uma tabela no dbfs
# MAGIC %python
# MAGIC 
# MAGIC df = spark.sql("select * from table_name")
# MAGIC 
# MAGIC df.createOrReplaceTempView("view_name")