from tkinter import * # used to create Graphical User Interface for desktop applications
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess # helps to create process and retrieve inputs, outputs or error in code

# create an instance for window
compiler = Tk()
# create title for window
compiler.title('Python IDE')
# create and configure menu
menu_bar = Menu(compiler)
compiler.config(menu= menu_bar)

# create editor window
editor = Text()
editor.pack(fill= BOTH, expand= 1)

# create output window
code_output = Text(height= 10)
# geometry manager organizes widgets in blocks before placing them in the parent widget.
code_output.pack()

file_path = ''

# function to open file
def open_file():
    global code,file_path
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

# function to save file
def save_as():
    global code,file_path
    path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    file_path = path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)

# funtion to excute the code and display output
def run():
    global code,file_path
    command = f'python {file_path}'
    # start a process
    process = subprocess.Popen(command, stdout= subprocess.PIPE, stderr =subprocess.PIPE, shell= True)
    # communicate() call reads input and output from the process stdout = process output , stderr error occurs.
    output, error = process.communicate()
    code_output.delete(1.0, END)
    code_output.insert(1.0, output)
    code_output.insert(1.0, error)

def light():
    editor.config(bg= 'white')
    code_output.config(bg= 'white')

def dark():
    editor.config(fg= 'white',  bg= 'black')
    code_output.config(fg= 'white', bg= 'black')

# create and define file menu
file_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label= 'File', menu= file_menu)
file_menu.add_command(label= 'Open', command= open_file)
file_menu.add_separator()
file_menu.add_command(label= 'Save', command= save_as)
file_menu.add_command(label= 'Save As', command= save_as)
file_menu.add_separator()
file_menu.add_command(label = 'Exit', command= exit)

# create and define run menu
run_bar = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label= 'Run', menu= run_bar)
run_bar.add_command(label= 'Run', command= run)

# create and define theme menu
theme_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = 'Theme', menu = theme_menu)
theme_menu.add_command(label= 'Light' , command= light)
theme_menu.add_command(label  'Dark' , command= dark)


code_output = Text(height = 10)
code_output.pack()
compiler.mainloop()
