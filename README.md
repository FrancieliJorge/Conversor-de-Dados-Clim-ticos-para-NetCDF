# Conversor-de-Dados-Clim-ticos-para-NetCDF
Este repositório contém um script Python que automatiza a conversão de arquivos .ctl para o formato NetCDF (.nc) e combina arquivos para cada membro de um conjunto de previsões climáticas.

# Conversor de Dados Climáticos 

Este repositório contém um script Python que automatiza a conversão de arquivos `.ctl` para o formato NetCDF (`.nc`) e os combina para cada membro de um conjunto de previsões. O script é projetado para trabalhar com dados climáticos, nesse caso para datas de 1 de novembro de 1999 a 16 de março de 2011, processando arquivos para o dia 1 e 16 de cada mês.

## Requisitos

- Python 3.x
- Pandas
- Climate Data Operators (CDO)

## Instalação

1. Instale o Python 3.x a partir do [Python.org](https://www.python.org/).
2. Instale os pacotes Python necessários usando o pip:
    ```bash
    pip install pandas
    ```
3. Instale o Climate Data Operators (CDO) a partir da [Documentação do CDO](https://code.mpimet.mpg.de/projects/cdo).

## Uso

1. Clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/seu-repo-nome.git
    cd seu-repo-nome
    ```

2. Coloque seus arquivos `.ctl` nos diretórios apropriados que correspondem ao padrão de data `YYYYMMDDHH`.

3. Execute o script:
    ```bash
    python converter.py
    ```

O script converterá todos os arquivos `.ctl` para arquivos `.nc` e, em seguida, os combinará em arquivos NetCDF únicos para cada membro do conjunto.

## Explicação

O script realiza os seguintes passos:
1. **Criação de Intervalo de Datas**: Cria uma lista de datas de 1 de novembro de 1999 a 16 de março de 2011, incluindo apenas os dias 1 e 16 de cada mês.
2. **Conversão de `.ctl` para `.nc`**: Para cada data, encontra todos os arquivos `.ctl` e os converte para `.nc` usando o CDO.
3. **Combinação de Arquivos**: Para cada data e cada membro (1-12), combina os arquivos `.nc` individuais em um único arquivo.

## Contribuindo

Se você deseja contribuir para este projeto, por favor faça um fork do repositório e crie um pull request com suas alterações.

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
