import chess
import tkinter
import tkinter.messagebox

'''
타이머 추가 해야함
'''

brd = tkinter.Tk()
brd.geometry("640x640+310+0")
brd.resizable(False, False)
brd.title("Play Chess")

bg = tkinter.Canvas(brd, width=640, height=640, bg="sienna")
bg.pack()
bg.place(x=0, y=0)

board = chess.Board()

x = 0
y = 0
which_to_move = ''
which_to_place = ''
which_to_promote = ''
promote_initial = 'q'
promote_buttons = []

name = ''
name_id = ''

ox = 0
oy = 0

cango = []

original_board = ''
last_move_board = str(board)
last_move = ''

is_selected = False
is_selected_color = ''

turn = 'White'

pawnwhite = tkinter.PhotoImage(file='./images/white_pawn.png')
bishopwhite = tkinter.PhotoImage(file='./images/white_bishop.png')
knightwhite = tkinter.PhotoImage(file='./images/white_knight.png')
rookwhite = tkinter.PhotoImage(file='./images/white_rook.png')
kingwhite = tkinter.PhotoImage(file='./images/white_king.png')
queenwhite = tkinter.PhotoImage(file='./images/white_queen.png')

pawnblack = tkinter.PhotoImage(file='./images/black_pawn.png')
bishopblack = tkinter.PhotoImage(file='./images/black_bishop.png')
knightblack = tkinter.PhotoImage(file='./images/black_knight.png')
rookblack = tkinter.PhotoImage(file='./images/black_rook.png')
kingblack = tkinter.PhotoImage(file='./images/black_king.png')
queenblack = tkinter.PhotoImage(file='./images/black_queen.png')

file = 'abcdefgh'
rank = '12345678'

chess_board = []

for i in range(8):
    for j in range(8):
        chess_board.append(file[i]+rank[j])
        
def mouse(event):
    global x, y
    x, y = event.x, event.y

def location(x, y):
    if 0 <= x <= 80:
        a = 'a'
    elif 80 <= x <= 160:
        a = 'b'
    elif 160 <= x <= 240:
        a = 'c'
    elif 240 <= x <= 320:
        a = 'd'
    elif 320 <= x <= 400:
        a = 'e'
    elif 400 <= x <= 480:
        a = 'f'
    elif 480 <= x <= 560:
        a = 'g'
    elif 560 <= x <= 640:
        a = 'h'

    if 0 <= y <= 80:
        b = '8'
    elif 80 <= y <= 160:
        b = '7'
    elif 160 <= y <= 240:
        b = '6'
    elif 240 <= y <= 320:
        b = '5'
    elif 320 <= y <= 400:
        b = '4'
    elif 400 <= y <= 480:
        b = '3'
    elif 480 <= y <= 560:
        b = '2'
    elif 560 <= y <= 640:
        b = '1'

    return a+b

def aton(a):
    global file, rank
    
    if a[0] == 'a':
        x = 40
    elif a[0] == 'b':
        x = 120
    elif a[0] == 'c':
        x = 200
    elif a[0] == 'd':
        x = 280
    elif a[0] == 'e':
        x = 360
    elif a[0] == 'f':
        x = 440
    elif a[0] == 'g':
        x = 520
    elif a[0] == 'h':
        x = 600

    if a[1] == '8':
        y = 40
    elif a[1] == '7':
        y = 120
    elif a[1] == '6':
        y = 200
    elif a[1] == '5':
        y = 280
    elif a[1] == '4':
        y = 360
    elif a[1] == '3':
        y = 440
    elif a[1] == '2':
        y = 520
    elif a[1] == '1':
        y = 600

    return [x, y]

def preview():
    global cango, which_to_move, chess_board, name_id, name, file, rank, is_selected

    cango.clear()

    for h in alive:
        if h.location == which_to_move:
            name = h.tag
            name_id = h
            
    for i in chess_board:
        if which_to_move != i and chess.Move.from_uci(which_to_move+i) in board.legal_moves:
            cango.append(i)
        if which_to_move != i and name_id != '' and name_id.type == 'pawn' and chess.Move.from_uci(which_to_move+i+'q') in board.legal_moves:
            cango.append(i)
            
    for j in cango:
        circle = Circle(j)
            
    if name_id != '' and name_id.color == 'white':
        for k in alivew:
            bg.tag_raise(k.tag)
    else:
        for k in aliveb:
            bg.tag_raise(k.tag)
    
