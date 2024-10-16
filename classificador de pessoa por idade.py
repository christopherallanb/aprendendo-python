while True:
    age = int(input('qual sua idade?'))
    if age < 0:
        print('a idade não pode ser negativa.')
    if age > 0 and age <= 12:
        print('você é uma criança')
    elif age > 12 and age <= 17:
        print('você é um adolescente')
    elif age > 17 and age <= 64:
        print('você é adulto')
    elif age > 65:
        print('você é idoso')

    main = input('gostaria de verificar outra idade? (s/n): ')
    if main.lower() == 'n':
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
                                                  