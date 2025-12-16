import pygame as py
import random

class main ():

    py.init()

#==================================# 
    def __init__ (self):
            
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.red     = (255,10,10)
       
        
        self.recX =  150        #400 max
        self.recY = 700      #800 max           
        
        self.ballX = 30       
        self.ballY = 30 
        
        self.ballCX=4        #speed x
        self.ballCY=4        #speed y
        
        self.size = (400,800)
        self.score= 0
        
        self.screen = py.display.set_mode((self.size))
        self.img_font = py.font.SysFont("Ariel",40,bold=True)
        
        
        self.image = py.image.load('asset/image/bg.jpg')
        self.size_bg = py.transform.scale(self.image,(self.size[0],self.size[1]))
        
        
        self.image2 = py.image.load('asset/image/ball.png')
        self.size_ball = py.transform.scale(self.image2,(30,30))
        
        
        self.image3 = py.image.load('asset/image/pad.png')
        self.size_pad = py.transform.scale(self.image3,(100,10))
        
        self.image4 = py.image.load('asset/image/instructions.png')
        self.size_instructions = py.transform.scale(self.image4,(400,800))
        
        
        
        self.sound = py.mixer.Sound("asset/music/tap.wav")
        

        
        
        self.clock = py.time.Clock()
    
    #==================================# 
    
    
    def game (self):
            while True :
                for event in py.event.get():
                    if event.type==py.MOUSEBUTTONUP:
                        done = True
                        break
                    else :
                        done = False
                if done == True:
                        break
              
            self.score =0
            concept = False
            
            while done :
                for event in py.event.get() :
                    
                   if event.type == py.QUIT :
                       done =False
                       
            #==================================# 
                        
                        
                   elif event.type==py.MOUSEBUTTONDOWN :
                           
                      x,y = py.mouse.get_pos()
                      
                      if event.button == 1:
                          if x<(self.size[0]/2)  :
                             self.recCX = -50
                          elif (self.size[0]/2)<x :
                             self.recCX = 50
                            
                          self.recX+=self.recCX
                          
                          if self.recX <= 0 :
                             self.recX = 0
                          elif self.recX+100 >= 400 :
                             self.recX = 400-100
                          
                          
            #==================================# 
                                           
                                           
                                           
                if self.ballX < 0 :
                       self.ballX = 0
                       self.ballCX*=-1
                elif self.ballY < 100:
                       self.ballY = 100
                       self.ballCY*=-1
                elif self.ballX > 400-30 :
                       self.ballX =400-30
                       self.ballCX*=-1
                elif self.ballY > 800-30:
                       self.ballX= random.randint(0,401)
                       self.ballY = 0
                       concept = True
                       return concept,self.score
                      
                       
                elif BALL.colliderect(PAD):
                       self.ballY = 700-30
                       self.ballCY*=-1
                       self.sound.play()          
                       self.score+=1
                       
                  
                       
 #==================================#           
              
              
                self.screen.blit(self.size_bg,(0,0))
                
                
                self.ballX+=self.ballCX
                self.ballY+=self.ballCY
                
                
                self.screen.blit(self.size_ball,(self.ballX,self.ballY))
                self.screen.blit(self.size_pad,(self.recX,self.recY))
                
                
                self.img_text = self.img_font.render('SCORE = {}'.format(self.score),True,(75,25,100))         
                
                
                #--
                py.draw.rect(self.screen,(10,10,10),(0,0,400,100))
                py.draw.rect(self.screen,(20,20,20),(10,10,380,80))
                py.draw.rect(self.screen,(30,30,30),(20,20,360,60))
                py.draw.rect(self.screen,(100,100,100),(30,30,340,40))
                
                self.screen.blit(self.img_text,(200,40))
                
                BALL = py.Rect(self.ballX,self.ballY,30,30)
                PAD = py.Rect(self.recX,self.recY,100,10)
                                 
                                 
                
                py.display.flip()
                
                self.clock.tick(60)
        
    
    #==================================#
    
    
Main = main()

#==================================#