import pandas as pd
from io import StringIO
from minio_connection import get_minio_client

def save_to_minio(df, bucket, key):
    client = get_minio_client()
    csv_buffer = StringIO()
    df.toPandas().to_csv(csv_buffer, index=False)
    client.put_object(Bucket=bucket, Key=key, Body=csv_buffer.getvalue())

if __name__ == "__main__":
    from data_transformation import transform_data

    # Caminho do arquivo local
    file_path = "customer_feedback.csv"
    bucket_name = "devlake"

    # Carregar e transformar os dados
    df_transformed = transform_data(file_path)

    # Salvar nas camadas
    save_to_minio(df_transformed, bucket_name, "raw/customer_feedback.csv")
    save_to_minio(df_transformed, bucket_name, "silver/customer_feedback.csv")
    save_to_minio(df_transformed, bucket_name, "gold/customer_feedback.csv")
