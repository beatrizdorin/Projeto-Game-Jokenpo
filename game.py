import os
import random
from time import sleep

import emoji
import pygame

pygame.init()

def limpar_tela():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def jogar():
    pygame.mixer.music.load('mario_ex045.mp3')
    pygame.mixer.music.play()

    print('')
    print('-----------------------')
    print('        \033[34mJOKENPÔ\033[m')
    print('-----------------------')
    print('')

    sleep(1)

    escolha = str(input('ESCOLHA: PEDRA / PAPEL / TESOURA: ')).upper()

    print('')
    print('        JO')
    sleep(1)
    print('        KEN')
    sleep(1)
    print('        PO!!')
    sleep (1)

    lista = ['PEDRA', 'PAPEL', 'TESOURA']
    pc_escolha = random.choice(lista)
    print('')
    print(pc_escolha)

    if pc_escolha == 'PEDRA':
     print(emoji.emojize(':raised_fist:'))
    elif pc_escolha == 'PAPEL':
     print(emoji.emojize(':raised_hand:'))
    elif pc_escolha == 'TESOURA':
     print(emoji.emojize(':victory_hand:'))

    print('')

    if escolha == pc_escolha:
       print('\033[33mEMPATE\033[m')
    elif escolha == 'PEDRA' and pc_escolha == 'PAPEL':
       print('\033[31mPERDEU\033[m')
    elif escolha == 'PAPEL' and pc_escolha == 'PEDRA':
      print ('\033[32mGANHOU\033[m')

    elif escolha == 'PAPEL' and pc_escolha == 'TESOURA':
      print ('\033[31mPERDEU\033[m')
    elif escolha == 'TESOURA' and pc_escolha == 'PAPEL':
     print ('\033[32mGANHOU\033[m')

    elif escolha == 'PEDRA' and pc_escolha == 'TESOURA':
      print ('\033[32mGANHOU\033[m')
    elif escolha == 'TESOURA' and pc_escolha == 'PEDRA':
      print('\033[31mPERDEU\033[m')

while True:
    jogar()
    resposta = input('   Deseja jogar novamente? (s/n): ').lower()
    if resposta == 's':
        limpar_tela()
    elif resposta == 'n':
        print('   Obrigado por jogar!')
        break

pygame.mixer.music.stop()
pygame.quit()