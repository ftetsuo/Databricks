# Databricks notebook source
import adal
import json
import requests
import pandas as pd

# COMMAND ----------

dbutils.widgets.text("region", "westus2")
dbutils.widgets.text("aas_name", "XXXXXXXXXXX") #AAS Server name
dbutils.widgets.text("model", "XXXXXXXXXXX") #AAS Database name
#dbutils.widgets.remove("region")
#dbutils.widgets.remove("aas_name")
#dbutils.widgets.remove("model")

# COMMAND ----------

location = getArgument('region')      
server_name = getArgument('aas_name') 
model = getArgument('model')          

# COMMAND ----------

tenant_id = 'XXXXXXXXXXX'
authentication_endpoint = f'https://login.windows.net/{tenant_id}'
resource  = f'https://{location}.asazure.windows.net/'
client_id = 'XXXXXXXXXXX'
client_secret = 'XXXXXXXXXXX'
# get an Azure access token using the adal library
context = adal.AuthenticationContext(authentication_endpoint)
token_response = context.acquire_token_with_client_credentials(resource, client_id, client_secret)

access_token = token_response.get('accessToken')
#print(access_token)

url = f'https://{location}.asazure.windows.net/servers/{server_name}/models/{model}/refreshes'

#table = '...'
#objects = [ dict(table=table) ]
#data = dict(
#    type = 'Full',
#    # CommitMode = 'transactional',
#    # MaxParallelism = 2,
#    RetryCount = 2,
#    Objects = objects,
#)

headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {access_token}',
}

#response = requests.post(url=url, headers=headers, data = json.dumps(data))
response = requests.get(url=url, headers=headers)

#print(response.text)
#print(response.status_code)

# COMMAND ----------

df = spark.createDataFrame(pd.read_json(response.text))

# COMMAND ----------

df.createOrReplaceTempView('vw_retorno_api')

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace temporary view vw_retorno_api_final
# MAGIC as
# MAGIC with cte00 as
# MAGIC (
# MAGIC   select
# MAGIC     * 
# MAGIC     ,row_number() over (order by cast(startTime as timestamp) desc) as seq
# MAGIC   from vw_retorno_api
# MAGIC )
# MAGIC select 
# MAGIC   *
# MAGIC from
# MAGIC   cte00
# MAGIC where
# MAGIC   seq = 1

# COMMAND ----------

df = spark.sql("select * from vw_retorno_api_final")

# COMMAND ----------

for row in df.collect():
  refresh_status = row.status

# COMMAND ----------

dbutils.notebook.exit(refresh_status)
