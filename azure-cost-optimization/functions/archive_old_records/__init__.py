import datetime
import azure.functions as func
from azure.cosmos import CosmosClient
from azure.storage.blob import BlobClient
import json

def main(mytimer: func.TimerRequest) -> None:
    client = CosmosClient("<COSMOS_URL>", "<COSMOS_KEY>")
    db = client.get_database_client("BillingDB")
    container = db.get_container_client("BillingRecords")

    cutoff_date = datetime.datetime.utcnow() - datetime.timedelta(days=90)

    query = f"SELECT * FROM BillingRecords b WHERE b.timestamp < '{cutoff_date.isoformat()}'"
    for record in container.query_items(query=query, enable_cross_partition_query=True):
        blob_client = BlobClient.from_connection_string("<BLOB_CONN_STR>", "<CONTAINER_NAME>", f"{record['id']}.json")
        blob_client.upload_blob(json.dumps(record), overwrite=True)
        container.delete_item(record, partition_key=record['partitionKey'])