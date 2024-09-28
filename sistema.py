print("Olá! Seja bem vindo ao Sistema AcademiKus\n")
print("O que deseja fazer?\n")

alunos = ["Diogo", "Erick", "Amanda"]
estudantes = {
        "Diogo": {
            "Nome": "Diogo", 
            "Idade": 20, 
            "Telefone": 
            "81 9 9999-9999", 
            "Nota": {"Nota1": 0, "Nota2": 0, "Nota3": 0, "Nota4": 0}
            },

        "Erick": {
            "Nome": "Erick", 
            "Idade": 21, 
            "Telefone": "81 9 9888-8888", 
            "Nota": {"Nota1": 0, "Nota2": 0, "Nota3": 0, "Nota4": 0}
            }, 

        "Amanda": {
            "Nome": "Amanda", 
            "Idade": 22, 
            "Telefone": 
            "81 9 9777-7777", 
            "Nota": {"Nota1": 0, "Nota2": 0, "Nota3": 0, "Nota4": 0}
            },
    }

estudante = estudantes

while True:
    opcao = int(input("1 - Consultar alunos\n2 - Adicionar novo aluno\n3 - Impressão de relatório\n0 - Sair\n\nDigite a opção correspondente ao que deseja: "))

    """alunos = ["Dhiego", "Erick", 0, 0]
    estudantes = {
        "Dhiego": {"Nome": "Dhiego", "Idade": 22, "Telefone": "81 9 9999-9999", "Nota": 0},
        "Erick": {"Nome": "Erick", "Idade": 21, "Telefone": "81 9 9888-8888", "Nota": 0}
    }
    estudante = estudantes"""


    
    if opcao == 1:
        print("Consultar alunos") # CONSULTAR ALUNOS
        nome = alunos
        print(nome)
        
        while True:
            aluno = input("Informe o nome do aluno: ") 
            if aluno in nome:
                print(aluno)
                
                print("\n1 - Adicionar frequência\n2 - Remover aluno\n3 - Editar informação do aluno\n\n")
                acao = 0
                acao = int(input("Qual ação realizar: "))
                
                if acao == 1: # ADICIONAR FREQUÊNCIA
                    print("Adicionar frequência")
                    
                    while True:
                        disciplina = 80
                        hora_aula = 1
                        
                        aulas = int(input("Informe a quantidade de aula(s) assistida(s): "))
                        percentual = (aulas / disciplina) * 100
                        if aulas != 0:
                            print(f"{aluno} possui {aulas} aulas assistida(s)")
                            break
                                
                    print(f"A quantidade de frequências obtidas corresponde a {aulas} aulas ou {aulas * hora_aula} horas/aulas ou ainda {percentual:.2f}% do total da disciplina.")
                
                elif acao == 2: # REMOVER ALUNO
                    print("Remover aluno")
                    while True:
                        aluno = input("Informe o aluno a ser removido: ")
                        if aluno in nome:
                            nome.remove(aluno)
                            print(f"Aluno {aluno} removido com sucesso!")
                            break
                        else:
                            print("Este nome não consta como matriculado. Tente outra vez.")

                else: # EDITAR INFORMAÇÃO DO ALUNO
                    print("Editar informação do aluno")
                    while True:
                        estudante = input("Informe o aluno a editar (ou 0 para voltar ao menu principal): ")
                        if estudante == "0":  
                            print("Retornando ao menu principal")
                            break

                        if estudante in estudantes:
                            info = input("Informe qual informação a editar (Nome, Idade, Telefone, Nota): ")
                            if info in estudantes[estudante]:
                                nova_info = input(f"Informe o novo valor para {info}: ")
                                if info in ["idade", "nota"]:
                                    nova_info = int(nova_info) 
                                    
                                estudantes[estudante][info] = nova_info
                                print(f"{info.capitalize()} de {estudante} atualizado para {nova_info}.")
                            else:
                                print("Informação inválida. Tente outra vez.")
                        
                            
                        else:
                            print("Aluno não consta no sistema. Tente outra vez.")     
                break
            else:
                print("Esse nome não consta na lista. Tente outra vez.")

    
    elif opcao == 2:
        alunos = ["Diogo", "Erick", "Amanda"]
        while True:
            
            print("Adicionar novo aluno")
            novo_aluno = input("Informe o nome do aluno a adicionar (ou digite 0 zero 'sair'): ") 
            if novo_aluno.lower() == "0":
                break
            elif novo_aluno in alunos:
                print("Esse nome já consta na lista de alunos.")

            else:
                aluno = novo_aluno
                alunos.append(aluno)
                print(alunos)
                print(f"Novo aluno {aluno} adicionado com sucesso!")
        

    elif opcao == 3:
        print("Impressão de relatório")
        while True:
            relatorio = int(input("1 - Relatório\n0 - Sair\n\nDigite 1 para Relatório (ou 0 para Sair): "))
            if relatorio == 0:
                break
            elif relatorio == 1:
                print("Relatório de situação geral")
                estudantes_1 = estudantes

                def situacao_geral(estudante):

                    if estudante in estudantes:
                        nome_aluno = estudantes[estudante]["Nome"]
                        soma = 0

                        for nota in range(1, 5):
                            
                            nota_aluno = float(input(f"Informe a Nota{nota} para {estudante}: "))
                            estudantes[estudante]["Nota"][f"Nota{nota}"] = nota_aluno
                            soma += nota_aluno
                            print(f"Nome: {nome_aluno}; Nota: {nota_aluno}")

                        media = soma / 4
                        carga_horaria = int(input("Informe a carga horária da disciplina: "))
                        aulas = int(input("Informe quantas aulas o aluno assistiu: "))
                        percentual = (aulas / carga_horaria) * 100
                        
                        reprovado_por = []
                        if percentual < 75:
                            reprovado_por.append("faltas")
                        if media < 7:
                            reprovado_por.append("notas")

                        if reprovado_por:
                            resultado = "Reprovado por " + ", ".join(reprovado_por)
                        else:
                            resultado = "Aprovado"

                        return nome_aluno, media, carga_horaria, resultado
                    else:
                        print("Estudante não foi encontrado. Tente outra vez.")
                        return None, None, None
                    
                    
                resultados = []
                resultados.append(situacao_geral("Diogo"))
                print()
                resultados.append(situacao_geral("Erick"))
                print()
                resultados.append(situacao_geral("Amanda"))

                print("\nInformações dos alunos:\n")
                for nome_aluno, media, carga_horaria, resultado in resultados:
                     if nome_aluno: 
                        print(f"Aluno(a) {nome_aluno} - nota: {media:.2f}/frequência: {carga_horaria} aulas - ({resultado})")
                print()
                print()


                print("Relatório de situação específica")
                
                def gerar_relatorio(situacao):
                    print(f"\nRelatório: {situacao}")
                    for nome_aluno, media, carga_horaria, resultado in resultados:
                        if situacao == "Aprovado" and resultado == "Aprovado":
                            print(f"Aluno(a) {nome_aluno} - nota: {media:.2f}/frequência: {carga_horaria} aulas - {resultado}")
                        elif situacao == "Reprovado por Falta" and "faltas" in resultado:
                            print(f"Aluno(a) {nome_aluno} - nota: {media:.2f}/frequência: {carga_horaria} aulas - {resultado}")
                        elif situacao == "Reprovado por Nota" and "notas" in resultado:
                            print(f"Aluno(a) {nome_aluno} - nota: {media:.2f}/frequência: {carga_horaria} aulas - {resultado}")


                situacao_filtro = input("\nDigite a situação para filtrar (Aprovado, Reprovado por Falta, Reprovado por Nota): ")
                gerar_relatorio(situacao_filtro)
            
            else:
                print("Opção inválida. Tente outra vez")        
        break

    elif opcao == 0:
        print("Até mais!")
        break

    else:
        print("Essa opção não existe! Por favor, tente outra.\n")
        
        

    
    


