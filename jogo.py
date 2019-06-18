x = 376#define a posição da imagem
y= 324#a posição y da imagem
BLACK = (0, 0, 0)#define imagem preta
RESOL = [800, 600]#define tamanho da tela
LOOP  = True#define o loop para verdadero
POS = (x,y)#coloca a imagem na posição escolhida
SPRITE = "meme.png"#define a imagem

import pygame#importa o pygame
import serial#importa o serial
import time#importa o time

FUNDO = pygame.image.load("neymar_119.jpg")#define a imagem de fundo
ser = serial.Serial('COM11', 9600, timeout=0)#define onde esta o arduino

pygame.init()#inicia o pygame


screen = pygame.display.set_mode(RESOL)#cria a tela
screen.fill (BLACK)#coloca o fundo preto
sprite = pygame.image.load (SPRITE)#coloca a imagem
screen.blit (FUNDO, (0,0))# coloca o fundo



while LOOP:
    porta =ser.read()#le a porta
    decodificado=porta.decode('utf-8')#decodifica a porta
    time.sleep(0.2)#define o tempo de espera
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            LOOP = False
    screen.blit (sprite, POS)
   
    if decodificado == "E":#se letra'e' anda para a esquerda
        x=x-10
        POS = (x,y)
        pygame.display.update()
        

    if decodificado == "D":
        x=x+10
        POS = (x,y)
        pygame.display.update()


    if decodificado == "C":
        y=y+10
        POS = (x,y)
        pygame.display.update()

    if decodificado == "B":
        #print("teste1")
        y=y-10
        POS = (x,y)
        pygame.display.update()
        #print("teste2")
        
        
    print(decodificado)