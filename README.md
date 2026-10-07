# Atividades autocorrigíveis SENAI

Professor Rodrigo Moreira. Aula 01 de Programação de Aplicativos.

Duas páginas independentes, com duração sugerida de 27 minutos cada:

- Python: `index.html`, execução de Python, seis desafios e duas questões conceituais.
- Matriz de Eisenhower: `eisenhower/index.html`, estudo de caso e múltipla escolha.

## Sites disponíveis para a aula

- Python: https://senai-python-rodrigo.nathsant.chatgpt.site
- Eisenhower: https://senai-eisenhower-rodrigo.nathsant.chatgpt.site

## Publicação no GitHub Pages

Em Settings > Pages, selecione Deploy from a branch, branch main, pasta /(root) e Save.

Após a ativação e implantação, os endereços previstos são:

- https://rodheisenberg.github.io/senai-python-rodrigo/
- https://rodheisenberg.github.io/senai-python-rodrigo/eisenhower/

## Executar localmente

Execute `python -m http.server 8000` nesta pasta. Abra http://localhost:8000 para Python ou http://localhost:8000/eisenhower/ para a matriz. Os sites precisam de HTTP para carregar os arquivos JSON.

## Progresso e resultados

Nome opcional, progresso salvo no navegador em localStorage, revisão das respostas e resultado baixado em texto ou impresso em PDF. Não há envio automático ao professor nem coleta centralizada.

## Python

O código executa em Web Worker com Pyodide 0.29.2, baixado do CDN jsDelivr. A primeira carga exige internet. checks.py verifica os seis desafios. Cada execução tem limite de 8 segundos.

HTML, CSS e JavaScript, sem compilação.
