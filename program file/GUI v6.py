import tkinter as tk

LARGE_FONT= ("Ariel", 15)

class Gui_Main(tk.Tk):

    def __init__(self, *args, **kwargs):#**kwargs allows me to pass as many frames as I need into the self.frames dictionary on line 16
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}#dictionary to hold the different frames
        
        self.frames["MainMenu"] = MainMenu(parent=container, controller=self)
        self.frames["Instructions"] = Instructions(parent=container, controller=self)


        self.frames["MainMenu"].grid(row=0, column=0, sticky="nsew")
        self.frames["Instructions"].grid(row=0, column=0, sticky="nsew")


        self.show_frame("MainMenu")#uses the method below to raise the MainMenu frame so it is the first frame to appear on screen

    def show_frame(self, cont):#this method is responsible for updating the frame with one of the classes below

        frame = self.frames[cont]#takes all frames defined in the constructor
        frame.tkraise()#raises the frame defined by the program



        
class MainMenu(tk.Frame):#this class holds the contents of the MainMenu frame

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self, text="Main Menu", font=LARGE_FONT).pack(side="top",fill="x",pady=20)
        button1 = tk.Button(self,text="Start",font=LARGE_FONT,command=lambda: controller.show_frame("SeasonPage")).pack()
        button2 = tk.Button(self,text="Instructions",font = LARGE_FONT,command=lambda: controller.show_frame("Instructions")).pack()
        

class Instructions(tk.Frame):#this class holds the contents of the Instructions frame
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        instr_text = """ To use the simulation press start on the main menu then select a speed at which to run the simulation.
        To access information on the simulation screen press the statistics button.
        For current information refer to the activity feed on the right of the map for all actions being made.
        """
        
        label1 = tk.Label(self,text=instr_text,font = LARGE_FONT).pack(side="top",fill="x",pady=20)
        button1 = tk.Button(self,text="Back to main menu",font = LARGE_FONT,command=lambda: controller.show_frame("MainMenu")).pack()


class SimulationMain(tk.Frame):
    def __init__(self,parent,controller):
        self.controller = controller
        tk.Frame.__init__(self,parent)
        pass


if __name__ == "__main__":    
    gui = Gui_Main()
    gui.mainloop()
