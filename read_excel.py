# Databricks notebook source
# MAGIC %python
# MAGIC 
# MAGIC # le arquivo Excel -> necessario instalar biblioteca “crealytics/spark-excel” no cluster em que sera executado o notebook
# MAGIC # https://mayur-saparia7.medium.com/reading-excel-file-in-pyspark-databricks-notebook-c75a63181548
# MAGIC 
# MAGIC filePath = "/mnt/amsbradls2a4a/inbound/external-files/sharepoint_origenes/sellout/depara_clientes/stage/SELLOUT_DEPARA_CLIENTES_SHAREPOINT_NOVO.xlsx"
# MAGIC 
# MAGIC df = spark.read.format("com.crealytics.spark.excel")\
# MAGIC                .option("useHeader", "false")\
# MAGIC                .option("inferSchema", "false")\
# MAGIC                .load(filePath, header = 'true')

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC import pandas as pd
# MAGIC 
# MAGIC # le arquivo Excel com Pandas, a partir do nome na planilha e pulando linhas, realizando leitura a partir da linha 5, gerando data frame Pandas
# MAGIC 
# MAGIC path = "/dbfs/mnt/amsbradls2a4a/inbound/external-files/sharepoint_origenes/sellout/calendario"
# MAGIC file_name = "00017_CALENDARIO_SELLOUT.xlsx"
# MAGIC 
# MAGIC df = pd.read_excel(fr'{path}/{file_name}', sheet_name='DADOS', skiprows = range(1, 4))
# MAGIC 
# MAGIC df

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC import pandas as pd
# MAGIC 
# MAGIC # le arquivo Excel com Pandas, a partir do índice da planilha, gerando data frame Pandas
# MAGIC 
# MAGIC path = "/dbfs/mnt/amsbradls2a4a/inbound/external-files/sharepoint_origenes/sellout/calendario"
# MAGIC file_name = "00017_CALENDARIO_SELLOUT.xlsx"
# MAGIC 
# MAGIC df = pd.read_excel(fr'{path}/{file_name}', sheet_index='0')
# MAGIC 
# MAGIC df

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC # convertendo data frame Pandas para Spark
# MAGIC 
# MAGIC sparkDF = spark.createDataFrame(df)