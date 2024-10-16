from datetime import datetime
def calcular_idade(data_nascimento):
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year
    return idade
data_nascimento_input = input("Por favor, insira sua data de nascimento (dia-mês-ano): ")
try:
    data_nascimento = datetime.strptime(data_nascimento_input, "%d-%m-%Y")
    idade = calcular_idade(data_nascimento)
    print(f"Você tem {idade} anos.")
except ValueError:
    print("Formato de data inválido. Por favor, use dia-mês-ano.")

#forma muito mais simplificada =
# atual = int(2024)
# nasc = int(input("Qual o ano em que você nasceu? "))
#idade = atual - nasc
#print("Sua idade é: ", idade , " anos.")


                    
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
                                                  