vogais = ['a', 'e', 'i', 'o', 'u']
palavra = input("Digite uma palavra: ")

for letra in palavra:
    if letra in vogais:
        print(letra)

vogal_numerica = 0
for letra in palavra:
    if letra in vogais:
        vogal_numerica += 1

print("A palavra", palavra, "tem", vogal_numerica, "vogais.")


                    
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
                                                  