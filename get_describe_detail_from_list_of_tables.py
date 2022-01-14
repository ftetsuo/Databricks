# Databricks notebook source
import pandas as pd

# COMMAND ----------

list = ['tableA','tableB','tableC']

query = '''select 
  cast(format as string) as format
  ,cast(id as string) as id
  ,cast(name as string) as name
  ,cast(description as string) as description
  ,cast(location as string) as location
  ,cast(createdAt as string) as createdAt
  ,cast(lastModified as string) as lastModified
  --,cast(partitionColumns as string) as partitionColumns
  --,cast(numFiles as string) as numFiles
  --,cast(sizeInBytes as string) as sizeInBytes
  --,cast(properties as string) as properties
  --,cast(minReaderVersion as string) as minReaderVersion
  --,cast(minWriterVersion as string) as minWriterVersion
from
  describedDetailed
'''

pandasDF = pd.DataFrame()

for tableName in list:
  df = spark.sql(fr"describe detail {tableName}")
  df.createOrReplaceTempView("describedDetailed")
  pandasDF = pandasDF.append(spark.sql(fr"{query}").toPandas())
  
spark.conf.set("spark.sql.execution.arrow.enabled","true")
sparkDF = spark.createDataFrame(pandasDF)
sparkDF.createOrReplaceTempView("describedTables")

# COMMAND ----------

# MAGIC %sql
# MAGIC select  
# MAGIC   *
# MAGIC from 
# MAGIC   describedTables

# COMMAND ----------

# print the script of show create table 
showTablesDF = spark.sql("show tables from sales_dataset")
showTablesDF.createOrReplaceTempView("showTables")
for row in spark.sql("select * from showTables where tableName like '%something%'").collect():
  print(spark.sql(fr"show create table {row.database}.{row.tableName}").collect()[0][0])