def click(event):
    global x, y, which_to_move, ox, oy, is_selected, is_selected_color

    brd.bind('<ButtonPress-1>')
    brd.bind('<ButtonRelease-1>')

    if 0 <= x <= 80:
        a = 'a'
        ox = 40
    elif 80 <= x <= 160:
        a = 'b'
        ox = 120
    elif 160 <= x <= 240:
        a = 'c'
        ox = 200
    elif 240 <= x <= 320:
        a = 'd'
        ox = 280
    elif 320 <= x <= 400:
        a = 'e'
        ox = 360
    elif 400 <= x <= 480:
        a = 'f'
        ox = 440
    elif 480 <= x <= 560:
        a = 'g'
        ox = 520
    elif 560 <= x <= 640:
        a = 'h'
        ox = 600

    if 0 <= y <= 80:
        b = '8'
        oy = 40
    elif 80 <= y <= 160:
        b = '7'
        oy = 120
    elif 160 <= y <= 240:
        b = '6'
        oy = 200
    elif 240 <= y <= 320:
        b = '5'
        oy = 280
    elif 320 <= y <= 400:
        b = '4'
        oy = 360
    elif 400 <= y <= 480:
        b = '3'
        oy = 440
    elif 480 <= y <= 560:
        b = '2'
        oy = 520
    elif 560 <= y <= 640:
        b = '1'
        oy = 600

    which_to_move = a+b

    locations = []

    if is_selected == True:
        is_selected = False
    if is_selected == False:
        is_selected = True
        
    for i in alive:
        locations.append(i.location)

    preview()
    
    if which_to_move in locations:
        bg.create_oval(ox-40, oy-40, ox+40, oy+40, fill='', outline='blue', tags='selected', width=3)

def bclk(a, b):
    global promote_initial, promote_buttons, alive, alivew, aliveb, name, name_id, turn
    
    promote_initial = a

    if b == 'white':
        w1 = 0
    else:
        w1 = 7
        
    for i in promote_buttons:
        i.destroy()

    if a == 'q':
        p1 = Queen(b, w1, file.find(which_to_place[0]), 'p')
    if a == 'n':
        p1 = Knight(b, w1, file.find(which_to_place[0]), 'p')
    if a == 'r':
        p1 = Rook(b, w1, file.find(which_to_place[0]), 'p')
    if a == 'b':
        p1 = Bishop(b, w1, file.find(which_to_place[0]), 'p')

    alive.append(p1)
    if b == 'white':
        alivew.append(p1)
    else:
        aliveb.append(p1)
        
    board.push(chess.Move.from_uci(which_to_move+which_to_place+which_to_promote+a))

    name_id = p1
    name = p1.tag

    if turn == 'White':
        turn = 'Black'
    else:
        turn = 'White'
    
    move_after()

    brd.bind('<ButtonPress-1>', click)
    brd.bind('<ButtonRelease-1>', release)
    
def promote():
    global window, x, y, name, name_id, which_to_place, which_to_move, file, rank, promote_buttons, alive
    
    k = aton(location(x, y))
    alpha = +40
    beta = 0
    bg1 = 'moccasin'
    bg2 = 'sienna'
    promote_buttons.clear()
    c = name_id.color
    
    if name_id.color == 'white':
        img1 = queenwhite
        img2 = knightwhite
        img3 = rookwhite
        img4 = bishopwhite
        if file.index(location(x, y)[0]) % 2 != 0:
            bg1, bg2 = bg2, bg1
            
    elif name_id.color == 'black':
        img1 = queenblack
        img2 = knightblack
        img3 = rookblack
        img4 = bishopblack
        alpha *= -1
        beta -= 80
        if file.index(location(x, y)[0]) % 2 == 0:
            bg1, bg2 = bg2, bg1

    qbtn =  tkinter.Button(brd, image=img1, command = lambda:bclk('q', c), bg=bg1, activebackground=bg1, overrelief='solid')
    qbtn.place(x=k[0]-40, y=k[1]-alpha+beta)
    
    nbtn =  tkinter.Button(brd, image=img2, command = lambda:bclk('n', c), bg=bg2, activebackground=bg2, overrelief='solid')
    nbtn.place(x=k[0]-40, y=k[1]+alpha+beta)
    
    rbtn =  tkinter.Button(brd, image=img3, command = lambda:bclk('r', c), bg=bg1, activebackground=bg1, overrelief='solid')
    rbtn.place(x=k[0]-40, y=k[1]+alpha*3+beta)
    
    bbtn =  tkinter.Button(brd, image=img4, command = lambda:bclk('b', c), bg=bg2, activebackground=bg2, overrelief='solid')
    bbtn.place(x=k[0]-40, y=k[1]+alpha*5+beta)

    promote_buttons.append(qbtn)
    promote_buttons.append(nbtn)
    promote_buttons.append(rbtn)
    promote_buttons.append(bbtn)

    brd.unbind('<ButtonPress-1>')
    brd.unbind('<ButtonRelease-1>')

