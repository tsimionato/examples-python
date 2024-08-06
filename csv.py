import pandas as pd
from typing import Tuple


def ler_arquivo_csv(caminho_arquivo: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(caminho_arquivo)
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        exit()
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo está vazio.")
        exit()
    except pd.errors.ParserError:
        print("Erro: Ocorreu um problema ao ler o arquivo.")
        exit()


def calcular_receita(df: pd.DataFrame) -> pd.DataFrame:
    df['Receita'] = df['Quantidade'] * df['Preço Unitário']
    return df


def total_vendas_por_produto(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('Produto').agg({'Quantidade': 'sum', 'Receita': 'sum'}).reset_index()


def receita_total_diaria(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('Data').agg({'Receita': 'sum'}).reset_index()


def produtos_top(df: pd.DataFrame) -> Tuple[pd.Series, pd.Series]:
    produto_mais_vendido = df.loc[df['Quantidade'].idxmax()]
    produto_maior_receita = df.loc[df['Receita'].idxmax()]
    return produto_mais_vendido, produto_maior_receita


def gerar_relatorio(
        total_vendas_produto: pd.DataFrame,
        receita_diaria: pd.DataFrame,
        produto_mais_vendido: pd.Series,
        produto_maior_receita: pd.Series,
        caminho_relatorio: str
) -> None:
    relatorio_vendas = total_vendas_produto
    relatorio_vendas.columns = ['Produto', 'Total Vendido', 'Receita Total']

    resumo = pd.DataFrame({
        'Produto': ['Total Diário', 'Produto mais vendido', 'Produto maior receita'],
        'Total Vendido': ['-', produto_mais_vendido['Quantidade'], '-'],
        'Receita Total': [receita_diaria['Receita'].sum(), produto_mais_vendido['Receita'],
                          produto_maior_receita['Receita']]
    })

    relatorio_final = pd.concat([relatorio_vendas, resumo], ignore_index=True)

    try:
        relatorio_final.to_csv(caminho_relatorio, index=False)
        print("Relatório de vendas gerado com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o relatório: {e}")


def main() -> None:
    caminho_arquivo_csv = '/.vendas.csv'
    caminho_relatorio_csv = 'relatorio_vendas.csv'

    df_vendas = ler_arquivo_csv(caminho_arquivo_csv)
    df_vendas = calcular_receita(df_vendas)
    total_vendas_produto = total_vendas_por_produto(df_vendas)
    receita_diaria = receita_total_diaria(df_vendas)
    produto_mais_vendido, produto_maior_receita = produtos_top(total_vendas_produto)
    gerar_relatorio(total_vendas_produto, receita_diaria, produto_mais_vendido, produto_maior_receita,
                    caminho_relatorio_csv)
