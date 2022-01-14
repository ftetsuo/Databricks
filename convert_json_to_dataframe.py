# Databricks notebook source
# MAGIC %python 
# MAGIC 
# MAGIC import pandas as pd
# MAGIC 
# MAGIC json_string = '[{"nome":"xpto"},{"nome":"xpto1", "idade":"10"}]'
# MAGIC 
# MAGIC df = spark.createDataFrame(pd.read_json(json_string))

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC df.show()