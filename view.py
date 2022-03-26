from tkinter import Tk, Frame, Canvas, Button, Entry, Label
import style as st

LEFT = "left"
RIGHT = "right"
TOP = "top"
BOTTOM = "bottom"

class View(Frame):
    """ 
    Acts as the View in an MVC pattern. This class extends tkinter.Frame.
    The View object defines the layout of the UI and assigns the correct Controller actions to each
    button and hotkey.

    Attributes:
        parent : the Tk root object which the View frame is contained within.
        canvas : the tkinter.Canvas object which the LSystem productions will be drawn to.
    """
    def __init__(self, parent, m):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        self.configure(height=600, width=800)
        self.init_block_bar()
        self.init_properties_bar()
        self.canvas = self.init_canvas()


    def init_block_bar(self):
        block_frame = Frame(self)
        block_frame.pack(side=LEFT, expand=True, fill="both")

        top_bar = Frame(block_frame)
        top_bar.pack(side=TOP)

        block_label = Label(top_bar, text="Block Selector", bg=st.BLOCK_LABEL)
        block_label.grid(column=0,row=0, sticky="NSEW")

        tab_frame = Frame(top_bar)
        tab_frame.grid(column=0,row=1)
        
        var_tab = Button(tab_frame,text="Vars", bg=st.VAR_TAB)
        var_tab.grid(column=0,row=0)

        obj_tab = Button(tab_frame,text="Obj", bg=st.OBJ_TAB)
        obj_tab.grid(column=1,row=0)

        func_tab = Button(tab_frame,text="Funcs", bg=st.FUNC_TAB)
        func_tab.grid(column=2,row=0)

        array_frame = Frame(block_frame, bg=st.ARRAY_BG)
        array_frame.pack(side=BOTTOM, expand=True, fill="both")

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

        c = Canvas(canvas_frame)
        c.configure(height=600, width=800)
        c.pack(side=RIGHT, padx=10, pady=10)

        return c

    def clear_canvas(self):
        """
        Clears all existing lines from the canvas.
        """
        self.canvas.delete("all")
        self.canvas.create_rectangle(0,0,800,600, fill="#FFFFFF")

    def draw_line(self, line_obj):
        """
        Draws a line to the canvas based on the given Line object
        """

        self.canvas.create_line(
            line_obj.startx,
            line_obj.starty,
            line_obj.endx,
            line_obj.endy,
            fill="#%02x%02x%02x" % line_obj.colour,
            width=line_obj.width)

           
