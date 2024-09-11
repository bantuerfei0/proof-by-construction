import os
import math
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
pygame.init()
class Proof:

    class Drawable:
        
        def __init__(self, color = pygame.Color(10, 10, 10)):
            self.color = color
        
        def draw(self, surface : pygame.Surface) -> None:
            pass

    class Vertex(Drawable):
        
        def __init__(self, color = pygame.Color(20, 20, 20), x = 0.0, y = 0.0):
            super().__init__(color)
            self.x = x
            self.y = y
        
        def draw(self, surface : pygame.Surface) -> None:
            pygame.draw.circle(surface, self.color, (self.x, self.y), 3)
    
    class Edge(Drawable):
        
        def __init__(self, color = pygame.Color(40, 40, 200), x1 = 0.0, y1 = 0.0, x2 = 100.0, y2 = 100.0):
            super().__init__(color)
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
        
        def draw(self, surface : pygame.Surface) -> None:
            pygame.draw.line(surface, self.color, (self.x1, self.y1), (self.x2, self.y2), 3)

    def __init__(self, n = 12) -> None:
        self.n = n # the n amount of nodes
        self.stop = False
        self.clock = pygame.time.Clock()
        self.WIDTH = 800
        self.HEIGHT = 800
        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Proof by Construction")
        pygame.display.set_icon(pygame.Surface((1,1)))
        self.vertices : list[Proof.Vertex] = []
        self.edges : list[Proof.Edge] = []
        self.generate_proof()
    
    def generate_proof(self) -> None:
        self.vertices = self.generate_vertices() # passing back like this probably doesn't need to be done
        self.edges = self.generate_edges(self.vertices)

    def generate_edges(self, vertices : list[Vertex]) -> list:
        edges = []
        for i in range(self.n - 1):
            edges.append(Proof.Edge(color=pygame.Color(200, 40, 40), x1 = vertices[i].x, y1 = vertices[i].y, x2 = vertices[i+1].x, y2 = vertices[i+1].y))
        edges.append(Proof.Edge(color=pygame.Color(40, 200, 40), x1=vertices[self.n-1].x, y1=vertices[self.n-1].y, x2=vertices[0].x, y2=vertices[0].y))
        for i in range(int(self.n / 2)):
            edges.append(Proof.Edge(color=pygame.Color(40, 40, 200), x1 = vertices[i].x, y1 = vertices[i].y, x2 = vertices[int(i + self.n/2)].x, y2 = vertices[int(i + self.n/2)].y))
        return edges
    
    def generate_vertices(self) -> list:
        mid_x = self.WIDTH / 2
        mid_y = self.HEIGHT / 2
        dist_from_mid = min(self.WIDTH, self.HEIGHT) / 2 * 0.9
        slice_angle = (math.pi * 2) / self.n # angle per vertex from center
        vertices = [] # not the same as verticies
        for i in range(self.n):
            vertices.append(Proof.Vertex(x=mid_x + math.cos(slice_angle * i) * dist_from_mid, y= mid_y +math.sin(slice_angle * i) * dist_from_mid))
        return vertices
    
    def start(self) -> None:
        while not self.stop:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.stop = True
                    pygame.image.save(self.surface, "proof.png")
            self.surface.fill(pygame.Color(240, 240, 240)) # hopefully this isn't instantiated every tick
            for edge in self.edges:
                edge.draw(self.surface)
            for vertex in self.vertices:
                vertex.draw(self.surface)
            pygame.display.update()
            self.clock.tick(10)
    
if __name__ == "__main__":
    app = Proof(12) # modify passed in n
    app.start()