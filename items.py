import pygame
class item():
    def __init__(self,name,imagestr,cost):
        self.name = name
        self.itemtype = "drops"
        self.imagestr = imagestr
        self.cost = cost
    def buy(self,player):
        player.gold -= self.cost
        player.inventory[self.itemtype].append(self)
    def sell(self,player):
        player.gold += self.cost/2
        player.inventory[self.itemtype].remove(self)
    def convert_dict(self):
        return self.__dict__


class weapon(item):
    def __init__(self, name, imagestr, cost, damage):
        super().__init__(name,imagestr,cost)
        #self.image = pygame.image.load(imagestr).convert_alpha()
        self.itemtype = "weapon"
        self.damage = damage

class defence(item):
    def __init__(self, name, imagestr, cost, blockpercentage):
        super().__init__(name,imagestr,cost)
        #self.image = pygame.image.load(imagestr).convert_alpha()
        self.itemtype = "defence"
        self.blockpercentage = blockpercentage

class rod(item):
    def __init__(self, name, imagestr, cost, chance):
        super().__init__(name,imagestr,cost)
        #self.image = pygame.image.load(imagestr).convert_alpha()
        self.itemtype = "rod"
        self.chance = chance

weaponlist = [weapon("Starter Sword","graphics/weapons/falchion.png",100,100000),
              weapon("Emerald Blade","graphics/weapons/emerald_blade.png",200,2000),
              weapon("Scythe","graphics/weapons/scythe.png",200,20),
              weapon("Silver Fang","graphics/weapons/silver_fang.png",200,20),
              weapon("Aspect of the Dragon","graphics/weapons/aotd.png",200,20)]

defencelist = [defence("Cheap Tuxedo","graphics/defences/cheap_jacket.png",100,0.1),
              defence("Elegant Tuxedo","graphics/defences/elegant_jacket.png",200,0.2),
              defence("Superior Dragon","graphics/defences/supdc.png",200,0.4)]
#rodlist = [rod("0.1","graphics/weapons/weapon1.png",100,0.1),
#              rod("0.2","graphics/weapons/weapon1.png",200,0.2), #we are not adding fishing touch yourself
#              rod("0.2","graphics/weapons/weapon1.png",200,0.2)]

shopitems = {"weapon":[weapon("Starter Sword","graphics/weapons/falchion.png",100,100000),
              weapon("Emerald Blade","graphics/weapons/emerald_blade.png",200,2000),
              weapon("Scythe","graphics/weapons/scythe.png",200,20),
              weapon("Silver Fang","graphics/weapons/silver_fang.png",200,20),
              weapon("Aspect of the Dragon","graphics/weapons/aotd.png",200,20)],
            "defence":[defence("Cheap Tuxedo","graphics/defences/cheap_jacket.png",100,0.1),
              defence("Elegant Tuxedo","graphics/defences/elegant_jacket.png",200,0.2),
              defence("Superior Dragon","graphics/defences/supdc.png",200,0.4)],
             "drops":[]}