def place(m, n):
    global x, y, which_to_place, name, name_id, ox, oy, alive, last_move_board, last_move, board, original_board, which_to_move, which_to_place, which_to_promote
    global is_selected, is_selected_color

    if which_to_move != which_to_place and chess.Move.from_uci(which_to_move+which_to_place) in board.legal_moves:
        board.push(chess.Move.from_uci(which_to_move+which_to_place))
        if name_id.type == 'king':
            if which_to_move[1] == which_to_place[1]:
                if abs(ox - x) >= 160:
                    if x < 300:
                        bg.coords(name, 200, n)
                        if name_id.color == 'white':
                            bg.coords(wrl.tag, 280, n)
                            name_id.location = location(200, n)
                            wrl.location = location(280, n)
                        else:
                            bg.coords(brl.tag, 280, n)
                            name_id.location = location(200, n)
                            brl.location = location(280, n)
                    else:
                        bg.coords(name, 520, n)
                        if name_id.color == 'white':
                            bg.coords(wrr.tag, 440, n)
                            name_id.location = location(520, n)
                            wrr.location = location(440, n)
                        else:
                            bg.coords(brr.tag, 440, n)
                            name_id.location = location(520, n)
                            brr.location = location(440, n)
                else:
                    bg.coords(name, m, n)
            else:
                bg.coords(name, m, n)
                
        elif name_id.type == 'pawn':
            if abs(int(which_to_move[1]) - int(which_to_place[1])) == 1:
                if name_id.color == 'white':
                    if which_to_move[1] == '5':
                        bpawn = []
                        for l in aliveb:
                            if which_to_place[0]+'5' == l.location:
                                bg.delete(l.tag)
                                aliveb.remove(l)
                else:
                    if which_to_move[1] == '4':
                        wpawn = []
                        for l in alivew:
                            if which_to_place[0]+'4' == l.location:
                                bg.delete(l.tag)
                                alivew.remove(l)
                                
                alive = alivew + aliveb
                bg.coords(name, m, n)
                
            else:
                bg.coords(name, m, n)
        else:
            bg.coords(name, m, n)

        move_after()
            
    elif which_to_move != which_to_place and name_id != '' and name_id.type == 'pawn' and chess.Move.from_uci(which_to_move+which_to_place+promote_initial) in board.legal_moves:
        promote()
        bg.coords(name, m, n)
        
        move_after()
      
    else:
        bg.coords(name, ox, oy)

    name = ''
    name_id = ''
        
def release(event):
    global x, y, which_to_place, name, name_id, ox, oy, alive, last_move_board, last_move, board, original_board, which_to_move, which_to_place, which_to_promote, already
    global is_selected, is_selected_color

    if is_selected == True:
        bg.delete('wherecango')
        bg.delete('selected')
        
    original_board = board
    
    if 0 <= x <= 80:
        a = 'a'
        m = 40
    elif 80 <= x <= 160:
        a = 'b'
        m = 120
    elif 160 <= x <= 240:
        a = 'c'
        m = 200
    elif 240 <= x <= 320:
        a = 'd'
        m = 280
    elif 320 <= x <= 400:
        a = 'e'
        m = 360
    elif 400 <= x <= 480:
        a = 'f'
        m = 440
    elif 480 <= x <= 560:
        a = 'g'
        m = 520
    elif 560 <= x <= 640:
        a = 'h'
        m = 600
    else:
        which_to_place = which_to_move

    if 0 <= y <= 80:
        b = '8'
        n = 40
    elif 80 <= y <= 160:
        b = '7'
        n = 120
    elif 160 <= y <= 240:
        b = '6'
        n = 200
    elif 240 <= y <= 320:
        b = '5'
        n = 280
    elif 320 <= y <= 400:
        b = '4'
        n = 360
    elif 400 <= y <= 480:
        b = '3'
        n = 440
    elif 480 <= y <= 560:
        b = '2'
        n = 520
    elif 560 <= y <= 640:
        b = '1'
        n = 600
    else:
        which_to_place = which_to_move
    
    try:
        which_to_place = a+b
    except:
        which_to_place = which_to_move
    
    place(aton(which_to_place)[0], aton(which_to_place)[1])

