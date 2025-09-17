from flask import Flask, render_template, request
from analise import analisar_planilha

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    tabela_html = None
    estatisticas_html = None
    colunas_numericas = None

    if request.method == "POST":
        arquivo = request.files["file"]

        if arquivo:
            tabela_html, estatisticas_html, colunas_numericas = analisar_planilha(arquivo)

    return render_template(
        "index.html",
        tabela=tabela_html,
        estatisticas=estatisticas_html,
        colunas=colunas_numericas
    )

if __name__ == "__main__":
    app.run(debug=True)
