from tkinter import *
from cell import Cell
import settings
import utils


root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.width}x{settings.height}')
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.width,
    height=utils.height_percent(20)
)
top_frame.place(x = 0, y = 0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper',
    font=('', 36)
)

game_title.place(
    x = utils.width_percent(30), y = 10
)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_percent(20),
    height=utils.height_percent(80)
)

left_frame.place(x=0, y=utils.height_percent(20))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_percent(80),
    height=utils.height_percent(80)
)

center_frame.place(x=utils.width_percent(20), y=utils.height_percent(20))

for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)

# Call the label from the cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x = 17, y = 40)

Cell.randomize_mines()


# Run the window
root.mainloop()
