import pyshorteners
from tkinter import *

# Create the main window
win = Tk()
win.geometry("400x200")  # Correct format for geometry specification
win.configure(bg="green")
win.title("URL Shortener")

# Function to shorten the URL
def shorten_url():
    url = url_entry.get()
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    short_url_label.config(text=short_url)

# Label for entering user URL
Label(win, text="Enter Your URL Link", font="impact 17 bold", bg="black", fg="white").pack(fill="x")

# Entry widget for URL input
url_entry = Entry(win, font="impact 16 bold", bd=3, width=40, bg="pink")
url_entry.pack(pady=5)

# Button to shorten the URL
shorten_button = Button(win, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)

# Label to display the shortened URL
short_url_label = Label(win, text="", bg="green")
short_url_label.pack(pady=5)

# Run the main event loop
win.mainloop()
