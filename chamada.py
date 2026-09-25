# Esboço da Lógica com Cadastro Dinâmico

# O banco de dados (lista) agora começa vazio
alunos_na_escola = []

def cadastrar_aluno():
    print("\n--- NOVO CADASTRO ---")
    nome_novo = input("Digite o nome do aluno: ")
    
    # O .append() adiciona o aluno digitado à nossa lista com o status inicial
    alunos_na_escola.append({"nome": nome_novo, "status": "Na Escola"})
    print(f"✅ {nome_novo} cadastrado com sucesso!")

def chamada_retorno():
    # Trava extra: não deixa iniciar a chamada se a lista estiver vazia
    if not alunos_na_escola:
        print("\n⚠️ Nenhum aluno cadastrado ainda. Vá no menu 1 primeiro!")
        return

    print("\n--- INICIANDO EMBARQUE NA ESCOLA ---")
    
    while True:
        # Verifica quem ainda tem o status "Na Escola"
        faltam_embarcar = [aluno for aluno in alunos_na_escola if aluno["status"] == "Na Escola"]
        
        # Se não falta ninguém, libera a van
        if not faltam_embarcar:
            print("\n✅ TODOS A BORDO! Nenhum aluno esquecido. A van está liberada para partir.")
            break
            
        print(f"\n⚠️ ATENÇÃO: Faltam {len(faltam_embarcar)} aluno(s) embarcar.")
        print("Ainda estão na escola:")
        for aluno in faltam_embarcar:
            print(f"- {aluno['nome']}")
            
        nome_digitado = input("\nDigite o nome de quem entrou na van (ou 'parar'): ")
        
        if nome_digitado.lower() == 'parar':
            print("\n❌ Embarque interrompido. NÃO PARTA, ainda faltam alunos!")
            break
            
        aluno_encontrado = False
        for aluno in alunos_na_escola:
            if aluno["nome"].lower() == nome_digitado.lower() and aluno["status"] == "Na Escola":
                aluno["status"] = "Na Van" # Atualiza o status em tempo real
                print(f"\n✔️ {aluno['nome']} conferido e está na van!")
                aluno_encontrado = True
                break
        
        if not aluno_encontrado:
            print("\n❌ Nome incorreto ou aluno já está na van. Verifique novamente.")

def menu_principal():
    # O laço (while True) mantém o programa rodando até você escolher a opção 3
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
            print("\nSaindo do sistema!")
            break
        else:
            print("\n❌ Opção inválida. Tente novamente.")

# Essa linha é o "motor de arranque" que faz o menu aparecer quando você roda o script
menu_principal()