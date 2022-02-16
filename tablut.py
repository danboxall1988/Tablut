import pygame as pg

SCREEN_SIZE = (9 * 52, 9 * 52)
SCREEN = pg.display.set_mode(SCREEN_SIZE)

WHITE = (255,255,255)
HIGHLIGHT = (220,75,75,255)


class Piece:
	def __init__(self, img_path, rect, type_str):
		self.img = pg.image.load(img_path)
		self.rect = self.img.get_rect(topleft = rect.topleft)
		self.type = type_str
		
	def draw(self):
		SCREEN.blit(self.img, self.rect)
		
	def move(self, board, coords):
		clock = pg.time.Clock()
		while self.rect.x < coords[1]:
			self.rect.x += 1
			board.draw()
			SCREEN.blit(self.img, self.rect)
			pg.display.update()
			clock.tick(30)
		
	
class Board:
	def __init__(self):
		self.light_square = pg.image.load("squareB.png")
		self.dark_square = pg.image.load("dark.png")
		self.corner_square = pg.image.load("corner.png")
		self.square_rects = [[None] * 9 for j in range(9)]
		self.squares = [[None for i in range(9)] for j in range(9)]
		self.size = self.light_square.get_size()[0]
		self.setup_squares()
		self.pieces = [[0] * 9 for i in range(9)]
		self.setup_pieces()
		#self.square_rect = self.light_square.get_rect(topleft = (0,0))
	
	def setup_pieces(self):
		dark = "pawnB2.png"
		lite = "pawnW2.png"
		king = "kingW.png"
		self.pieces[2][4] = Piece(lite, self.square_rects[2][4], "light")
		self.pieces[3][4] = Piece(lite, self.square_rects[3][4], "light")
		self.pieces[4][4] = Piece(king, self.square_rects[4][4], "king") 
		self.pieces[5][4] = Piece(lite, self.square_rects[5][4], "light") 
		self.pieces[6][4] = Piece(lite, self.square_rects[6][4], "light") 
		self.pieces[4][2] = Piece(lite, self.square_rects[4][2], "light")
		self.pieces[4][3] = Piece(lite, self.square_rects[4][3], "light")
		self.pieces[4][5] = Piece(lite, self.square_rects[4][5], "light")
		self.pieces[4][6] = Piece(lite, self.square_rects[4][6], "light")   
		self.pieces[0][3] = Piece(dark, self.square_rects[0][3], "dark")
		self.pieces[0][4] = Piece(dark, self.square_rects[0][4], "dark") 
		self.pieces[0][5] = Piece(dark, self.square_rects[0][5], "dark") 
		self.pieces[1][4] = Piece(dark, self.square_rects[1][4], "dark")
		self.pieces[3][0] = Piece(dark, self.square_rects[3][0], "dark")
		self.pieces[4][0] = Piece(dark, self.square_rects[4][0], "dark")
		self.pieces[5][0] = Piece(dark, self.square_rects[5][0], "dark")
		self.pieces[4][1] = Piece(dark, self.square_rects[4][1], "dark")
		self.pieces[8][3] = Piece(dark, self.square_rects[8][3], "dark")
		self.pieces[8][4] = Piece(dark, self.square_rects[8][4], "dark")
		self.pieces[8][5] = Piece(dark, self.square_rects[8][5], "dark")
		self.pieces[7][4] = Piece(dark, self.square_rects[7][4], "dark")
		self.pieces[3][8] = Piece(dark, self.square_rects[3][8], "dark")
		self.pieces[4][8] = Piece(dark, self.square_rects[4][8], "dark")
		self.pieces[5][8] = Piece(dark, self.square_rects[5][8], "dark")
		self.pieces[4][7] = Piece(dark, self.square_rects[4][7], "dark")
		
		
			
	def setup_squares(self):
		# set up light squares with even indices
		# topleft of rect has to be (col, row), not (row, col) because
		# col is the x coord!!!
		for row in range(0, 9, 2):
			for col in range(0, 9, 2):
				square = self.light_square
				self.squares[row][col] = square
				self.square_rects[row][col] = square.get_rect(topleft = \
					(col * self.size, row * self.size))
				#print((row, col), self.square_rects[row][col].topleft)
		
		# set up light squares with odd indices
		for row in range(1, 9, 2):
			for col in range(1, 9, 2):
				square = self.light_square
				self.squares[row][col] = square
				self.square_rects[row][col] = square.get_rect(topleft = \
					(col * self.size, row * self.size))
		# set up dark squares with even rows and odd columns
		for row in range(0, 9, 2):
			for col in range(1, 9, 2):
				square = self.dark_square
				self.squares[row][col] = square
				self.square_rects[row][col] = square.get_rect(topleft = \
					(col * self.size, row * self.size))
		# set up dark squares with odd rows and even columns
		for row in range(1, 9, 2):
			for col in range(0, 9, 2):
				square = self.dark_square
				self.squares[row][col] = square
				self.square_rects[row][col] = square.get_rect(topleft = \
					(col * self.size, row * self.size))
		# set up the corner squares
		self.squares[0][0] = self.corner_square
		self.squares[0][8] = self.corner_square
		self.squares[8][8] = self.corner_square
		self.squares[8][0] = self.corner_square
	
	def get_pieces(self):
		return self.pieces
					
	def get_squares(self):
		return self.square_rects
						
	def draw(self):
		for row in range(9):
			for col in range(9):
				rect = self.square_rects[row][col]
				if rect:
					SCREEN.blit(self.squares[row][col], self.square_rects[row][col])
				rect = self.pieces[row][col]
				if rect:
					SCREEN.blit(self.pieces[row][col].img, self.pieces[row][col].rect)
		"""
		for row in range(0, 9, 2):
			for col in range(0, 9, 2):
				SCREEN.blit(self.squares[row][col], self.square_rects[row][col])
				SCREEN.blit(self.squares[row+1][col+1], self.square_rects[row+1][col+1])
				SCREEN.blit(self.squares[row][col+1], self.square_rects[row][col+1])
				SCREEN.blit(self.squares[row+1][col], self.square_rects[row+1][col])"""
				

