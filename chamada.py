import sqlite3

# 1. CONEXÃO COM O BANCO DE DADOS
conexao = sqlite3.connect('banco_van.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        status TEXT NOT NULL
    )
''')
conexao.commit()

# 2. FUNÇÃO DE CADASTRO
def cadastrar_aluno():
    print("\n--- NOVO CADASTRO ---")
    nome_novo = input("Digite o nome do aluno: ")
    
    cursor.execute("INSERT INTO alunos (nome, status) VALUES (?, ?)", (nome_novo, "Na Escola"))
    conexao.commit()
    
    print(f"✅ {nome_novo} cadastrado com sucesso e salvo no banco de dados!")

# 3. FUNÇÃO DE CHAMADA
def chamada_retorno():
    cursor.execute("SELECT * FROM alunos")
    se_vazio = cursor.fetchall()
    
    if not se_vazio:
        print("\n⚠️ Nenhum aluno cadastrado ainda. Vá no menu 1 primeiro!")
        return

    print("\n--- INICIANDO EMBARQUE NA ESCOLA ---")
    
    while True:
        cursor.execute("SELECT nome FROM alunos WHERE status = 'Na Escola'")
        faltam_embarcar = cursor.fetchall()
        
        if not faltam_embarcar:
            print("\n✅ TODOS A BORDO! Nenhum aluno esquecido. A van está liberada para partir.")
            break
            
        print(f"\n⚠️ ATENÇÃO: Faltam {len(faltam_embarcar)} aluno(s) embarcar.")
        print("Ainda estão na escola:")
        for aluno in faltam_embarcar:
            print(f"- {aluno[0]}")
            
        nome_digitado = input("\nDigite o nome de quem entrou na van (ou 'parar'): ")
        
        if nome_digitado.lower() == 'parar':
            print("\n❌ Embarque interrompido. NÃO PARTA, ainda faltam alunos!")
            break
            
        cursor.execute("UPDATE alunos SET status = 'Na Van' WHERE nome = ? COLLATE NOCASE AND status = 'Na Escola'", (nome_digitado,))
        conexao.commit()
        
        if cursor.rowcount > 0:
            print(f"\n✔️ {nome_digitado} conferido e está na van!")
        else:
            print("\n❌ Nome incorreto ou aluno já está na van. Verifique novamente.")

# 4. MENU PRINCIPAL
def menu_principal():
    while True:
        print("\n" + "="*30)
        print("🚐 SISTEMA DA VAN ESCOLAR")
        print("="*30)
        print("1. Cadastrar Novo Aluno")
        print("2. Fazer Chamada (Retorno da Escola)")
        print("3. Sair do Sistema")
        
        opcao = input("\nEscolha uma opção (1, 2 ou 3): ")
        
        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            chamada_retorno()
        elif opcao == '3':
            print("\nSaindo do sistema. Até amanhã!")
            break
        else:
            print("\n❌ Opção inválida. Tente novamente.")

# INICIA O SISTEMA
menu_principal()