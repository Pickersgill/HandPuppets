from tkinter import Button
import style as st

class Variable:
    def __init__(self, name, display_name=None):
        if display_name == None:
            self.display_name = name
        else:
            self.display_name = display_name
        self.name = name
        self.colour = st.random()


class Model:
    def __init__(self, c):
        self.controller = c
        self.vars = list()
        self.selected_block_id = None

    def get_vars(self):
        return self.vars[:]

    def deselect(self):
        self.selected_block_id = None

    def select_block(self, bid):
        self.selected_block_id = bid    
    
    def add_var(self, var_name):
        if var_name not in map(lambda x : x.name, self.vars):
            self.vars.append(Variable(var_name))

    def get_var_by_name(self, name):    
        for var in self.vars:
            if var.name == name:
                return var

        print("FAILED TO FIND VAR %s" % name)
        return None
    

            

