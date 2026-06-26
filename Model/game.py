class Game:

    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode(
            (WIN_WIDTH, WIN_HEIGHT)
        )

        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

        self.state = MENU

        self.menu = Menu(self.window)
        self.end_screen = EndScreen(self.window)

        self.snake = Snake()
        self.food = Food()
        self.score = Score()
        self.level = Level()

        self.food.spawn(self.snake)