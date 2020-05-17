# HELPFUL FOR ALIEN INVASION.
import pygame
# First, create you group
gems = pygame.sprite.Group()

class Jewel (pygame.sprite.Sprite): # Inherit from the Sprite
    def __init__ (self, *args): # Call the constructor with whatever arguments...
        # This next part is key. You call the super constructor, and pass in the
        # group you've created and it is automatically added to the group every
        # time you create an instance of this class
        pygame.sprite.Sprite.__init__(self, gems)
        self.hi = 1

        # rest of class stuff after this.
    def hi(self):
        print(self.hi)

ruby = Jewel()
diamond = Jewel()



# All three are now in the group gems.
print(gems.sprites())
gems.remove(diamond)
print(gems.sprites())