from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI(title="API da Van Escolar")

# Libera o cadeado da API para o aplicativo do celular conseguir conectar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # O asterisco permite que qualquer tela acesse a API
    allow_credentials=True,
    allow_methods=["*"], # Libera os métodos de ler (GET) e alterar (PUT/POST)
    allow_headers=["*"],
)

# Inicializa o "motor" da API
# Rota de teste para confirmar se o servidor está no ar
@app.get("/")
def raiz():
    return {"mensagem": "A API da Van Escolar está online e pronta para uso!"}

# Rota para cadastrar alunos (Substitui o Menu 1 do terminal)
@app.post("/cadastrar/{nome}")
def cadastrar_aluno(nome: str):
    # Conecta ao mesmo banco de dados que criamos antes
    conexao = sqlite3.connect('banco_van.db')
    cursor = conexao.cursor()
    
    # Salva o aluno
    cursor.execute("INSERT INTO alunos (nome, status) VALUES (?, ?)", (nome, "Na Escola"))
    conexao.commit()
    conexao.close()
    
    return {"sucesso": True, "mensagem": f"{nome} cadastrado com sucesso no banco de dados!"}

# Rota para o aplicativo consultar quem ainda falta embarcar (Substitui o print da lista)
@app.get("/alunos/pendentes")
def listar_pendentes():
    conexao = sqlite3.connect('banco_van.db')
    cursor = conexao.cursor()
    
    cursor.execute("SELECT nome FROM alunos WHERE status = 'Na Escola'")
    alunos = cursor.fetchall()
    conexao.close()
    
    # Transforma a resposta do banco em uma lista simples de nomes
    lista_nomes = [aluno[0] for aluno in alunos]
    
    return {
        "faltam_embarcar": len(lista_nomes), 
        "alunos": lista_nomes
    }

# Rota para atualizar o status quando o aluno entra na van (Substitui o input do terminal)
@app.put("/embarcar/{nome}")
def embarcar_aluno(nome: str):
    conexao = sqlite3.connect('banco_van.db')
    cursor = conexao.cursor()
    
    cursor.execute("UPDATE alunos SET status = 'Na Van' WHERE nome = ? COLLATE NOCASE AND status = 'Na Escola'", (nome,))
    linhas_alteradas = cursor.rowcount
    conexao.commit()
    conexao.close()
    
    if linhas_alteradas > 0:
        return {"sucesso": True, "mensagem": f"✔️ {nome} conferido e está na van!"}
    else:
        return {"sucesso": False, "mensagem": "❌ Aluno não encontrado na escola ou já embarcou."}