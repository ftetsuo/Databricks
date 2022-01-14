# Databricks notebook source
# MAGIC %python
# MAGIC #https://sparkbyexamples.com/pyspark/pyspark-create-an-empty-dataframe/
# MAGIC #https://sparkbyexamples.com/pyspark/pyspark-structtype-and-structfield/
# MAGIC #https://sparkbyexamples.com/spark/spark-sql-dataframe-data-types/
# MAGIC #https://mungingdata.com/pyspark/union-unionbyname-merge-dataframes/
# MAGIC 
# MAGIC from pyspark.sql.types import *
# MAGIC 
# MAGIC schema = StructType([
# MAGIC   StructField('database', StringType(), True),
# MAGIC   StructField('tableName', StringType(), True),
# MAGIC   StructField('isTemporary', BooleanType(), True)
# MAGIC   ])
# MAGIC 
# MAGIC df = spark.createDataFrame([], schema)
# MAGIC 
# MAGIC sd = spark.sql("show databases")
# MAGIC 
# MAGIC for db in sd.collect():
# MAGIC   showTables = spark.sql("show tables in " + db.databaseName)
# MAGIC   df = df.union(showTables)
# MAGIC 
# MAGIC df.createOrReplaceTempView("tmp_systables")

# COMMAND ----------

list = []

for tb in df.filter(df['isTemporary']=="false").collect():
  try:
    showCreate = spark.sql("show create table "+tb.database+"."+tb.tableName).first()["createtab_stmt"]
    #print(showCreate)
    list.append(showCreate)
  except Exception as e:
    #print(e)
    print("ERRO: show create table "+tb.database+"."+tb.tableName)

# COMMAND ----------

import pandas as pd

list_to_df = pd.DataFrame(list, columns=['create_stmt'])

spark.createDataFrame(list_to_df).createOrReplaceTempView("tmp_showcreatetable")

#list_to_df.createOrReplaceTempView("tmp_showcreatetable")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from tmp_showcreatetable 
# MAGIC where 
# MAGIC   create_stmt like '%/mnt/amsbradls2a4a/solutions/dataset/origenes/dsr4dsfato_aux%'
# MAGIC   or create_stmt like '%/mnt/amsbradls2a4a/solutions/external-files/sharepoint_origenes/sellout/pricing_criteria/tb_sellout_pricing_criteria%'
# MAGIC   or create_stmt like '%/mnt/amsbradls2a4a/inbound/external-files/sellout/calendario/data-quality-result/TB_CALENDARIO_SELLOUT%'

# COMMAND ----------

# MAGIC %sql
# MAGIC describe table sales_gold.tb_sellout_dim_calendario

# COMMAND ----------

# MAGIC %sql
# MAGIC describe table delta.`/mnt/amsbradls2a4a/inbound/external-files/sellout/calendario/data-quality-result/TB_CALENDARIO_SELLOUT`

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace temp view systables as
# MAGIC select distinct
# MAGIC   database
# MAGIC   ,tableName
# MAGIC   ,isTemporary
# MAGIC from
# MAGIC   tmp_systables
# MAGIC where
# MAGIC   isTemporary = false

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select * from systables 
# MAGIC where lower(tableName) like '%diario%' and lower(tableName) like '%ageing%'

# COMMAND ----------

# MAGIC %sql
# MAGIC describe table extended stock_gold.tb_rpa_ageing_diario

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select distinct database from systables order by database

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select distinct database from systables
# MAGIC where database like '%dataset%'

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select * from md_gold.tb_siso_ageing_diario limit 10

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select count(1) from md_gold.tb_siso_ageing_diario 

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC describe table md_gold.tb_siso_ageing_diario