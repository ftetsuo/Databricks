# Databricks notebook source
# MAGIC %python
# MAGIC 
# MAGIC import pandas as pd
# MAGIC 
# MAGIC # Salvar arquivo csv usando biblioteca Pandas
# MAGIC # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
# MAGIC 
# MAGIC destination_path = "/dbfs/mnt/amsbradls2a4a/Taira"
# MAGIC delimiter = ";"
# MAGIC 
# MAGIC sparkDF = spark.sql("select * from sales_gold.tb_sellout_dim_calendario limit 10")
# MAGIC 
# MAGIC pandasDF = sparkDF.toPandas()
# MAGIC 
# MAGIC # cria arquivo csv, por default mode = "w", escreve ou sobrescreve, para appendar definir mode = "a"
# MAGIC pandasDF.to_csv(destination_path+"/teste01.csv", sep=delimiter, index=False)
# MAGIC 
# MAGIC # cria arquivo csv com coluna adicional chamda seq contendo valores sequeciais (identity), por default mode = "w", escreve ou sobrescreve, para appendar definir mode = "a"
# MAGIC pandasDF.to_csv(destination_path+"/teste02.csv", sep=delimiter, index=True, index_label="seq")

# COMMAND ----------

# MAGIC %python 
# MAGIC 
# MAGIC # Salvar arquivo csv usando biblioteca do PySpark
# MAGIC # https://sparkbyexamples.com/spark/spark-write-dataframe-to-csv-file/
# MAGIC # https://sparkbyexamples.com/spark/spark-write-dataframe-single-csv-file/
# MAGIC 
# MAGIC sep = ";"
# MAGIC # diretorio que sera gerado o arquivo no Data Lake
# MAGIC work_dir = "/mnt/amsbradls2a4a/Taira/teste04"
# MAGIC dest_dir = "/mnt/amsbradls2a4a/Taira"
# MAGIC file_name = "teste04.csv"
# MAGIC 
# MAGIC df = spark.sql("select * from sales_gold.tb_sellout_dim_calendario limit 10")
# MAGIC 
# MAGIC # utilizando a biblioteca nativa do PySpark para gerar o arquivo csv, e necesario utilizar o método coalesce(1) para que apenas um arquivo csv seja gerado, do contrario varios arquivos csv particionados serão gerados. 
# MAGIC df.coalesce(1)\
# MAGIC   .write.format("csv")\
# MAGIC   .mode("overwrite")\
# MAGIC   .option("header", "true")\
# MAGIC   .options(delimiter=sep) \
# MAGIC   .save(work_dir, encoding='utf-8')
# MAGIC 
# MAGIC # obtendo nome (aleatório) do arquivo csv gerado
# MAGIC files = dbutils.fs.ls(work_dir)
# MAGIC csv_file = [x.path for x in files if x.path.endswith(".csv")][0]
# MAGIC # move o arquivo unico csv para o destino final já renomeado
# MAGIC dbutils.fs.mv(csv_file, dest_dir+"/"+file_name)
# MAGIC # remove o diretorio de trabalho
# MAGIC dbutils.fs.rm(work_dir, recurse = True)