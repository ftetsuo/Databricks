# Databricks notebook source
# MAGIC %python
# MAGIC 
# MAGIC from pyspark.sql.functions import input_file_name
# MAGIC 
# MAGIC df = spark.read.csv("dbfs:/mnt/amsbradls2a4a/listaDatas.csv", header=True, sep=';', encoding='UTF-8').withColumn("file_name", input_file_name())

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC df.createOrReplaceTempView("tvw")

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select * from tvw

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC describe table tvw