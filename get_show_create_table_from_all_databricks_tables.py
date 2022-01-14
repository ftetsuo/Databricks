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
# MAGIC select 
# MAGIC   *
# MAGIC from
# MAGIC   tmp_showcreatetable 

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
# MAGIC select distinct 
# MAGIC   database
# MAGIC from
# MAGIC   systables
# MAGIC order by
# MAGIC   database
