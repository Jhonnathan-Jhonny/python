import sys

#  resp = 1,2,2,1,1


# FASE 1
def fase1(resposta, voltar):
  correta = "1"

  while resposta != "1" or resposta != "2":
    print("---------------------------------")
    print("-- Qual caminho deseja seguir? --")
    print("---------------------------------")
    resposta = input("1 - O tesouro escondido. \n2 - Sair da floresta.\nR: ")

    if resposta == "1":
      print()
      print("A primeira fase foi tranquila e Jack avançou sem problemas.")
      return resposta

    elif resposta == "2":
      print()
      print(
        "O caminho na verdade não saia da floresta, Jack caiu em um rio ácido e já sabemos o que aconteceu ..."
      )
      while resposta != correta and voltar != 0:
        print()
        print("Tem apenas ", voltar, " chance(s), tente novamente:")
        voltar -= 1
        print("---------------------------------")
        print("-- Qual caminho deseja seguir? --")
        print("---------------------------------")
        resposta = input(
          "1 - O tesouro escondido. \n2 - Sair da floresta.\nR: ")

        if resposta == "1":
          print()
          print("A primeira fase foi tranquila e Jack avançou sem problemas.")
          return resposta

        elif resposta == "2":
          print()
          print(
            "O caminho na verdade não saia da floresta, Jack caiu em um rio ácido e já sabemos o que aconteceu ..."
          )
        else:
          voltar += 1
          print("---------------------------------")
          print("-- Responda apenas com 1 ou 2. --")
          print("---------------------------------")

        if voltar == 0:
          print("Suas chances acabaram, Jack não conseguiu seu tesouro.")
          sys.exit()

    else:
      print("---------------------------------")
      print("-- Responda apenas com 1 ou 2. --")
      print("---------------------------------")


# FASE 2
def fase2(resposta, voltar):
  resposta = 0
  correta = "2"
  print(
    "Mas Jack começou a perceber que algo estava errado. Ele se sentiu seguido por algo nas sombras, mas não conseguiu identificar o que era."
  )
  print(
    "Jack se deparou com um lago enevoado. Ele podia ouvir gemidos vindos da água, mas não conseguia ver nada. Jack precisava decidir."
  )
  print()

  while resposta != "1" or resposta != "2":
    print("---------------------------------")
    print("-- Qual caminho deseja seguir? --")
    print("---------------------------------")
    resposta = input(
      "1 - Atravessar o lago. \n2 - Seguir por um caminho mais longo e seguro..\nR: "
    )

    if resposta == "1":
      print()
      print(
        "O lago estava cheio de criaturas arrepiantes, e logo capturaram Jack e se alimentaram e assim, Jack morreu."
      )
      while resposta != correta and voltar != 0:
        print()
        print("Tem apenas ", voltar, " chance(s), tente novamente:")
        voltar -= 1
        print("---------------------------------")
        print("-- Qual caminho deseja seguir? --")
        print("---------------------------------")
        resposta = input(
          "1 - Atravessar o lago. \n2 - Seguir por um caminho mais longo e seguro..\nR: "
        )

        if resposta == "2":
          print()
          print(
            "Jack escolheu o caminho seguro, ele evitou todos os perigos da floresta e continuou ileso, e em busca do seu tesouro."
          )
          return resposta

        elif resposta == "1":
          print()
          print(
            "O lago estava cheio de criaturas arrepiantes, e logo capturaram Jack e se alimentaram e assim, Jack morreu."
          )
        else:
          voltar += 1
          print("---------------------------------")
          print("-- Responda apenas com 1 ou 2. --")
          print("---------------------------------")

        if voltar == 0:
          print()
          print("Suas chances acabaram, Jack não conseguiu seu tesouro.")
          sys.exit()

    elif resposta == "2":
      print()
      print(
        "Jack escolheu o caminho seguro, ele evitou todos os perigos da floresta e continuou ileso, e em busca do seu tesouro."
      )
      return resposta

    else:
      print("---------------------------------")
      print("-- Responda apenas com 1 ou 2. --")
      print("---------------------------------")


