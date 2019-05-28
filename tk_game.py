# adapted from notes: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/tkinter.md

import tkinter
import tkinter.messagebox # h/t: https://stackoverflow.com/a/38181986/670433

from game import random_choice, determine_winner

window = tkinter.Tk()

my_message = tkinter.Message(text="Hi. Welcome to my Rock-Paper-Scissors game!", width=1000)

my_select_label = tkinter.Label(text="Please choose an option from the dropdown:")
my_select = tkinter.Listbox()
my_select.insert(1, "rock")
my_select.insert(2, "paper")
my_select.insert(3, "scissors")

def handle_button_click():
    user_choice = my_select.get(my_select.curselection())

    computer_choice = random_choice()

    message = "-------------------"
    message += f"\nYou chose: {user_choice}"
    message += f"\nThe computer chose: {computer_choice}"

    #winning_choice = determine_winner(user_choice, computer_choice)
    #if winning_choice:
    #    if winning_choice == user_choice:
    #        print("Congratulations, you won!")
    #    elif winning_choice == computer_choice:
    #        print("Oh, the computer won. It's ok.")
    #else:
    #    print("Oh, it's a tie.")

    message += "\n-------------------"
    heading = "Congratulations"
    message += "\nYou won!"

    message += "\n-------------------"
    message += "\nThanks for playing. Please play again!"

    tkinter.messagebox.showinfo(heading, message)


my_button = tkinter.Button(text="Submit", command=handle_button_click)

my_select.pack()
my_button.pack()
window.mainloop()
