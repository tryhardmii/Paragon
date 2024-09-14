
import pygame
from items import item
pygame.init()
class monster:
    def __init__(self,name,image,HP,damage,spawnrate,drops):
        self.drops = drops
        self.dropstring = "".join([x.name for x in drops])
        self.name = name
        self.image = pygame.image.load(image).convert()
        self.image = pygame.transform.scale(self.image,(128,128))
        self.posx = 608
        self.posy = 0
        self.rect = self.image.get_rect(center=(self.posx,self.posy))
        self.spawnrate = spawnrate #lower number = lower spawnrate
        self.maxHP = HP
        self.HP = HP
        self.damage = damage
    def move(self,displacedx,displacedy):
        self.posx+=displacedx
        self.posy+=displacedy
        self.rect = self.image.get_rect(center=(self.posx,self.posy))

#drops, cost is for the sell value
#drops sorted as list to make monsters list more readable
drops = [item("Egg","graphics/drops/bridge_egg.png",100),
         item("String","graphics/drops/melody_hair.png",100),
         item("Pearl","graphics/drops/silent_pearl.png",100),
         item("Diamond","graphics/drops/diamond_spreading.png",200),
         item("Essence","graphics/drops/true_essence.png",100),
         item("Crystal","graphics/drops/crystal_frag.png",400),
         item("Star","graphics/drops/catalyst.png",300),
         item("Night Star","graphics/drops/night_crystal.png",600),
         item("Web","graphics/drops/tarantula_silk.png",500),
         item("Golden Tooth","graphics/drops/golden_tooth.png",500),
         item("Tooth","graphics/drops/tooth.png",500),
         item("Day Star","graphics/drops/day_crystal.png",500),
         item("Crown","graphics/drops/tarantula_silk.png",1000),
         ]

#monsters, each list is a different area
monsterlist = [[monster("ghost","graphics/area1monsters/ghost.png",100,100,6,[drops[0]]),
                monster("goblin","graphics/area1monsters/goblin.png",200,50,6, [drops[1]]),
                monster("loser","graphics/area1monsters/loser.png",250,50,1,[drops[2]]),
                monster("skeleton","graphics/area1monsters/skeleton.png",100,10,6,[drops[3]])],
               [monster("crab","graphics/area2monsters/crab.png",300,1,1,[drops[4]]),
                monster("frog","graphics/area2monsters/frog.png",300,1,1,[drops[5]]),
                monster("redspider","graphics/area2monsters/redspider.png",300,1,1,[drops[6]]),
                monster("rock","graphics/area2monsters/rock.png",300,1,1,[drops[7]])],
               [monster("circle","graphics/area3monsters/fatbitch.png",500,2,1,[drops[8]]),
                monster("iceghost","graphics/area3monsters/iceghost.png",500,2,1,[drops[9]]),
                monster("Creep","graphics/area3monsters/redweirdo.png",500,2,1,[drops[10]]),
                monster("skeleton2","graphics/area3monsters/skeleton2.png",500,2,1,[drops[11]])],
               [monster("wizard","graphics/npcs/wizard.png", 1000, 20, 1, [drops[12]])]]
                # wizard is the final boss and has its own area