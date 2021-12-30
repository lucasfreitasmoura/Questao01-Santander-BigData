class Selecao:
    def __init__(self):
        self.gato = 'Miau'
        self.cachorro = 'Auau'
        self.historico = []


def menu():
    selecao = Selecao()
    menu = 0
    
    while menu != '1000':
        try:
            print("\n\n  [---- MENU ----] \n  Escolha uma Opção: \n \n    1 - GATO \n    2 - CACHORRO \n    3 - SAIR\n\n  [--------------]\n\n OBS: Digite: 'Histórico' - para ver o histórico de comandos!")
            menu = (input("\n Digite a opção desejada : "))
            
                            

            if menu == '1':
                print(selecao.gato)
                gato01 = selecao.gato
                i = 1
                
                iteracaogato = str(i) + ' ' + gato01
                
                selecao.historico.append(iteracaogato)
              
            elif menu =='2':
                print(selecao.cachorro)
                cachorro01 =selecao.cachorro
                i = 2
                iteracaocachorro = str(i) + ' ' + cachorro01
                selecao.historico.append(iteracaocachorro)
            elif menu =='Histórico' :
                print("\n".join(selecao.historico))
                break
                
            elif menu == '3':
                print("Volte sempre!....")
                break;
            elif menu != ('1' and '2' and '3' and 'Histórico'):
                print("\n\n [ATENÇÃO] ....Não temos essa opção em nosso menu no momento tente novamente uma opção válida como: \n 1\n 2\n Histórico\n OU\n 3 Se desejar parar o programa!\n\n")

            #elif menu > '4':
               # print("As opções disponíveis nesse momento são de 1 a 4 tente novamente.")
            #menu = (int(menu))
        except ValueError as erro:
            print("Nenhuma opção válida foi escolhida! tente novamente.")
    
        
    


def main():

   menu()

if __name__ == "__main__":
    main()



    
