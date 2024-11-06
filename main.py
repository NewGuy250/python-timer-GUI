import tkinter as tk

def start_timer(window, time_display, minutes, seconds):
    def countdown():
        nonlocal minutes, seconds
        # Update the label with the current time
        time_display.set(f"{minutes:02d}:{seconds:02d}")
        
        # Stop if time is up
        if minutes == 0 and seconds == 0:
            time_display.set("Time's up!")
        else:
            # Decrement the seconds and update the time
            if seconds > 0:
                seconds -= 1
            else:
                if minutes > 0:
                    minutes -= 1
                    seconds = 59
            # Call countdown function again after 1 second
            window.after(1000, countdown)

    countdown()  # Start the countdown

def main():
    # Create the main window
    window = tk.Tk()
    window.title("Timer Program")

    # Greeting label
    greeting_label = tk.Label(window, text="Welcome to my timer program!", font=("Helvetica", 14))
    greeting_label.pack(pady=10)

    # Entry for minutes
    minutes_label = tk.Label(window, text="Enter the amount of minutes:", font=("Helvetica", 12))
    minutes_label.pack()
    minutes_entry = tk.Entry(window, font=("Helvetica", 12))
    minutes_entry.pack(pady=5)

    # Entry for seconds
    seconds_label = tk.Label(window, text="Enter the amount of seconds:", font=("Helvetica", 12))
    seconds_label.pack()
    seconds_entry = tk.Entry(window, font=("Helvetica", 12))
    seconds_entry.pack(pady=5)

    # Timer display
    time_display = tk.StringVar()
    time_display.set("00:00")
    timer_label = tk.Label(window, textvariable=time_display, font=("Helvetica", 30))
    timer_label.pack(pady=20)

    # Start button
    def start_button_click():
        try:
            # Get the input values
            minutes = int(minutes_entry.get())
            seconds = int(seconds_entry.get())
            
            # Ensure inputs are valid
            if minutes < 0 or seconds < 0:
                raise ValueError("Please enter non-negative numbers.")
            
            # Start the timer
            start_timer(window, time_display, minutes, seconds)
        except ValueError as e:
            time_display.set(str(e))  # Show error message in the window

    start_button = tk.Button(window, text="Start Timer", font=("Helvetica", 12), command=start_button_click)
    start_button.pack(pady=10)

    # Run the main loop to display the window
    window.mainloop()

if __name__ == "__main__":
    main()
