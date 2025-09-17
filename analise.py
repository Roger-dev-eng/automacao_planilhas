import pandas as pd

def analisar_planilha(arquivo):
    df = pd.read_excel(arquivo)

    tabela_html = df.head().to_html(classes="table table-striped", index=False)

    colunas_numericas = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    estatisticas = df[colunas_numericas].agg(["sum", "mean", "min", "max"])
    estatisticas_html = estatisticas.to_html(classes="table table-bordered")

    tabela_html = df.head().to_html(
    classes="table table-striped table-bordered text-center align-middle",
    index=False
    )

    return tabela_html, estatisticas_html, colunas_numericas
