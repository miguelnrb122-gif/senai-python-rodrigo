# Laboratório de Python

Atividade autocorrigível da Aula 01 da UC Programação de Aplicativos, Técnico em Desenvolvimento de Sistemas.

Professor Rodrigo Moreira, SENAI.

## Acesso

Versão publicada: https://senai-python-rodrigo.nathsant.chatgpt.site

Tempo sugerido: 27 minutos. As respostas podem ser revisadas e o resultado pode ser baixado em texto ou salvo em PDF. Não há envio automático ao professor.

## Publicar no GitHub Pages

1. Em Settings > Pages, selecione Deploy from a branch.
2. Selecione a branch main e a pasta / (root).
3. Salve e aguarde a publicação.

O projeto usa HTML, CSS e JavaScript e não exige compilação.

## Executar localmente

Na pasta do projeto, execute `python -m http.server 8000` e abra http://localhost:8000. Use um servidor HTTP, pois a página carrega arquivos com fetch().

## Progresso e resultados

O progresso é salvo no navegador usando localStorage. O nome é opcional. Não há banco de dados nem coleta centralizada das respostas. A autocorreção é destinada à prática em aula.

## Ambiente Python

Python executa em um Web Worker com Pyodide 0.29.2. A primeira carga precisa de internet para baixar o ambiente do CDN jsDelivr. O arquivo checks.py verifica os requisitos dos seis desafios. A execução tem limite de 8 segundos para evitar travamento por repetição sem fim.
