# Databricks notebook source
# converte a tabela em um data frame spark
df = spark.sql("select * from table_name")

# COMMAND ----------

for row in df.collect():
  var1 = row.column_name