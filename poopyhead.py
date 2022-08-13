import pygame
from time import sleep
pygame.mixer.init()
siren = pygame.mixer.Sound("siren.wav")
fart1 = pygame.mixer.Sound("fart1.wav")
fart2 = pygame.mixer.Sound("fart2.wav")
fart3 = pygame.mixer.Sound("fart3.wav")


def poopyhead():
    
    person = input(str("\nEnter name to find out if they are a poopy head: "))
    
    if person.lower() == "finley":
        print("\n" + person + "? older brother of ferron? yes. the biggest poopy head of all.")
        fart1.play()
        for i in range(1, 10, 1):
            print(i)
            sleep(.1)
        
    elif person.lower() == "ferron":
        print("\n" + person + "? younger brother of finley? yes. ferron is a mucho numero dos poopy head.")
        fart2.play()
        
    elif person.lower() == "jim" or person.lower() == "matt":
        print("\n" + person + "? big grey & crusty poopy head.")
        fart3.play()
    
    elif person.lower() == "debbie" or person.lower() == "diane":
        print("\n" + person + "? you should be embarrassed to even question their poopy headedness.")
    
    elif person.lower() == "mom" or person.lower() == "dad":
        print("\n" + person + "? poopiness over load.... computer crashing... please reboot... nuclear missiles launching...")
        siren.play()  
    else:
        print("\nhmmm, "+person + "? I do not currently know the degree of poopiness to " + person + "'s head.")
    pygame.mixer.fadeout(8000)    
    input("\ncontinue...")
    poopyhead()
    
    
    
poopyhead()