# FASE 3
def fase3(resposta, voltar):
  correta = "2"
  resposta = 0
  print()
  print("Jack seguiu adiante, ainda cauteloso após sua experiência no lago enevoado. Ele logo chegou a uma clareira, onde viu duas opções de caminho.")
  while resposta != "1" or resposta != "2":
    print("---------------------------------")
    print("-- Qual caminho deseja seguir? --")
    print("---------------------------------")
    resposta = input("1 - Para esquerda \n2 - Para direita. \nR: ")
    if resposta == "1":
      print()
      print(
        "Jack decidiu seguir o caminho da esquerda, no entanto, caminho levou Jack a um abismo profundo, ele escorregou e caiu, gritando até desaparecer no escuro."
      )

      while resposta != correta and voltar != 0:
        print()
        print("Tem apenas ", voltar, " chance(s), tente novamente:")
        voltar -= 1
        print("---------------------------------")
        print("-- Qual caminho deseja seguir? --")
        print("---------------------------------")
        resposta = input("1 - Para esquerda \n2 - Para direita. \nR: ")

        if resposta == "2":
          print()
          print(
            "Jack decidiu seguir o caminho da direita, e foi um ótima escolha, no entando ..."
          )
          return resposta

        elif resposta == "1":
          print()
          print(
            "Jack decidiu seguir o caminho da esquerda, no entanto, caminho levou Jack a um abismo profundo, ele escorregou e caiu, gritando até desaparecer no escuro."
          )

        else:
          voltar += 1
          print("---------------------------------")
          print("-- Responda apenas com 1 ou 2. --")
          print("---------------------------------")

        if voltar == 0:
          print()
          print("Suas chances acabaram, Jack não conseguiu seu tesouro.")
          sys.exit()

    elif resposta == "2":
      print(
        " Jack decidiu seguir o caminho da direita, e foi um ótima escolha, no entando ..."
      )
      return resposta

    else:
      print("---------------------------------")
      print("-- Responda apenas com 1 ou 2. --")
      print("---------------------------------")


# FASE 4
def fase4(resposta, voltar):
  correta = "1"
  resposta = 0
  print()
  print(
    "Jack caminhou um pouco mais, mas logo viu que o caminho estava bloqueado por uma grande rocha. Ele precisava encontrar uma maneira de contorná-la."
  )

  while resposta != "1" or resposta != "2":
    print("---------------------------------")
    print("-- Qual caminho deseja seguir? --")
    print("---------------------------------")
    resposta = input(
      "1 - Procurar um caminho alternativo. \n2 - Empurrar a pedra. \nR: ")

    if resposta == "1":
      print()
      print(
        "Jack decidiu procurar uma passagem alternativa, mesmo que levasse mais tempo. Jack encontrou um caminho alternativo, que o levou através de um desfiladeiro estreito, mas seguro. Ele conseguiu contornar a rocha e continuar em sua busca pelo tesouro."
      )
      return resposta
    elif resposta == "2":
      print()
      print(
        "Jack decidiu tentar mover a rocha, para continuar seguindo o caminho original. Jack usou todas as suas forças para mover a rocha, mas ela era muito pesada. Ele se esforçou tanto que acabou desmaiando de exaustão. Quando acordou, Jack se encontrava em uma caverna escura, cheia de morcegos gigantes e aranhas venenosas."
      )

      while resposta != correta and voltar != 0:
        print()
        print("Tem apenas ", voltar, " chance(s), tente novamente:")
        voltar -= 1
        print("---------------------------------")
        print("-- Qual caminho deseja seguir? --")
        print("---------------------------------")
        resposta = input(
          "1 - Procurar um caminho alternativo. \n2 - Empurrar a pedra. \nR: ")

        if resposta == "1":
          print()
          print(
            "Jack decidiu procurar uma passagem alternativa, mesmo que levasse mais tempo. Jack encontrou um caminho alternativo, que o levou através de um desfiladeiro estreito, mas seguro. Ele conseguiu contornar a rocha e continuar em sua busca pelo tesouro."
          )
          return resposta

        elif resposta == "2":
          print()
          print(
            "Jack decidiu tentar mover a rocha, para continuar seguindo o caminho original. Jack usou todas as suas forças para mover a rocha, mas ela era muito pesada. Ele se esforçou tanto que acabou desmaiando de exaustão. Quando acordou, Jack se encontrava em uma caverna escura, cheia de morcegos gigantes e aranhas venenosas."
          )

        else:
          voltar += 1
          print("---------------------------------")
          print("-- Responda apenas com 1 ou 2. --")
          print("---------------------------------")

        if voltar == 0:
          print()
          print("Suas chances acabaram, Jack não conseguiu seu tesouro.")
          sys.exit()

    else:
      print("---------------------------------")
      print("-- Responda apenas com 1 ou 2. --")
      print("---------------------------------")


