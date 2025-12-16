import pygame as py

py.init()

screen=py.display.set_mode((400,800))
light_1 = (0,25,51)
dark_1 = (0,51,102)
light_2 = (192,192,192)
bark_2 = (224,224,224)

x = 70
y = 480
length = 120
breath = 60
Textx,Texty=92,497


#==================================#

class Final () :
    
    def rec (self,screen,colour,position):
        py.draw.rect(screen,colour,position)
        py.display.flip()
    
            
#==================================#
  
              
    def text (self,size,text,colour,position):
        font = py.font.Font(None,size)
        font_render = font.render(text,True,colour)
        screen.blit(font_render,position)
        py.display.flip()
  
              
#==================================#
  
              
    def going (self,score): # score_-_-_-_-
        #score = 0
        #self.rec(screen,(255,255,255),(0,0,400,800))
        
        concept = False
        
        BOX1 = py.Rect(x,y,length,breath)
        BOX2 = py.Rect(x+120+20,y,length,breath)
        bc=py.image.load("asset/image/game_over.png")
        Tbc=py.transform.scale(bc,(350,500))
        screen.blit(Tbc,(25,150)) #drawing 0
        #self.rec (screen,(255,255,50),(140,400,800,1200)) # drawing 0 ---
        
        self.rec (screen,light_1,BOX1) # drawing 1 rec
        self.rec (screen,light_1,BOX2) # drawing 2 rec
        
        self.text (45,"QUIT",light_2,(Textx,Texty))
        self.text (45,"MENU",light_2,(Textx+135,Texty)) # text - quit,menu 
        
        mz=py.image.load("asset/image/gameover.png")
        nx=py.image.load("asset/image/score.png")
        tr_mz=py.transform.scale(mz,(250,250))                     # image 1 game over
        tr_nx=py.transform.scale(nx,(150,80))
                   # image 2 score
        screen.blit(tr_mz,(70,160))
        screen.blit(tr_nx,(125,330))
            
        self.rec(screen,(200,200,200),(150,415,100,45))        
        z=str(score) #score
        while len(z)<3 :
            z="0"+z
        self.text(50,z,(255,0,0),(168,423))
        sound = py.mixer.Sound("asset/music/game_over.wav") #over sound
        mouse = py.mixer.Sound("asset/music/mouse.wav") #mouse sound
        sound.play()
        py.display.flip()
        
       
        
#==================================# 

        
        Running = True 
        
        while Running :
            
            for event in py.event.get():
                if event.type == py.QUIT : #quit
                    Running = False
                    
                    
                    
                elif event.type == py.MOUSEBUTTONDOWN : #                                                      mouse button down 
                    pos = py.mouse.get_pos()
                    if BOX1.collidepoint(pos):
                        self.rec (screen,dark_1,BOX1)
                        self.text (45,"QUIT",light_2,(Textx,Texty+1))
                        mouse.play()
        
                        
                    elif BOX2.collidepoint(pos):
                       self.rec (screen,dark_1,BOX2)
                       self.text (45,"MENU",light_2,(Textx+135,Texty+1))
                       mouse.play()
                       
                elif event.type == py.MOUSEBUTTONUP : #                                                      mouse button up 
                    if BOX1.collidepoint(pos):
                        self.rec (screen,light_1,BOX1)
                        self.text (45,"QUIT",light_2,(Textx,Texty))
                        concept = "QUIT"
                        return concept
                        
                    elif BOX2.collidepoint(pos):
                       self.rec (screen,light_1,BOX2)
                       self.text (45,"MENU",light_2,(Textx+135,Texty))
                       concept = "MENU"
                       return concept
            
            
#==================================#
                        
final = Final()  
#==================================#