from settings import * 
from sprites import *
from player import*

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('POKI')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups 
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        map=load_pygame(join('data','maps','world.tmx'))

        for x,y,image in map.get_layer_by_name('Main').tiles():
            Sprite((x*TILE_SIZE,y*TILE_SIZE),image,self.all_sprites)

        for x,y,image in map.get_layer_by_name('Decoration').tiles():
            Sprite((x*TILE_SIZE,y*TILE_SIZE),image,self.all_sprites)

        for obj in map.get_layer_by_name('Entities'):
            if obj.name=='Player':
                self.player=Player((obj.x,obj.y),(self.collision_sprites,self.all_sprites))

    def run(self):
        while self.running:
            dt = self.clock.tick(FRAMERATE) / 1000 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False 
            
            # update
            self.all_sprites.update(dt)

            # draw 
            self.display_surface.fill(BG_COLOR)
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run() 