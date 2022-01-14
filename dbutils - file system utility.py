# Databricks notebook source
# DBTITLE 1,Referência
# https://docs.databricks.com/dev-tools/databricks-utils.html

# COMMAND ----------

# DBTITLE 1,Obter ajuda para utilizar algum método
# MAGIC %python
# MAGIC 
# MAGIC # https://docs.databricks.com/dev-tools/databricks-utils.html#list-available-utilities
# MAGIC # To list available utilities along with a short description for each utility, run dbutils.help() for Python or Scala.
# MAGIC # This example lists available commands for the Databricks Utilities.
# MAGIC 
# MAGIC dbutils.fs.help()

# COMMAND ----------

# DBTITLE 1,Copiar arquivo
# MAGIC %python
# MAGIC 
# MAGIC # https://docs.databricks.com/dev-tools/databricks-utils.html#cp-command-dbutilsfscp
# MAGIC # Copies a file or directory, possibly across filesystems.
# MAGIC # This example copies the file named old_file.txt from /FileStore to /tmp/new, renaming the copied file to new_file.txt.
# MAGIC 
# MAGIC dbutils.fs.cp("/FileStore/old_file.txt", "/tmp/new/new_file.txt")

# COMMAND ----------

# DBTITLE 1,Exibe o conteúdo do arquivo
# MAGIC %python 
# MAGIC 
# MAGIC # https://docs.databricks.com/dev-tools/databricks-utils.html#head-command-dbutilsfshead
# MAGIC # Returns up to the specified maximum number bytes of the given file. The bytes are returned as a UTF-8 encoded string.
# MAGIC # This example displays the first 25 bytes of the file my_file.txt located in /tmp.
# MAGIC 
# MAGIC dbutils.fs.head("/tmp/my_file.txt", 25)

# COMMAND ----------

# DBTITLE 1,Lista conteúdo de um diretório
# MAGIC %python
# MAGIC 
# MAGIC # https://docs.databricks.com/dev-tools/databricks-utils.html#ls-command-dbutilsfsls
# MAGIC # Lists the contents of a directory.
# MAGIC 
# MAGIC dbutils.fs.ls("/tmp")

# COMMAND ----------

# DBTITLE 1,Cria diretório
# MAGIC %python
# MAGIC 
# MAGIC # https://docs.databricks.com/dev-tools/databricks-utils.html#mkdirs-command-dbutilsfsmkdirs
# MAGIC # Creates the given directory if it does not exist. Also creates any necessary parent directories.
# MAGIC 
# MAGIC dbutils.fs.mkdirs("/tmp/parent/child/grandchild")

# COMMAND ----------

# DBTITLE 1,Cria um mount
# MAGIC %python
# MAGIC 
# MAGIC # https://docs.databricks.com/dev-tools/databricks-utils.html#mount-command-dbutilsfsmount
# MAGIC # Mounts the specified source directory into DBFS at the specified mount point.
# MAGIC 
# MAGIC aws_bucket_name = "my-bucket"
# MAGIC mount_name = "s3-my-bucket"
# MAGIC 
# MAGIC dbutils.fs.mount("s3a://%s" % aws_bucket_name, "/mnt/%s" % mount_name)

# COMMAND ----------

# DBTITLE 1,Exibe mounts existentes
# MAGIC %python
# MAGIC 
# MAGIC # https://docs.databricks.com/dev-tools/databricks-utils.html#mounts-command-dbutilsfsmounts
# MAGIC # Displays information about what is currently mounted within DBFS.
# MAGIC 
# MAGIC dbutils.fs.mounts()
# MAGIC 
# MAGIC # Out[11]: [MountInfo(mountPoint='/mnt/databricks-results', source='databricks-results', encryptionType='sse-s3')]

# COMMAND ----------

# DBTITLE 1,Mover arquivo
# MAGIC %python
# MAGIC 
# MAGIC # https://docs.databricks.com/dev-tools/databricks-utils.html#mv-command-dbutilsfsmv
# MAGIC # Moves a file or directory, possibly across filesystems. A move is a copy followed by a delete, even for moves within filesystems.
# MAGIC 
# MAGIC dbutils.fs.mv("/FileStore/my_file.txt", "/tmp/parent/child/grandchild")

# COMMAND ----------

# DBTITLE 1,Criar arquivo texto
# MAGIC %python
# MAGIC 
# MAGIC # https://docs.databricks.com/dev-tools/databricks-utils.html#put-command-dbutilsfsput
# MAGIC # Writes the specified string to a file. The string is UTF-8 encoded.
# MAGIC # This example writes the string Hello, Databricks! to a file named hello_db.txt in /tmp. If the file exists, it will be overwritten.
# MAGIC 
# MAGIC dbutils.fs.put("/tmp/hello_db.txt", "Hello, Databricks!", True)

# COMMAND ----------

# DBTITLE 1,Limpa cache de mounts 
# MAGIC %python
# MAGIC 
# MAGIC # https://docs.databricks.com/dev-tools/databricks-utils.html#refreshmounts-command-dbutilsfsrefreshmounts
# MAGIC # Forces all machines in the cluster to refresh their mount cache, ensuring they receive the most recent information.
# MAGIC 
# MAGIC dbutils.fs.refreshMounts()

# COMMAND ----------

# DBTITLE 1,Deleta pasta ou arquivo
# MAGIC %python
# MAGIC 
# MAGIC # https://docs.databricks.com/dev-tools/databricks-utils.html#rm-command-dbutilsfsrm
# MAGIC # Removes a file or directory.
# MAGIC 
# MAGIC dbutils.fs.rm("/tmp/hello_db.txt")

# COMMAND ----------

# DBTITLE 1,Apaga mount
# MAGIC %python
# MAGIC 
# MAGIC # https://docs.databricks.com/dev-tools/databricks-utils.html#unmount-command-dbutilsfsunmount
# MAGIC # Deletes a DBFS mount point.
# MAGIC 
# MAGIC dbutils.fs.unmount("/mnt/<mount-name>")