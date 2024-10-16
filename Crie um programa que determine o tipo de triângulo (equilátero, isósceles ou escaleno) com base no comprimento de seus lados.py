def tipo_triangulo(lado1, lado2, lado3):
    # Verificar se é válido
    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        return "triângulo invalido ."

    # determina o tipo de triângulo
    if lado1 == lado2 == lado3:
        return "Triângulo Equilátero (todos os lados iguais)"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:

        return "Triângulo Isósceles (dois lados iguais)"
    else:
        return "Triângulo Escaleno (todos os lados diferentes)"
        #mais uma vez
def main():
    try:
        lado1 = float(input('Informe o comprimento do primeiro lado: '))

        lado2 = float(input('Informe o comprimento do segundo lado: '))

        lado3 = float(input('Informe o comprimento do terceiro lado: '))


        resultado = tipo_triangulo(lado1, lado2, lado3)
        print(resultado)

    except ValueError:
        print('coloque valores numéricos válidos.')

    #extremamente necessario

while True:
    main()
    continuar = input('verificar outro triângulo? (s/n): ')
    if continuar.lower() == 'n':
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
                                                  