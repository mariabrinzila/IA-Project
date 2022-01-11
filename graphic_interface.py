import tkinter as t
import generate_posts as gp


class GraphicInterface:
    def __init__(self):
        # Create window
        self.window = t.Tk()
        self.window.geometry("600x200")
        self.window.configure(background='black')

        # Get the keyword from user
        self.keyword_variable = t.StringVar(value='something')
        ask_user_keyword = t.Label(text="Keyword:", bg='black',
                                   fg='white', font='Arial 9 bold')
        keyword_entry = t.Entry(textvariable=self.keyword_variable, width=25,
                                bg='black', fg='white')

        # Get the number of tweets from user
        self.number_variable = t.IntVar(value=10)
        ask_user_number = t.Label(text="Number of tweets:",
                                  bg='black', fg='white',
                                  font='Arial 9 bold')
        number_entry = t.Entry(textvariable=self.number_variable, width=25,
                               bg='black', fg='white')

        # Submit input button
        okay = t.Button(self.window, text="All good", bg='sky blue',
                        fg='black', width=15, height=2,
                        font='Arial 9 bold',
                        command=self.button_action_function)

        # Close window button
        close_window_button = t.Button(self.window, text="Done searching",
                                       bg='sky blue', fg='black', width=15,
                                       height=2, font='Arial 9 bold',
                                       command=self.close_window)

        # Put entries, labels and buttons in a grid
        ask_user_keyword.grid(column=0, row=0, pady=(20, 10), padx=(10, 20))
        keyword_entry.grid(column=1, row=0, pady=(20, 10), padx=(20, 10))

        ask_user_number.grid(column=0, row=1, pady=(10, 10), padx=(10, 20))
        number_entry.grid(column=1, row=1, pady=(10, 15), padx=(20, 10))

        okay.grid(column=0, row=2, pady=(10, 0), padx=(10, 10))
        close_window_button.grid(column=1, row=2, pady=(10, 0), padx=(10, 10))

        # Display the window
        self.window.mainloop()

    def button_action_function(self):
        gp.submit_input(self.keyword_variable, self.number_variable)

    def close_window(self):
        self.window.destroy()
