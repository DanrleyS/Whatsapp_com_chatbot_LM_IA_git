📩 WhatsApp AI - Processamento Inteligente de Mensagens
API desenvolvida para classificar e responder mensagens no WhatsApp com inteligência artificial. A API utiliza Machine Learning para classificar mensagens em categorias e fornece respostas contextuais utilizando OpenAI GPT.

🚀 Funcionalidades
📌 Classificação Inteligente de Mensagens
A API classifica mensagens em:
trabalho: relacionadas a atividades profissionais.
sugestoes_locais: pedidos de recomendações de locais.
perguntas_gerais: perguntas gerais que podem ser respondidas pela IA.
outros: mensagens sem classificação específica.
💬 Geração de Respostas com OpenAI GPT
Responde automaticamente perguntas gerais.
📍 Integração com Google Maps
Sugere locais com base no contexto da mensagem.
🛠️ Tecnologias Utilizadas
FastAPI - Framework para criação da API REST.
scikit-learn - Treinamento do modelo de Machine Learning para classificação.
OpenAI GPT - Responde a perguntas gerais.
Google Maps API - Busca locais recomendados.
pandas & joblib - Manipulação de dados e persistência do modelo.

📥 Instalação e Configuração
1️⃣ Clone o repositório:
bash:
git clone https://github.com/seu-usuario/whatsapp_AI.git
cd whatsapp_AI

2️⃣ Crie um ambiente virtual e ative:
bash:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

3️⃣ Instale as dependências:
bash:
pip install -r requirements.txt

4️⃣ Crie um arquivo .env e configure suas chaves:
ini
OPENAI_API_KEY= "sua-chave-da-openai"
GOOGLE_MAPS_API_KEY= "sua-chave-do-google-maps"

5️⃣ Treine o modelo de Machine Learning:
bash:
python models/train_model.py

6️⃣ Execute a API:
bash:
uvicorn main:app --reload
A API estará disponível em http://127.0.0.1:8000.

📡 Endpoints da API
🔹 1. Classificação e Resposta de Mensagens
POST /classificar_mensagem

📌 Descrição: Classifica a mensagem e retorna a categoria com uma resposta adequada.

📥 Exemplo de Requisição:
json:

{
  "mensagem": "Onde fica um bom restaurante para almoçar? Preciso também revisar um relatório urgente para o cliente."
}

📤 Exemplo de Resposta:
json:
{
  "categoria": "trabalho",
  "resposta": "Mensagem classificada como trabalho. Nenhuma consulta externa necessária."
}

🔹 2. Treinar o Modelo de Machine Learning
POST /train_model

📌 Descrição: Treina o modelo com novos dados para melhorar a classificação de mensagens.

📥 Exemplo de Requisição:

json:
{
  "dados": [
    {"mensagem": "Tem reunião hoje?", "categoria": "trabalho"},
    {"mensagem": "Sabe onde tem uma farmácia?", "categoria": "sugestoes_locais"},
    {"mensagem": "O que é inteligência artificial?", "categoria": "perguntas_gerais"}
  ]
}

📤 Exemplo de Resposta:
json
{
  "status": "Modelo treinado com sucesso!"
}
🔹 3. Buscar Locais no Google Maps
POST /buscar_locais

📌 Descrição: Retorna sugestões de locais com base na mensagem do usuário.

📥 Exemplo de Requisição:

json>
{
  "mensagem": "Onde encontro um bom restaurante por aqui?"
}
📤 Exemplo de Resposta:

json:
{
  "categoria": "sugestoes_locais",
  "resposta": ["Restaurante A - 4.5⭐", "Restaurante B - 4.2⭐"]
}
🏗️ Estrutura do Projeto

whatsapp_AI/
│── models/         # Modelos de Machine Learning
│── services/       # Serviços de processamento de mensagens
│── utils/          # Funções auxiliares
│── main.py         # Arquivo principal da API
│── requirements.txt # Dependências do projeto
│── .env            # Configurações de API Keys
📝 Notas Finais
O modelo de Machine Learning é treinado com um conjunto de mensagens previamente classificadas.
A API pode ser expandida para suportar novas funcionalidades, como integração com outros serviços.
Feedbacks e melhorias são bem-vindos! 🚀
