from data_transformation import transform_data
from data_load import save_to_minio
from minio_connection import get_minio_client

def main():
    # Caminho do arquivo local
    file_path = "customer_feedback.csv"
    bucket_name = "devlake"

    # Conexão ao MinIO (teste opcional)
    client = get_minio_client()
    try:
        response = client.list_buckets()
        print("Conexão bem-sucedida ao MinIO. Buckets disponíveis:")
        for bucket in response['Buckets']:
            print(f"- {bucket['Name']}")
    except Exception as e:
        print(f"Erro ao conectar ao MinIO: {e}")
        return

    # Transformação de dados
    print("Iniciando transformação de dados...")
    df_transformed = transform_data(file_path)
    print("Transformação concluída.")

    # Carregamento dos dados nas camadas (raw, silver, gold)
    print("Carregando dados no MinIO...")
    save_to_minio(df_transformed, bucket_name, "raw/customer_feedback.csv")
    save_to_minio(df_transformed, bucket_name, "silver/customer_feedback.csv")
    save_to_minio(df_transformed, bucket_name, "gold/customer_feedback.csv")
    print("Dados carregados com sucesso.")

if __name__ == "__main__":
    main()