def move_after():
    global x, y, which_to_place, name, name_id, ox, oy, alive, last_move_board, last_move, board, which_to_move, which_to_place, original_board, turn
    
    last_move_board = str(board)
    last_move = name_id

    bg.delete('checked')
    
    if name_id != '' and original_board != last_move_board:
        bg.delete('did')

    if name_id != '':  
        name_id.location = which_to_place

    p = aton(which_to_move)[0]
    q = aton(which_to_move)[1]
    r = aton(which_to_place)[0]
    s = aton(which_to_place)[1]
        
    bg.create_rectangle(p-38, q-38, p+38, q+38, fill='', outline='green', tags='did', width=4)
    bg.create_rectangle(r-38, s-38, r+38, s+38, fill='', outline='green', tags='did', width=4)

    for i in alive:
        if i.location == which_to_place and i != name_id:
            bg.delete(i.tag)
            if i.color == 'white':
                alivew.remove(i)
            else:
                aliveb.remove(i)

    alive = alivew + aliveb

    print(board)

    if board.is_checkmate():
        print("checkmate")
        tkinter.messagebox.showinfo("Checkmate", "{} Won by Checkmate".format(turn))
    elif board.is_check():
        print("check")
        if turn == 'White':
            p = aton(bkr.location)[0]
            q = aton(bkr.location)[1]
            bg.create_oval(p-40, q-40, p+40, q+40, fill='', outline='red', tags='checked', width=3)
        else:
            p = aton(wkr.location)[0]
            q = aton(wkr.location)[1]
            bg.create_oval(p-40, q-40, p+40, q+40, fill='', outline='red', tags='checked', width=3)    
    elif board.is_stalemate():
        print("stalemate")
        tkinter.messagebox.showinfo("Stalemate", "Draw by Stalemate")
    elif board.is_insufficient_material():
        print("insufficient material")
        tkinter.messagebox.showinfo("Insufficient Material", "Draw by Insufficient Material")

    if turn == 'White':
        turn = 'Black'
    else:
        turn = 'White'

    name = ''
    name_id = ''
    last_move = ''
    
def drag(event):
    global x, y, alive, name, name_id, chess_board, cango, which_to_move, ox, oy
    x = event.x
    y = event.y

    for i in alive:
        if i.location == which_to_move:
            name = i.tag
            name_id = i
            
    bg.coords(name, x, y)

    preview()
    
def squares():
    a = 0
    b = 0
    c = [0, 80]
    for m in range(8):
        for n in range(4):
            bg.create_rectangle(a, b, a+80, b+80, fill="moccasin", outline="")
            a+=160
        a=c[m%2-1]
        b+=80
        
squares()

class Pawn:
    def __init__(self, color, w1, w2, dirc):
        self.color = color
        self.type = 'pawn'
        self.dirc = dirc
        self.tag = color+self.type+dirc
        self.location = location(w2*80+40, w1*80+40)
        if color == 'white':
            self.pawn = bg.create_image(w2*80+40, w1*80+40, image=pawnwhite,tags=color+self.type+dirc)
        else:
            self.pawn = bg.create_image(w2*80+40, w1*80+40, image=pawnblack,tags=color+self.type+dirc)

class Bishop:
    def __init__(self, color, w1, w2, dirc):
        self.color = color
        self.type = 'bishop'
        self.dirc = dirc
        self.tag = color+self.type+dirc
        self.location = location(w2*80+40, w1*80+40)
        if color == 'white':
            self.bishop = bg.create_image(w2*80+40, w1*80+40,image=bishopwhite,tags=color+self.type+dirc)
        else:
            self.bishop = bg.create_image(w2*80+40, w1*80+40,image=bishopblack,tags=color+self.type+dirc)

class Knight:
    def __init__(self, color, w1, w2, dirc):
        self.color = color
        self.type = 'knight'
        self.dirc = dirc
        self.tag = color+self.type+dirc
        self.location = location(w2*80+40, w1*80+40)
        if color == 'white':
            self.knight = bg.create_image(w2*80+40, w1*80+40, image=knightwhite,tags=color+self.type+dirc)
        else:
            self.knight = bg.create_image(w2*80+40, w1*80+40, image=knightblack,tags=color+self.type+dirc)

