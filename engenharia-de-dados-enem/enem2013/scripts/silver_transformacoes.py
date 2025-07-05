import os
import pandas as pd
import gcsfs

def processar_dados_gcs(bucket_name, chave_json, formato_entrada, caminho_particionado,
                        limpar_colunas, pasta_saida_local, grupos, particionado=False):
    fs = gcsfs.GCSFileSystem(token=chave_json)

    if particionado:
        arquivos = fs.glob(f'{bucket_name}/{caminho_particionado}*.{formato_entrada}')
    else:
        arquivos = [f'{bucket_name}/{caminho_particionado}.{formato_entrada}']

    for caminho_completo in arquivos:
        print(f'Processando {caminho_completo}...')
        nome_base = os.path.splitext(os.path.basename(caminho_completo))[0]

        with fs.open(caminho_completo, 'rb') as f:
            df = pd.read_parquet(f)

        for col in limpar_colunas:
            if col in df.columns:
                df.drop(columns=[col], inplace=True)

        for grupo, colunas in grupos.items():
            colunas_existentes = [col for col in colunas if col in df.columns]
            if not colunas_existentes:
                continue

            df_subset = df[colunas_existentes]

            caminho_saida = f"{bucket_name}/{pasta_saida_local}/{grupo}/{nome_base}_{grupo}.parquet"
            print(f'Salvando arquivo {caminho_saida}...')

            with fs.open(caminho_saida, 'wb') as f_out:
                df_subset.to_parquet(f_out, index=False)

    print("Processamento finalizado.")

if __name__ == "__main__":
    bucket_name = 'enem2013'
    chave_json = r'C:\Users\gustavo\Desktop\projeto-bd2\engenharia-de-dados-enem\enem2013\chave\chave.json'

    formato_entrada = 'parquet'
    caminho_particionado = 'bronze/parquet/MICRODADOS_ENEM_2013_chunk_'

    remover_colunas = [
        'TP_ESTADO_CIVIL',
        'TP_ST_CONCLUSAO',
        'ANO_CONCLUIU',
        'TP_ENSINO',
        'IN_TREINEIRO',
        "CO_UF_ESC",
        "TP_SIT_FUNC_ESC",
        "IN_CERTIFICADO",
        "NO_ENTIDADE_CERTIFICACAO",
        "CO_UF_ENTIDADE_CERTIFICACAO",
        "SG_UF_ENTIDADE_CERTIFICACAO",
        "CO_UF_PROVA",
        "TP_PRESENCA_CN",
        "TP_PRESENCA_CH",
        "TP_PRESENCA_LC",
        "TP_PRESENCA_MT",
        "CO_PROVA_CN",
        "CO_PROVA_CH",
        "CO_PROVA_LC",
        "CO_PROVA_MT",
        "TX_RESPOSTAS_CN",
        "TX_RESPOSTAS_CH",
        "TX_RESPOSTAS_LC",
        "TX_RESPOSTAS_MT",
        "TX_GABARITO_CN",
        "TX_GABARITO_CH",
        "TX_GABARITO_LC",
        "TX_GABARITO_MT",
        "TP_STATUS_REDACAO",
        "Q001",
        "Q002",
        "Q004",
        "Q005",
        "Q006",
        "Q007",
        "Q008",
        "Q009",
        "Q011",
        "Q012",
        "Q013",
        "Q014",
        "Q015",
        "Q018",
        "Q019",
        "Q020",
        "Q021",
        "Q022",
        "Q023",
        "Q024",
        "Q025",
        "Q026",
        "Q027",
        "Q028",
        "Q029",
        "Q030",
        "Q031",
        "Q032",
        "Q033",
        "Q034",
        "Q035",
        "Q036",
        "Q037",
        "Q038",
        "Q039",
        "Q040",
        "Q041",
        "Q042",
        "Q043",
        "Q044",
        "Q045",
        "Q046",
        "Q047",
        "Q048",
        "Q049",
        "Q050",
        "Q051",
        "Q052",
        "Q053",
        "Q054",
        "Q055",
        "Q056",
        "Q057",
        "Q058",
        "Q059",
        "Q060",
        "Q061",
        "Q062",
        "Q063",
        "Q064",
        "Q065",
        "Q066",
        "Q067",
        "Q068",
        "Q069",
        "Q070",
        "Q071",
        "Q072",
        "Q073",
        "Q074",
        "Q075",
        "Q076"
    ]

    grupos_dados = {
        "participante": [
            "NU_INSCRICAO",
            "NU_ANO",
            "TP_FAIXA_ETARIA",
            "TP_SEXO",
            "TP_COR_RACA",
            "TP_NACIONALIDADE",
            "TP_ESCOLA"
        ],

        "escola": [
            "NU_INSCRICAO",
            "CO_MUNICIPIO_ESC",
            "NO_MUNICIPIO_ESC",
            "SG_UF_ESC",
            "TP_DEPENDENCIA_ADM_ESC",
            "TP_LOCALIZACAO_ESC"
        ],

        "local": [
            "NU_INSCRICAO",
            "CO_MUNICIPIO_PROVA",
            "NO_MUNICIPIO_PROVA",
            "SG_UF_PROVA"
        ],

        "prova": [
            "NU_INSCRICAO",
            "NU_NOTA_CN",
            "NU_NOTA_CH",
            "NU_NOTA_LC",
            "NU_NOTA_MT",
            "TP_LINGUA"
        ],

        "redacao": [
            "NU_INSCRICAO",
            "NU_NOTA_REDACAO"
        ],

        "questionario": [
            "NU_INSCRICAO",
            "Q003",
            "Q010",
            "Q016",
            "Q017"
        ],
    }

    processar_dados_gcs(
        bucket_name=bucket_name,
        chave_json=chave_json,
        formato_entrada=formato_entrada,
        caminho_particionado=caminho_particionado,
        limpar_colunas=remover_colunas,
        pasta_saida_local='silver/parquet',
        grupos=grupos_dados,
        particionado=True
    )