import re
import joblib

modelo = joblib.load("modelo_classificacao.pkl")
def classificar_mensagem_ml(mensagem):
    """Classifica a mensagem usando o modelo de ML e ajusta a prioridade."""

    # Expressão regular para dividir frases por ".", "?", "!", ";" e ","
    partes = re.split(r"[.!?;,]", mensagem)

    # Classifica cada parte separadamente
    categorias_detectadas = [modelo.predict([p.strip()])[0] for p in partes if p.strip()]

    # Dicionário de prioridade
    prioridades = {
        "Trabalho": 1,
        "Sugestões Locais": 2,
        "Perguntas Gerais": 3,
        "Outros": 4
    }

    # Se "Trabalho" estiver presente, ele tem prioridade máxima
    if "Trabalho" in categorias_detectadas:
        return "Trabalho"

    # Senão, retorna a categoria com menor valor de prioridade
    return min(categorias_detectadas, key=lambda c: prioridades.get(c, 5))
