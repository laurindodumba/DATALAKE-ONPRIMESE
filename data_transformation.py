from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

def transform_data(file_path):
    # Inicia a sessão Spark
    spark = SparkSession.builder.appName("Data Transformation").getOrCreate()

    # Carregar dados raw
    df_raw = spark.read.csv(file_path, header=True, inferSchema=True)

    # Exemplo de transformação (adicionar coluna "processed_date")
    df_transformed = df_raw.withColumn("processed_date", lit("2024-12-29"))

    return df_transformed

if __name__ == "__main__":
    # Caminho do arquivo local
    file_path = "customer_feedback.csv"
    df_transformed = transform_data(file_path)
    df_transformed.show()
