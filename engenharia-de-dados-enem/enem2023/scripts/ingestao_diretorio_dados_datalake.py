import os
from google.cloud import storage

def upload_pasta_para_bucket(
    caminho_pasta_local: str,
    bucket_name: str,
    pasta_destino_bucket: str,
    chave_json: str
):
    client = storage.Client.from_service_account_json(chave_json)
    bucket = client.bucket(bucket_name)

    for nome_arquivo in os.listdir(caminho_pasta_local):
        caminho_completo_arquivo = os.path.join(caminho_pasta_local, nome_arquivo)
        
        if os.path.isfile(caminho_completo_arquivo):
            blob_nome = os.path.join(pasta_destino_bucket, nome_arquivo).replace("\\", "/")
            
            blob = bucket.blob(blob_nome)
            blob.upload_from_filename(caminho_completo_arquivo)
            
            print(f"Arquivo {nome_arquivo} enviado para gs://{bucket_name}/{blob_nome}")

if __name__ == "__main__":
    pasta_local = 'parquet_chunks'
    bucket = 'bucket-enem'
    pasta_destino = 'bronze/parquet'
    caminho_chave = r'C:\Users\gustavo\Desktop\projeto\EngenhariaDadosEnem\chave\chave.json'

    upload_pasta_para_bucket(pasta_local, bucket, pasta_destino, caminho_chave)