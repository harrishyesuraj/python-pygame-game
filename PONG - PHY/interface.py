import pygame as py


py.init()

blue = (0,25,51)
change_blue = (0,51,102)
change_black = (192,192,192)
black = (224,224,224)


b,w =200,80
xa =100
ya = 450


screen = py.display.set_mode((400,800))


image = py.image.load("asset/image/game.png")
back = py.image.load("asset/image/back.jpg")
Tback = py.transform.scale(back,(400,800))
mouse = py.mixer.Sound("asset/music/mouse.wav")


#==================================#


class INTERFACE ():
    
    
    def rect (self,screen,colour, position):
        py.draw.rect(screen,colour,position)
        py.display.update()
        
        
    def text (self,text,colour,position):
        img_font = py.font.SysFont("Arial",40,bold=True)
        img =img_font.render(text,True,colour)
        screen.blit(img,position)
        py.display.flip()
        
    
#==================================#


    def face(self):
        
        concept = False
        
        screen.blit(Tback,(0,0))
        
        mm = py.transform.scale(image,(300,300))
        screen.blit(mm,(50,50))
        
        self.rect_play =py.Rect(xa,ya,b,w)
        self.rect_quit = py.Rect(xa,ya+150,b,w)
        self.word_play=(xa+55,ya+18)
        self.word_quit=(xa+55,ya+150+18)
        self.word_playC=(xa+55,ya+18+1)
        self.word_quitC=(xa+55,ya+150+18+1)
        
        self.rect(screen,blue,self.rect_play)
        self.rect(screen,blue,self.rect_quit)
        self.text("PLAY",black,self.word_play)
        self.text("QUIT",black,self.word_quit)
    
   
     #==================================#
     
     
        inter = True
        while inter :
            
            for event in py.event.get():
                if event.type == py.QUIT :
                    py.quit()
                    
                if event.type==py.MOUSEBUTTONDOWN:
                   
                    x,y = py.mouse.get_pos()
                    
                    if self.rect_play.collidepoint(x,y) :
                        self.rect(screen,change_blue,self.rect_play)
                        self.text("PLAY",change_black,self.word_playC)
                        mouse.play()
                         
                    elif self.rect_quit.collidepoint(x,y) :
                        self.rect(screen,change_blue,self.rect_quit)
                        self.text("QUIT",change_black,self.word_quitC)
                        mouse.play()
                        
                        
                    
                if event.type == py.MOUSEBUTTONUP:
                    
                    if self.rect_play.collidepoint(x,y):
                       
                       self.rect(screen,blue,self.rect_play)
                       self.text("PLAY",black,self.word_play)
                       concept = "PLAY"
                       return concept
                       
                    elif self.rect_quit.collidepoint(x,y):
                       self.rect(screen,blue,self.rect_quit)
                       self.text("QUIT",black,self.word_quit)
                       concept = "QUIT"
                       return concept
                       
    
#==================================#

    
InterFace = INTERFACE()


#==================================#