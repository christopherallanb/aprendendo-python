
def verificar_aprovacao(nota1, nota2):
    if nota1 >= 60 and nota2 >= 60:
        return "Aprovado em ambas as disciplinas."
    elif nota1 < 60 and nota2 < 60:
        return "Reprovado em ambas as disciplinas."
    else:
        if nota1 < 60:
            return "Deve fazer prova de nivelamento na disciplina 1."
        if nota2 < 60:
            return "Deve fazer prova de nivelamento na disciplina 2."

def main():
    while True:
        try:
            # Entrada das notas
            nota1 = float(input('Digite a nota da primeira disciplina (0-100): '))
            nota2 = float(input('Digite a nota da segunda disciplina (0-100): '))


            if not (0 <= nota1 <= 100) or not (0 <= nota2 <= 100):
                print("As notas devem estar entre 0 e 100. Tente novamente.")
                continue  # Retorna ao início do loop

            # Verifica a situação do aluno
            resultado = verificar_aprovacao(nota1, nota2)
            print(resultado)
            break  # Sai do loop se ok

        except ValueError:
            print("insira um valor numérico válido para as notas.")

main()


                    
                                      ##          
                                      ############
                                    ##############
                                  ##############  
                            ##################    
                      ####################        
      ##            ####################          
                  ######################          
    ##            ######################          
    ##            ######################          
  ##            ##################      ##        
  ##          ##################        ##        
  ##          ################                    
  ##        ##################                    
  ####    ####################                    
    ################################              
                                                  