class Control:
	
	def __init__(self):
		self.done = False
		self.board = Board()
		self.clock = pg.time.Clock()
		self.img = pg.image.load("pawnW.png")
		print("======================")
		self.y = 1
		pieces = self.board.get_pieces()
		self.highlight_coords = None
		self.square_highlighted = None
		"""
		pieces[0][5].move(self.board, (0, self.board.get_squares()[0][8].x))
		pieces[0][8] = pieces[0][5]
		pieces[0][5] = None"""
		
	def event_loop(self):
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					self.done = True
			if event.type == pg.MOUSEBUTTONDOWN:
				pos = pg.mouse.get_pos()
				squares = self.board.get_squares()
				#print(squares[0])
				for row in range(9):
					for col in range(9):
						if squares[row][col].collidepoint(pos):
							pieces = self.board.get_pieces()
							self.square_highlighted = True
							self.highlight_coords = (row, col)
								#print(SCREEN.get_at((0,0)))
								#pieces[row][col].move(self.board, (row, col+1))
								#pg.draw.rect(SCREEN,
							
				
	def main_loop(self):
		while not self.done:
			self.board.draw()
			#SCREEN.fill(WHITE)
			#SCREEN.blit(self.checkers[0], (0,0))
			#SCREEN.blit(self.img, self.board.get_squares()[2][0])
			#self.board.draw()
			#print(SCREEN.get_at((0,0)))
			if self.square_highlighted:
				pos = self.highlight_coords
				square = self.board.get_squares()[pos[0]][pos[1]]
				pg.draw.rect(SCREEN, HIGHLIGHT, square, 6)
			self.clock.tick(30)
			pg.display.update()
			self.event_loop()
			
c = Control()
c.main_loop()
