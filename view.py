from tkinter import Tk, Frame, Canvas, Button, Entry, Label, PhotoImage
from block_canvas import BlockCanvas
import tkinter as tk
import style as st

LEFT = "left"
RIGHT = "right"
TOP = "top"
BOTTOM = "bottom"

class View(Frame):

    def __init__(self, parent, m):
        self.load_resources()
        Frame.__init__(self, parent)
        self.parent = parent
        self.model = m
        self.pack()
        self.configure(height=600, width=800)
        self.block_palette = self.init_block_bar()
        self.init_properties_bar()
        self.canvas = self.init_canvas()
        self.init_key_binds()

    def init_key_binds(self):
        self.parent.bind('<Control-q>', lambda x : exit())
        self.parent.bind('<Control-v>', lambda x : self.rebuild_vars())

    def load_resources(self):
        self.PLUS_IMG = PhotoImage(file=st.PLUS_IMG_PATH)

    def init_block_bar(self):
        block_frame = Frame(self)
        block_frame.pack(side=LEFT, expand=True, fill="both")

        top_bar = Frame(block_frame)
        top_bar.pack(side=TOP)

        block_label = Label(top_bar, text="Block Selector", bg=st.BLOCK_LABEL)
        block_label.grid(column=0,row=0, sticky="NSEW")

        array_frame = Frame(block_frame, bg=st.ARRAY_BG)
        array_frame.pack(side=BOTTOM, expand=True, fill="both")

        tab_frame = Frame(top_bar)
        tab_frame.grid(column=0,row=1)
        
        var_tab = Button(tab_frame,text="Vars.", bg=st.VAR_TAB, 
            command=self.rebuild_vars)
        var_tab.grid(column=0,row=0)

        obj_tab = Button(tab_frame,text="Obj.", bg=st.OBJ_TAB)
        obj_tab.grid(column=1,row=0)

        func_tab = Button(tab_frame,text="Funcs.", bg=st.FUNC_TAB)
        func_tab.grid(column=2,row=0)

        return array_frame

    def add_var_popup(self):
        popup = tk.Toplevel()
        popup.title("Add Variable")
    
        popup.configure(width=200)
    
        var_label = Label(popup, text="Variable Name")
        var_label.grid(row=0,column=0)

        entry = Entry(popup, bd=5)
        entry.grid(row=0,column=1)

        submit_button = Button(popup, text="Add"
            ,command=lambda : self.resolve_add_var(popup, entry))

        submit_button.grid(row=1,column=0, columnspan=2)

    def resolve_add_var(self, popup, entry):
        # TODO SANITIZE THE VARNAME
        self.model.add_var(entry.get())
        popup.destroy()
        self.rebuild_vars()
        
    
    def rebuild_vars(self):
        old_widgets = self.block_palette.winfo_children()
        for child in old_widgets:
            child.destroy()

        bp = self.block_palette

        for var in self.model.get_vars():
            self.build_var_button(var)

        add_var_popup = Button(bp, text = 'New Variable', 
            image = self.PLUS_IMG, 
            compound=LEFT,
            command=self.add_var_popup)
        add_var_popup.pack(side=TOP, padx=10, pady=10)
        
    def build_var_button(self, var):
        b = Button(self.block_palette, text=var.display_name, bg=var.colour
            ,command=lambda : self.block_clicked(var))
        b.pack(side=TOP,padx=5,pady=5, fill="x")

    def block_clicked(self, var):
        self.canvas.add_block(var)
    
    def init_properties_bar(self):
        prop_frame = Frame(self)
        prop_frame.configure(width=100)
        prop_frame.pack(side=RIGHT, expand=True,fill="both")

        top_bar = Frame(prop_frame)
        top_bar.pack(side=TOP)

        prop_label = Label(top_bar, text="Properties", bg=st.BLOCK_LABEL)
        prop_label.configure(width=25)
        prop_label.grid(column=0,row=0, sticky="NSEW")
        

    def init_canvas(self):
        """
        Initialises a new tkinter.Canvas object.
        """
        canvas_frame = Frame(self, bg=st.WORKSPACE_BORDER)
        canvas_frame.pack(side=RIGHT)

        c = BlockCanvas(canvas_frame, self.model)
        c.configure(height=600, width=800)
        c.pack(side=RIGHT, padx=10, pady=10)

        return c

    def clear_canvas(self):
        """
        Clears all existing lines from the canvas.
        """
        self.canvas.delete("all")
        self.canvas.create_rectangle(0,0,800,600, fill="#FFFFFF")

           