class Rook:
    def __init__(self, color, w1, w2, dirc):
        self.color = color
        self.type = 'rook'
        self.dirc = dirc
        self.tag = color+self.type+dirc
        self.location = location(w2*80+40, w1*80+40)
        if color == 'white':
            self.rook = bg.create_image(w2*80+40, w1*80+40, image=rookwhite,tags=color+self.type+dirc)
        else:
            self.rook = bg.create_image(w2*80+40, w1*80+40, image=rookblack,tags=color+self.type+dirc)

class King:
    def __init__(self, color, w1, w2, dirc):
        self.color = color
        self.type = 'king'
        self.dirc = dirc
        self.tag = color+self.type+dirc
        self.location = location(w2*80+40, w1*80+40)
        if color == 'white':
            self.king = bg.create_image(w2*80+40, w1*80+40, image=kingwhite,tags=color+self.type+dirc)
        else:
            self.king = bg.create_image(w2*80+40, w1*80+40, image=kingblack,tags=color+self.type+dirc)

class Queen:
    def __init__(self, color, w1, w2, dirc):
        self.color = color
        self.type = 'queen'
        self.dirc = dirc
        self.tag = color+self.type+dirc
        self.location = location(w2*80+40, w1*80+40)
        if color == 'white':
            self.queen = bg.create_image(w2*80+40, w1*80+40, image=queenwhite,tags=color+self.type+dirc)
        else:
            self.queen = bg.create_image(w2*80+40, w1*80+40, image=queenblack,tags=color+self.type+dirc)

class Circle:
    def __init__(self, loc):
        self.x = aton(loc)[0]
        self.y = aton(loc)[1]
        self.tag = 'wherecango'
        self.circle = bg.create_oval(self.x-10, self.y-10, self.x+10, self.y+10, fill='silver', tags='wherecango')
        
# white pawns
wpa = Pawn("white", 6, 0, 'a')
wpb = Pawn("white", 6, 1, 'b')
wpc = Pawn("white", 6, 2, 'c')
wpd = Pawn("white", 6, 3, 'd')
wpe = Pawn("white", 6, 4, 'e')
wpf = Pawn("white", 6, 5, 'f')
wpg = Pawn("white", 6, 6, 'g')
wph = Pawn("white", 6, 7, 'h')
# white rooks
wrl = Rook("white", 7, 0, 'l')
wrr = Rook("white", 7, 7, 'r')
# white knights
wnl = Knight("white", 7, 1, 'l')
wnr = Knight("white", 7, 6, 'r')
# white bishops
wbl = Bishop("white", 7, 2, 'l')
wbr = Bishop("white", 7, 5, 'r')
# white queen
wql = Queen("white", 7, 3, 'l')
# white king
wkr = King("white", 7, 4, 'r')

alivew = [wpa, wpb, wpc, wpd, wpe, wpf, wpg, wph, wrl, wrr, wbl, wbr, wnl, wnr, wql, wkr]

# black pawns
bpa = Pawn("black", 1, 0, 'a')
bpb = Pawn("black", 1, 1, 'b')
bpc = Pawn("black", 1, 2, 'c')
bpd = Pawn("black", 1, 3, 'd')
bpe = Pawn("black", 1, 4, 'e')
bpf = Pawn("black", 1, 5, 'f')
bpg = Pawn("black", 1, 6, 'g')
bph = Pawn("black", 1, 7, 'h')
# black rooks
brl = Rook("black", 0, 0, 'l')
brr = Rook("black", 0, 7, 'r')
# black knights
bnl = Knight("black", 0, 1, 'l')
bnr = Knight("black", 0, 6, 'r')
# black bishops
bbl = Bishop("black", 0, 2, 'l')
bbr = Bishop("black", 0, 5, 'r')
# black queen
bql = Queen("black", 0, 3, 'l')
# black king
bkr = King("black", 0, 4, 'r')

aliveb = [bpa, bpb, bpc, bpd, bpe, bpf, bpg, bph, brl, brr, bbl, bbr, bnl, bnr, bql, bkr]

alive = alivew + aliveb

brd.bind('<Motion>', mouse)
brd.bind('<B1-Motion>', drag)
brd.bind('<ButtonPress-1>', click)
brd.bind('<ButtonRelease-1>', release)

brd.mainloop()
