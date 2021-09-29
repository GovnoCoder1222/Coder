import pygame
import sys
import matplotlib
import random
import time


#Классы объектов
class Ants:
    def __init__(self,x_pos,y_pos,height,width,color,quantity):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height = height
        self.width = width
        self.color = color
        self.quantity = quantity

class Eats:
    def __init__(self, x_pos, y_pos, height, width):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height = height
        self.width = width


# Цвета, добавляются в диапазоне от 0 до 255. По три значения
Red = (255,0,0)
White = (255,255,255)
Green = (0,255,0)
Black = (0,0,0)
#Цвета для объектов
Eat_color = Green
Ant_color = White
#Высота и ширина бегающей точки
height = 5
width = 5


#Списки в которые записываются координаты зеленых точек по Х и У
Eats_pos_dict_x = []
Eats_pos_dict_y = []
quantity_for_while = 0
Ant_colony_1 = Ants(20, 50, height, width, Ant_color,0)
Colors = [Green,White]
#Функция вызова игры
def run_game():
    #Инициализация игры
    pygame.init()
    #Цикл
    whle = True
    while whle:
        #Размеры экрана
        win = pygame.display.set_mode((900, 850))


        #Рандомная позиция по Х и У
        pos_x = random.randint(10, 750)
        pos_y = random.randint(10, 750)
        #Запись позиции в список
        Eats_pos_dict_x.append(pos_x)
        Eats_pos_dict_y.append((pos_y))
        #Установка обхекта с указанием позиции
        Eat_Place = Eats(Eats_pos_dict_x[0], Eats_pos_dict_y[0], 4, 4)



        # Рисование обхектов на сцене
        Eats_col = pygame.draw.rect(win,(Colors[0]),
                                    (Eats_pos_dict_x[0],
                                     Eats_pos_dict_y[0],
                                     Eat_Place.height,
                                     Eat_Place.width))
        Ants_1 = pygame.draw.rect(win,(Red),
                                  (Ant_colony_1.x_pos,
                                   Ant_colony_1.y_pos,
                                   Ant_colony_1.height,
                                   Ant_colony_1.width))


        # Условия и тригеры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if Ant_colony_1.x_pos < Eats_pos_dict_x[0]:
                Ant_colony_1.x_pos += 1

            if Ant_colony_1.x_pos > Eats_pos_dict_x[0]:
                Ant_colony_1.x_pos -= 1
            if Ant_colony_1.y_pos < Eats_pos_dict_y[0]:
                Ant_colony_1.y_pos += 1
            if Ant_colony_1.y_pos > Eats_pos_dict_y[0]:
                Ant_colony_1.y_pos -= 1
            if Ant_colony_1.x_pos == Eats_pos_dict_x[0] and Ant_colony_1.y_pos == Eats_pos_dict_y[0]:
                #Удаление точки при достижении её
                Eats_pos_dict_x.pop(0)
                Eats_pos_dict_y.pop(0)
                print('Deleted X', Eats_pos_dict_x[0],'///', Eats_pos_dict_y[0])
                




        #Обновление экрана
        pygame.display.update()
#Инициализация запуска
run_game()









