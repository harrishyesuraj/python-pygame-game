#==================================#

import pygame as py
import interface as inter
import mobile_gamee as mg
import oooooo as O
import time


#==================================#


screen = py.display.set_mode((1080,2050))


#==================================#


def loading ():
    
    
    back = py.image.load("asset/image/loaded.jpg")
    Tback = py.transform.scale(back,(400,800))
    while True :
        screen.blit(Tback,(0,0))
        py.display.flip()
        time.sleep(1)
        break

                
#==================================#

      
class MAIN (mg.main):
  def main(self):
    running = True
    while running:
        loading ()
        a=inter.InterFace.face()
        loading ()
        if a == "PLAY" :
                    
                    self.screen.blit(self.size_bg,(0,0))
                    py.draw.rect(self.screen,(10,10,10),(0,0,400,100))
                    py.draw.rect(self.screen,(20,20,20),(10,10,380,80))
                    py.draw.rect(self.screen,(30,30,30),(20,20,360,60))
                    py.draw.rect(self.screen,(100,100,100),(30,30,340,40))
                    self.screen.blit(self.size_instructions,(0,0))
                    py.display.flip()
                    b=mg.Main.game()
                    
                    if b[0] == True :
                            c=O.final.going(b[1])
                            if c == "MENU" :
                                    running = True 
                    
                            elif c == "QUIT" : 
                                    running = False
                            
        elif a == "QUIT" :
                    running = False
    py.quit()
 
#==================================# 
                
                
MAIN=MAIN()


MAIN.main()
    
    
#==================================#     