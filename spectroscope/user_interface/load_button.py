from tkinter import *
from tkinter import filedialog
import csv

def openFile():   
   the_file = filedialog.askopenfilename(  # Open explorer
      title = "Select a .csv file",  
      filetypes = (("CSV Files","*.csv"),) # File type only csv
      )  
   with open(the_file, 'r') as csv_file:
      write = csv.writer(csv_file)
      file = csv_file.readlines()
      print(file)
      
window = Tk()

window.title('File Explorer')
window.geometry("500x500")


button_explore = Button(window, 
						text = "Load",
						command = openFile) 


button_explore.grid()


window.mainloop()