def fase5(resposta, voltar):
  correta = "1"
  resposta = 0
  print()
  print(
    "Após conseguir contornar a pedra, Jack finalmente chegou à clareira onde o tesouro estava escondido. Mas, para sua surpresa, encontrou uma caverna bloqueando a entrada. Ele precisava encontrar uma maneira de entrar. Lembrou-se então de um velho mapa que havia ganhado de seu avô"
  )
  print("Mas será que esse mapa realmente levará Jack para o tesouro?")
  while resposta != "1" or resposta != "2":
    print("---------------------------------")
    print("-- Qual caminho deseja seguir? --")
    print("---------------------------------")
    resposta = input("1 - Seguir o mapa. \n2 - Entrar na caverna à força. \nR: ")

    if resposta == "1":
      print()
      print(
        "Jack usa o mapa para encontrar uma entrada escondida na caverna. Ele descobre que o tesouro estava bem ali o tempo todo e comemora sua vitória!"
      )
      print(Fore.BLUE + """                                                 
                              ██████╗░░█████╗░██████╗░░█████╗░██████╗░███████╗███╗░░██╗░██████╗
                              ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗░██║██╔════╝
                              ██████╔╝███████║██████╔╝███████║██████╦╝█████╗░░██╔██╗██║╚█████╗░
                              ██╔═══╝░██╔══██║██╔══██╗██╔══██║██╔══██╗██╔══╝░░██║╚████║░╚═══██╗
                              ██║░░░░░██║░░██║██║░░██║██║░░██║██████╦╝███████╗██║░╚███║██████╔╝
                              ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░
      """)
      return resposta

    elif resposta == "2":
      print()
      print(
        "Jack decide entrar na caverna à força, mas um grupo de bandidos o espera lá dentro. Eles o capturam e Jack nunca mais é visto novamente."
      )
      while resposta != correta and voltar != 0:
        print()
        print("Tem apenas ", voltar, " chance(s), tente novamente:")
        voltar -= 1
        print("---------------------------------")
        print("-- Qual caminho deseja seguir? --")
        print("---------------------------------")
        resposta = input(
          "1 - Seguir o mapa. \n2 - Entrar na caverna à força. \nR: ")

        if resposta == "1":
          print()
          print(
            "Jack usa o mapa para encontrar uma entrada escondida na caverna. Ele descobre que o tesouro estava bem ali o tempo todo e comemora sua vitória!"
          )
          print(Fore.BLUE + """
                                    ██████╗░░█████╗░██████╗░░█████╗░██████╗░███████╗███╗░░██╗░██████╗
                                    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗░██║██╔════╝
                                    ██████╔╝███████║██████╔╝███████║██████╦╝█████╗░░██╔██╗██║╚█████╗░
                                    ██╔═══╝░██╔══██║██╔══██╗██╔══██║██╔══██╗██╔══╝░░██║╚████║░╚═══██╗
                                    ██║░░░░░██║░░██║██║░░██║██║░░██║██████╦╝███████╗██║░╚███║██████╔╝
                                    ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░
          """)

          return resposta

        elif resposta == "2":
          print()
          print(
            "Jack decide entrar na caverna à força, mas um grupo de bandidos o espera lá dentro. Eles o capturam e Jack nunca mais é visto novamente."
          )

        else:
          voltar += 1
          print("---------------------------------")
          print("-- Responda apenas com 1 ou 2. --")
          print("---------------------------------")

        if voltar == 0:
          print()
          print("Suas chances acabaram, Jack não conseguiu seu tesouro.")
          sys.exit()

    else:
      print("---------------------------------")
      print("-- Responda apenas com 1 ou 2. --")
      print("---------------------------------")


from colorama import Fore, Back, Style

resposta = []
voltar = 1
print(Fore.BLUE + ''' 
                                          ░░░░░██╗░█████╗░░█████╗░██╗░░██╗  ███████╗  ░█████╗░
                                          ░░░░░██║██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝  ██╔══██╗
                                          ░░░░░██║███████║██║░░╚═╝█████═╝░  █████╗░░  ██║░░██║
                                          ██╗░░██║██╔══██║██║░░██╗██╔═██╗░  ██╔══╝░░  ██║░░██║
                                          ╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗  ███████╗  ╚█████╔╝
                                          ░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚══════╝  ░╚════╝░
                                          
                                          ████████╗███████╗░██████╗░█████╗░██╗░░░██╗██████╗░░█████╗░
                                          ╚══██╔══╝██╔════╝██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔══██╗
                                          ░░░██║░░░█████╗░░╚█████╗░██║░░██║██║░░░██║██████╔╝██║░░██║
                                          ░░░██║░░░██╔══╝░░░╚═══██╗██║░░██║██║░░░██║██╔══██╗██║░░██║
                                          ░░░██║░░░███████╗██████╔╝╚█████╔╝╚██████╔╝██║░░██║╚█████╔╝
                                          ░░░╚═╝░░░╚══════╝╚═════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝░╚════╝░
''')
print()
print()
print(
  Fore.WHITE +
  "Era uma vez um jovem aventureiro chamado Jack, que decidiu explorar uma floresta densa e escura. Enquanto caminhava pelo meio das árvores, Jack encontrou uma bifurcação no caminho. À sua frente, havia dois caminhos a seguir, cada um levando a lugares diferentes."
)

print()

print(
  "Jack percebeu que havia um sinal indicando que um dos caminhos levava a um tesouro escondido."
)
print("Enquanto o outro caminho era um atalho para sair da floresta. ")
print()

resultado = fase1(resposta, voltar)
if resultado == "1":
  print()
  resultado = fase2(resposta, voltar)
  if resultado == "2":
    print()
    resultado = fase3(resposta, voltar)
    if resultado == "2":
      resultado = fase4(resposta, voltar)
      if resultado == "1":
        resultado == fase5(resposta, voltar)
