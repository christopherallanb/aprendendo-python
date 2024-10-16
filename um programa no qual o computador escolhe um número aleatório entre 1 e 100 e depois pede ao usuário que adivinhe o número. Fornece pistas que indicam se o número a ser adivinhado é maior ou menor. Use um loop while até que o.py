import random

akinator = random.randint(1, 100)

akinator2 = int(akinator)

jogador = int(input('tente adivinhar o número de 1 a 100: '))

if jogador == akinator2:
    print('acertou')
else:
    print('errou')
    while True:
        if jogador > akinator2:
            print('tente um número menor')
        elif jogador < akinator2:
            print('tente um número maior')
        jogador = int(input('tente adivinhar o número de 1 a 100: '))
        if jogador == akinator2:
            print('acertou')
            break

                    
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
                                                  