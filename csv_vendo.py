import pandas as pd
from typing import Tuple


# Função para localizar e ler o arquivo CSV
def ler_arquivo_csv(caminho_arquivo: str) -> pd.DataFrame:
    try:
        # Tenta ler o arquivo CSV usando pandas
        df = pd.read_csv(caminho_arquivo)
        print("Colunas do DataFrame:", df.columns)  # Exibe as colunas do DataFrame lido
        return df  # Retorna o DataFrame lido
    except FileNotFoundError:
        # Trata o erro caso o arquivo não seja encontrado
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        exit()  # Encerra o programa
    except pd.errors.EmptyDataError:
        # Trata o erro caso o arquivo esteja vazio
        print("Erro: O arquivo está vazio.")
        exit()  # Encerra o programa
    except pd.errors.ParserError:
        # Trata o erro caso haja um problema ao ler o arquivo
        print("Erro: Ocorreu um problema ao ler o arquivo.")
        exit()  # Encerra o programa


# Função para calcular a receita com base na quantidade e no preço unitário
def calcular_receita(df: pd.DataFrame) -> pd.DataFrame:
    # Adiciona uma nova coluna 'Receita' calculando o produto de 'Quantidade' e 'Preço Unitário'
    df['Receita'] = df['Quantidade'] * df['Preço Unitário']
    return df  # Retorna o DataFrame atualizado


# Função para calcular o total de vendas por produto
def total_vendas_por_produto(df: pd.DataFrame) -> pd.DataFrame:
    # Agrupa os dados por 'Produto' e calcula a soma de 'Quantidade' e 'Receita'
    return df.groupby('Produto').agg({'Quantidade': 'sum', 'Receita': 'sum'}).reset_index()


# Função para calcular a receita total diária
def receita_total_diaria(df: pd.DataFrame) -> pd.DataFrame:
    # Agrupa os dados por 'Data' e calcula a soma de 'Receita'
    return df.groupby('Data').agg({'Receita': 'sum'}).reset_index()


# Função para encontrar o produto mais vendido e o produto que gerou mais receita
def produtos_top(df: pd.DataFrame) -> Tuple[pd.Series, pd.Series]:
    # Encontra o produto mais vendido com base na maior quantidade
    produto_mais_vendido = df.loc[df['Quantidade'].idxmax()]
    # Encontra o produto que gerou mais receita
    produto_maior_receita = df.loc[df['Receita'].idxmax()]
    return produto_mais_vendido, produto_maior_receita  # Retorna os dois produtos encontrados


# Função para gerar e salvar o relatório em um arquivo CSV
def gerar_relatorio(
        total_vendas_produto: pd.DataFrame,
        receita_diaria: pd.DataFrame,
        produto_mais_vendido: pd.Series,
        produto_maior_receita: pd.Series,
        caminho_relatorio: str
) -> None:
    # Renomeia as colunas do DataFrame para corresponder ao formato do relatório
    relatorio_vendas = total_vendas_produto
    relatorio_vendas.columns = ['Produto', 'Total Vendido', 'Receita Total']

    # Cria um resumo com a receita total diária e os produtos top
    resumo = pd.DataFrame({
        'Produto': ['Total Diário', 'Produto mais vendido', 'Produto maior receita'],
        'Total Vendido': ['-', produto_mais_vendido['Quantidade'], '-'],
        'Receita Total': [receita_diaria['Receita'].sum(), produto_mais_vendido['Receita'],
                          produto_maior_receita['Receita']]
    })

    # Concatena o relatório de vendas e o resumo
    relatorio_final = pd.concat([relatorio_vendas, resumo], ignore_index=True)

    try:
        # Tenta salvar o relatório final em um arquivo CSV
        relatorio_final.to_csv(caminho_relatorio, index=False)
        print("Relatório de vendas gerado com sucesso!")
    except Exception as e:
        # Trata o erro caso ocorra um problema ao salvar o relatório
        print(f"Erro ao salvar o relatório: {e}")


# Função principal que coordena a execução do script
def main() -> None:
    caminho_arquivo_csv = './vendas.csv'  # Caminho para o arquivo CSV de vendas
    caminho_relatorio_csv = './relatorio_vendas.csv'  # Caminho para salvar o relatório

    df_vendas = ler_arquivo_csv(caminho_arquivo_csv)  # Lê o arquivo CSV
    print("Primeiras linhas do DataFrame:", df_vendas.head())  # Exibe as primeiras linhas do DataFrame
    df_vendas = calcular_receita(df_vendas)  # Calcula a receita
    total_vendas_produto = total_vendas_por_produto(df_vendas)  # Calcula o total de vendas por produto
    receita_diaria = receita_total_diaria(df_vendas)  # Calcula a receita total diária
    produto_mais_vendido, produto_maior_receita = produtos_top(total_vendas_produto)  # Encontra os produtos top
    gerar_relatorio(total_vendas_produto, receita_diaria, produto_mais_vendido, produto_maior_receita,
                    caminho_relatorio_csv)  # Gera e salva o relatório


if __name__ == "__main__":
    main()  # Executa a função principal quando o script é executado