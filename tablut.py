import pygame as pg
import os
import sys

SQUARE_SIZE = 52

SCREEN_SIZE = (9 * SQUARE_SIZE, 10 * SQUARE_SIZE)
SCREEN = pg.display.set_mode(SCREEN_SIZE)

WHITE = (255,255,255)
HIGHLIGHT = (220,75,75,255)

FPS = 60


class Player:
	def __init__(self, types, color):
		self.types = types
		self.lost_pieces = 0
		self.color = color

class Piece:
	def __init__(self, img_path, rect, type_str, color_str):
		self.img = pg.image.load(img_path)
		self.rect = self.img.get_rect(topleft = rect.topleft)
		self.type = type_str
		self.color = color_str
		self.speed = 4
		self.directions = {"up"    : self.move_up,
						   "down"  : self.move_down,
						   "right" : self.move_right,
						   "left"  : self.move_left}
		
	def draw(self):
		SCREEN.blit(self.img, self.rect)
	
	def move_up(self, board, new_square):
		clock = pg.time.Clock()
		while self.rect.y > new_square.y:
			self.rect.y -= self.speed
			self.update(board, clock)
	
	def move_down(self, board, new_square):
		clock = pg.time.Clock()
		while self.rect.y < new_square.y:
			self.rect.y += self.speed
			self.update(board, clock)
	
	def move_right(self, board, new_square):
		clock = pg.time.Clock()
		while self.rect.x < new_square.x:
			self.rect.x += self.speed
			self.update(board, clock)
			
	def move_left(self, board, new_square):
		clock = pg.time.Clock()
		while self.rect.x > new_square.x:
			self.rect.x -= self.speed
			self.update(board, clock)
	
	def move(self, board, new_square, dir_str):
		self.directions[dir_str](board, new_square)
	
	def update(self, board, clock):
		board.draw()
		self.draw()
		clock.tick(FPS)
		pg.display.update()
		
	
class Board:
	def __init__(self):
		self.light_square = pg.image.load("squareB.png")
		self.dark_square = pg.image.load("dark.png")
		self.corner_square = pg.image.load("corner.png")
		self.square_rects = [[None] * 9 for j in range(9)]
		self.squares = [[None] * 9 for j in range(9)]
		self.setup_squares()
		self._pieces = [[None] * 9 for i in range(9)]
		self.setup_pieces()
	
	def setup_pieces(self):
		dark = "pawnB2.png"
		lite = "pawnW2.png"
		king = "kingW.png"
		self._pieces[4][4] = Piece(king, self.square_rects[4][4], "king", "white") 
		self._pieces[2][4] = Piece(lite, self.square_rects[2][4], "light", "white")
		self._pieces[3][4] = Piece(lite, self.square_rects[3][4], "light", "white")
		self._pieces[5][4] = Piece(lite, self.square_rects[5][4], "light", "white") 
		self._pieces[6][4] = Piece(lite, self.square_rects[6][4], "light", "white") 
		self._pieces[4][2] = Piece(lite, self.square_rects[4][2], "light", "white")
		self._pieces[4][3] = Piece(lite, self.square_rects[4][3], "light", "white")
		self._pieces[4][5] = Piece(lite, self.square_rects[4][5], "light", "white")
		self._pieces[4][6] = Piece(lite, self.square_rects[4][6], "light", "white")   
		self._pieces[0][3] = Piece(dark, self.square_rects[0][3], "dark", "black")
		self._pieces[0][4] = Piece(dark, self.square_rects[0][4], "dark", "black") 
		self._pieces[0][5] = Piece(dark, self.square_rects[0][5], "dark", "black") 
		self._pieces[1][4] = Piece(dark, self.square_rects[1][4], "dark", "black")
		self._pieces[3][0] = Piece(dark, self.square_rects[3][0], "dark", "black")
		self._pieces[4][0] = Piece(dark, self.square_rects[4][0], "dark", "black")
		self._pieces[5][0] = Piece(dark, self.square_rects[5][0], "dark", "black")
		self._pieces[4][1] = Piece(dark, self.square_rects[4][1], "dark", "black")
		self._pieces[8][3] = Piece(dark, self.square_rects[8][3], "dark", "black")
		self._pieces[8][4] = Piece(dark, self.square_rects[8][4], "dark", "black")
		self._pieces[8][5] = Piece(dark, self.square_rects[8][5], "dark", "black")
		self._pieces[7][4] = Piece(dark, self.square_rects[7][4], "dark", "black")
		self._pieces[3][8] = Piece(dark, self.square_rects[3][8], "dark", "black")
		self._pieces[4][8] = Piece(dark, self.square_rects[4][8], "dark", "black")
		self._pieces[5][8] = Piece(dark, self.square_rects[5][8], "dark", "black")
		self._pieces[4][7] = Piece(dark, self.square_rects[4][7], "dark", "black")
		
		
			
	def setup_squares(self):
		# set up light squares with even indices
		# topleft of rect has to be (col, row), not (row, col) because
		# col is the x coord!!!
		for row in range(0, 9, 2):
			for col in range(0, 9, 2):
				square = self.light_square
				self.squares[row][col] = square
				self.square_rects[row][col] = square.get_rect(topleft = \
					(col * SQUARE_SIZE, row * SQUARE_SIZE))
				#print((row, col), self.square_rects[row][col].topleft)
		
		# set up light squares with odd indices
		for row in range(1, 9, 2):
			for col in range(1, 9, 2):
				square = self.light_square
				self.squares[row][col] = square
				self.square_rects[row][col] = square.get_rect(topleft = \
					(col * SQUARE_SIZE, row * SQUARE_SIZE))
		# set up dark squares with even rows and odd columns
		for row in range(0, 9, 2):
			for col in range(1, 9, 2):
				square = self.dark_square
				self.squares[row][col] = square
				self.square_rects[row][col] = square.get_rect(topleft = \
					(col * SQUARE_SIZE, row * SQUARE_SIZE))
		# set up dark squares with odd rows and even columns
		for row in range(1, 9, 2):
			for col in range(0, 9, 2):
				square = self.dark_square
				self.squares[row][col] = square
				self.square_rects[row][col] = square.get_rect(topleft = \
					(col * SQUARE_SIZE, row * SQUARE_SIZE))
		# set up the corner squares
		self.squares[0][0] = self.corner_square
		self.squares[0][8] = self.corner_square
		self.squares[8][8] = self.corner_square
		self.squares[8][0] = self.corner_square
		self.squares[4][4] = self.corner_square
	
	@property
	def pieces(self):
		return self._pieces
					
	def get_squares(self):
		return self.square_rects
	
	def check_path(self, src, dst):
		flag = False
		# if moving up
		if (src[0] > dst[0]) and (src[1] == dst[1]):
			for i in range(src[0]-1, dst[0]-1, -1):
				if self._pieces[i][src[1]]:
					flag = True
					break
			return False if flag else "up"
		# if moving down
		elif (src[0] < dst[0]) and (src[1] == dst[1]):
			for i in range(src[0]+1, dst[0]+1):
				if self._pieces[i][src[1]]:
					flag = True
					break
			return False if flag else "down"
		# if moving right
		elif (src[0] == dst[0]) and (src[1] < dst[1]):
			for i in range(src[1]+1, dst[1]+1):
				if self._pieces[src[0]][i]:
					flag = True
					break
			return False if flag else "right"
		# if moving left
		elif (src[0] == dst[0]) and (src[1] > dst[1]):
			for i in range(src[1]-1, dst[1]-1, -1):
				if self._pieces[src[0]][i]:
					flag = True
					break
			return False if flag else "left"
		else:
			return False
			
	def check_for_kills(self, player, row, col):
		typ = self._pieces[row][col].type
		# check for pieces to the left
		if col >= 2: # prevents IndexError
			r = self._pieces[row]
			c1, c2 = r[col-1], r[col-2]
			if c1 and c2 and c1.type != typ and c2.type == typ:
				yield (row, col-1)
		# check for kills to the right
		if col <= 6:
			r = self._pieces[row]
			c1, c2 = r[col+1], r[col+2]
			if c1 and c2 and c1.type != typ and c2.type == typ:
				yield (row, col+1)
		# check for kills above
		if row >= 2:
			r1, r2 = self._pieces[row-1][col], self._pieces[row-2][col]
			if r1 and r2 and r1.type != typ and r2.type == typ:
				yield (row-1, col)
		# check for kills below
		if row <=6:
			r1, r2 = self._pieces[row+1][col], self._pieces[row+2][col]
			if r1 and r2 and r1.type != typ and r2.type == typ:
				yield (row+1, col)
							
	def draw(self):
		for row in range(9):
			for col in range(9):
				rect = self.square_rects[row][col]
				if rect:
					SCREEN.blit(self.squares[row][col], self.square_rects[row][col])
				rect = self._pieces[row][col]
				if rect:
					SCREEN.blit(self._pieces[row][col].img, self._pieces[row][col].rect)
				

