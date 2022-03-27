from tkinter import Canvas
import style as st

uid = 0

class Block:
    def __init__(self, x, y, w, h, var):
        global uid
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.uid = uid
        uid += 1
        self.text_id = None
        self.block_id = None
        self.var = var

    def add_to_canvas(self, canvas):
        self.block_id = canvas.create_rectangle(
            self.x, 
            self.y, 
            self.x+self.w, 
            self.y+self.h, 
            fill=self.var.colour)
        self.text_id = canvas.create_text(self.x+self.w/2, self.y+self.h/2, 
            anchor="center", text=self.var.display_name)
    
    def move(self, canvas, newx, newy):
        dx = newx - (self.x + self.w/2)
        dy = newy - (self.y + self.h/2)
        self.x += dx
        self.y += dy

        canvas.move(self.block_id, dx, dy)
        canvas.move(self.text_id, dx, dy)

    def contains(self, x, y):
        return (x > self.x and x < self.x+self.w and y > self.y and y < self.y+self.h)
        

class BlockCanvas(Canvas):
    def __init__(self, root, model):
        Canvas.__init__(self, root)
        self.parent = root
        self.model = model
        self.blocks = {}
        self.bind("<Motion>", self.drag)
        self.bind("<Button-1>", self.click)

    def get_block_by_tkid(self, bid):
        for b in self.blocks.values():
            if b.block_id == bid or b.text_id == bid:
                return b
        return None

    def add_block(self, var):
        b = Block(0, 0, 100, 100, var)
        b.add_to_canvas(self)
        self.model.select_block(b.uid)
        self.blocks[b.uid] = b
    
    def drag(self, ev):
        bid = self.model.selected_block_id
        if bid is not None:
            self.blocks[bid].move(self, ev.x, ev.y)

    def click(self, ev):
        if self.model.selected_block_id is not None:
            self.model.deselect()
        else:
            b = self.get_block_by_tkid(self.find_closest(ev.x, ev.y)[0])
            if b.contains(ev.x, ev.y):
                self.model.select_block(b.uid)
    

