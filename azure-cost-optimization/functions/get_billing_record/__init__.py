from azure.cosmos import CosmosClient, exceptions
from azure.storage.blob import BlobClient
import json

COSMOS_CLIENT = CosmosClient("<COSMOS_URL>", "<COSMOS_KEY>")
DB = COSMOS_CLIENT.get_database_client("BillingDB")
CONTAINER = DB.get_container_client("BillingRecords")

def get_record(record_id, partition_key):
    try:
        return CONTAINER.read_item(item=record_id, partition_key=partition_key)
    except exceptions.CosmosResourceNotFoundError:
        blob_client = BlobClient.from_connection_string("<BLOB_CONN_STR>", "<CONTAINER_NAME>", f"{record_id}.json")
        blob_data = blob_client.download_blob()
        return json.loads(blob_data.readall())