# Engenharia de Dados — Projeto ENEM 2013 vs 2023

Este repositório contém a parte de **engenharia de dados** de um projeto que compara os dados do Exame Nacional do Ensino Médio (ENEM) entre os anos de **2013 e 2023**. O objetivo é construir uma **pipeline de dados** estruturada em camadas — **bronze**, **silver** e **gold** — para tratar, integrar e analisar os dados, gerando assim um conjunto de **indicadores visuais** em um painel interativo (dashboard).

---

## 🔍 Sobre o Projeto

A pipeline foi projetada para:

- Realizar a **extração, transformação e carga (ETL)** dos dados brutos do ENEM;
- Organizar os dados em camadas:
  - **Bronze**: dados brutos e desorganizados;
  - **Silver**: dados limpos, com tipos ajustados e colunas relevantes;
  - **Gold**: dados prontos para análise e geração de visualizações;
- Armazenar essas camadas em **buckets no Google Cloud Storage (GCS)**;
- Fazer uma análise exploratória e comparativa entre os anos de 2013 e 2023.

Foram analisadas informações como:

- Perfil dos participantes;
- Local de realização da prova;
- Escolas participantes;
- Desempenho nas provas objetivas e na redação;
- Questionário socioeconômico.

---

## ☁️ Infraestrutura em Nuvem

As camadas de dados (**bronze**, **silver**, **gold**) foram armazenadas em **buckets do Google Cloud Storage**, facilitando o controle, escalabilidade e integração com ferramentas de análise e visualização.

---

## 📊 Visualizações

As visualizações dos indicadores foram desenvolvidas com o **Looker Studio** (antigo Data Studio), permitindo uma análise interativa e intuitiva dos dados.

📎 Acesse o dashboard aqui: [🔗 Link para o painel no Looker Studio](https://seu-link-aqui.com)

---

## 📝 Artigo no Medium

Publiquei também um artigo explicando o projeto, abordando tanto a parte técnica quanto os principais insights obtidos.

📎 Leia o artigo: [🔗 Projeto ENEM 2013 vs 2023 — Medium](https://medium.com/seu-artigo-aqui)

---

## Tecnologias Utilizadas

Python

Pandas / NumPy

Jupyter Notebooks

Google Cloud Storage (GCS)

Google Looker Studio

Git / GitHub

## Objetivo Geral

Demonstrar, através de uma pipeline de dados bem estruturada, como é possível transformar grandes volumes de dados públicos em informações valiosas para análise e tomada de decisão, com foco na educação.
