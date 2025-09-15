import pandas as pd

arquivo = 'dados.xlsx'
tabela = pd.read_excel(arquivo)

print("📊 Estatísticas automáticas:\n")
print(tabela.describe(include="all"))

colunas_numericas = tabela.select_dtypes(include=["int64", "Float64"]).columns
print("\nColunas numéricas encontradas:", list(colunas_numericas))

estatisticas = tabela[colunas_numericas].agg(["sum", "mean", "min", "max"])
print("n\Resumo estatístico (soma, média, mínimo e máximo): ")
print(estatisticas)

with pd.ExcelWriter("relatorio_geral.xlsx") as writer:
    tabela.to_excel(writer, sheet_name="Original", index=False)
    estatisticas.to_excel(writer, sheet_name="Resumo")

print("\n✅ Relatório salvo em 'relatorio_geral.xlsx")
