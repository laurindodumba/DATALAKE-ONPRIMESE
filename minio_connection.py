import boto3
from boto3.session import Config

def get_minio_client():
    client = boto3.client(
        's3',
        endpoint_url='http://127.0.0.1:9000',
        aws_access_key_id='vx3hZvJvpN3NjPDEAkTn',
        aws_secret_access_key='ACSYVO8qxTWwf4vk4uavggLDym1jw8oy02m0Zyhk',
        config=Config(signature_version='s3v4'),
        verify=False,
        region_name='sa-east-1'
    )
    return client

# Teste a conexão
if __name__ == "__main__":
    client = get_minio_client()
    try:
        response = client.list_buckets()
        print("Buckets disponíveis:")
        for bucket in response['Buckets']:
            print(f"- {bucket['Name']}")
    except Exception as e:
        print(f"Erro ao conectar ao MinIO: {e}")
