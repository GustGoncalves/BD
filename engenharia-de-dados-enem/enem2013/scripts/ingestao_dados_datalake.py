from google.cloud import storage

client = storage.Client.from_service_account_json(r'C:\Users\gustavo\Desktop\projeto\EngenhariaDadosEnem\chave\chave.json')

bucket_name = 'bucket-enem'
file_path = r'C:\Users\gustavo\Desktop\projeto\EngenhariaDadosEnem\dados\MICRODADOS_ENEM_2023_saida_amostra.csv'
destination_blob_name = 'bronze/microdados_enem_amostra.csv'

bucket = client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)

blob.upload_from_filename(file_path)

print(f"Arquivo enviado para gs://{bucket_name}/{destination_blob_name}")