class Control:
	def __init__(self):
		self.done = False
		self.board = Board()
		self.clock = pg.time.Clock()
		self.highlight_coords = None # A tuple containing indices
		self.square_highlighted = None # A bool determining whether a square is selected
		self.selected_piece = None
		pieces = self.board.pieces
		self.player = player1
	
	def switch_player(self):
		if self.player == player1:
			self.player = player2
		else:
			self.player = player1
		
	def event_loop(self):
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					self.done = True
			if event.type == pg.MOUSEBUTTONDOWN:
				pos = pg.mouse.get_pos()
				squares = self.board.get_squares()
				pieces = self.board.pieces
				row = pos[1] // SQUARE_SIZE
				col = pos[0] // SQUARE_SIZE
				if self.square_highlighted:
					dir_ = self.board.check_path(self.highlight_coords, (row, col))
					if dir_:
						square = squares[row][col]
						self.selected_piece.move(self.board, square, dir_)
						coords = self.highlight_coords
						pieces[row][col] = pieces[coords[0]][coords[1]]
						pieces[coords[0]][coords[1]] = None
						# check for and erase killed pieces
						for row, col in set(self.board.check_for_kills(self.player, row, col)):
							pieces[row][col] = None
						self.switch_player()
					self.square_highlighted = False
					self.highlight_coords = None
				else:
					piece = pieces[row][col]
					if piece and piece.color == self.player.color:
						self.square_highlighted = True
						self.highlight_coords = (row, col)
						self.selected_piece = piece
							
	def main_loop(self):
		while not self.done:
			self.board.draw()
			if self.square_highlighted:
				pos = self.highlight_coords
				square = self.board.get_squares()[pos[0]][pos[1]]
				pg.draw.rect(SCREEN, HIGHLIGHT, square, 6)
			self.event_loop()
			self.clock.tick(FPS)
			pg.display.set_caption(str(int(self.clock.get_fps())))
			pg.display.update()


if __name__ == "__main__":		
	pg.init()
	pg.mouse.set_cursor(*pg.cursors.broken_x)	
	player1 = Player(("dark"), "black")
	player2 = Player(("light", "king"), "white")
	c = Control()
	c.main_loop()
	pg.quit()
	
