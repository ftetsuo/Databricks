# Databricks notebook source
df = spark.sql("select * from table_name limit 3")
df_to_json = df.toJSON().collect()

# COMMAND ----------

dbutils.notebook.exit(df_to_json)
