# Purpose of this file
# Connect to GCS
# Test the connection to GCS
# List buckets in GCS
# List objects in a bucket


from google.cloud import storage
import os

client = storage.Client()


class GCSClient:

    def __init__(self):
        '''
        Initialize the GCS client using service account credentials.
        Docker automatically sets the GOOGLE_APPLICATION_CREDENTIALS environment variable to point to the service account key file.
        '''
        self.client = storage.Client()

    def list_buckets(self):
        '''
        List all buckets in the GCS project.
        '''
        buckets = self.client.list_buckets()
        return [bucket.name for bucket in buckets]

    def list_files(self, bucket_name, prefix=None):
        '''
        List all objects in a specific bucket.
        '''
        bucket = self.client.get_bucket(bucket_name)
        objects = bucket.list_blobs(prefix=prefix)

        return [obj.name for obj in objects]
    
    def test_connection(self):
        '''
        Test the connection to GCS by listing buckets.
        '''
        try:
            buckets = self.list_buckets()
            print(f"Successfully connected to GCS. Buckets: {buckets}")
            return True
        except Exception as e:
            print(f"Failed to connect to GCS: {e}")
            return False