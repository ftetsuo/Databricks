# Databricks notebook source
# MAGIC %python
# MAGIC 
# MAGIC # exporta arquivo Excel
# MAGIC # https://mayur-saparia7.medium.com/reading-excel-file-in-pyspark-databricks-notebook-c75a63181548
# MAGIC 
# MAGIC filePath = "dbfs:/mnt/amsbradls2a4a/inbound/external-files/sharepoint_origenes/sellout/depara_clientes/SELLOUT_DEPARA_CLIENTES_SHAREPOINT.xlsx"
# MAGIC 
# MAGIC df.write.format("com.crealytics.spark.excel")\
# MAGIC         .option("dataAddress", "'SELLOUT_DEPARA_CLIENTES'!A1")\
# MAGIC         .option("header", "true")\
# MAGIC         .option("inferSchema", "false")\
# MAGIC         .mode("overwrite")\
# MAGIC         .save(filePath)