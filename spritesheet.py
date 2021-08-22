import pygame
import json

class Spritesheet:
    def __init__(self,filename):
        self.filename = filename
        self.json_file = filename[0:-3] + "json"
        with open(self.json_file,"r") as file:
            str1 = file.read()   
            self.meta_data = json.loads(str1)
        
        self.state = "idle"
        self.face = "right"
        self.w = self.meta_data["size"]["width"]
        self.h = self.meta_data["size"]["height"]
        self.rows = self.meta_data["count"]["rows"]
        self.coulmns = self.meta_data["count"]["coulmns"]
        self.states = self.meta_data["states"]
        self.swing = 1
        
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.sprite_list = self.sprite_list()

    def get_sprite(self,x,y):
        sprite = pygame.Surface((self.w,self.h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0,0),(x,y,self.w,self.h))
        return sprite

    def sprite_list(self):
        sprite_list = []
        for y in range(self.rows):
            for x in range(self.coulmns):
                sprite_list.append(self.get_sprite(self.w*x,self.h*y))

        return sprite_list

    def set_state(self,new_state):
        self.state = new_state

    def get_state(self):
        return self.state

    def set_face(self,new_face):
        self.face = new_face
                       
    def get_state_indexes(self):
        if type(self.states[self.state]) == dict:
            return map(int,self.states[self.state][self.swing].split())
        else:
            return map(int,self.states[self.state].split())

    def reset_atack(self):
        self.swing = 1

    def get_face(self):
        return self.face

    def get_sprites(self):
        indexes = self.get_state_indexes()
        sprites = [self.sprite_list[index] for index in indexes]
        if self.face == "right":
            return sprites
        elif self.face == "left":
            sprites = [pygame.transform.flip(sprite, True, False) for sprite in sprites] 
        return sprites

