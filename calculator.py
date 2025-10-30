import tkinter as tk
import math

def calculator():
    def calculate():
        operator = operator_var.get()
        try:
            if operator in ['+', '-', '*', '/', '%', '**']:
                num1 = float(entry_num1.get())
                num2 = float(entry_num2.get())
                
                if operator == "+":
                    result = num1 + num2
                elif operator == "-":
                    result = num1 - num2
                elif operator == "*":
                    result = num1 * num2
                elif operator == "/":
                    if num2 == 0:
                        result_label.config(text="Error: Division by zero is not allowed.")
                        return
                    result = num1 / num2
                elif operator == "%":
                    result = num1 % num2
                elif operator == "**":
                    result = num1 ** num2
                
                result_label.config(text=f"Result: {result}")
                history.append(f"{num1} {operator} {num2} = {result}")
            
            elif operator == "sqrt":
                num = float(entry_num1.get())
                if num < 0:
                    result_label.config(text="Error: Cannot take square root of negative numbers.")
                else:
                    result = math.sqrt(num)
                    result_label.config(text=f"Result: {result}")
                    history.append(f"sqrt({num}) = {result}")
            
            # Update history
            history_text.set("\n".join(history))
        
        except ValueError:
            result_label.config(text="Invalid input. Please enter numeric values.")

    def clear():
        entry_num1.delete(0, tk.END)
        entry_num2.delete(0, tk.END)
        result_label.config(text="Result:")
        history_text.set("")

    def exit_calculator():
        window.quit()

    window = tk.Tk()
    window.title("Advanced Calculator")

    history = []  # Store history of calculations
    
    # Input fields and labels
    operator_var = tk.StringVar()
    
    tk.Label(window, text="Enter the first value:").grid(row=0, column=0)
    entry_num1 = tk.Entry(window)
    entry_num1.grid(row=0, column=1)
    
    tk.Label(window, text="Enter the second value:").grid(row=1, column=0)
    entry_num2 = tk.Entry(window)
    entry_num2.grid(row=1, column=1)
    
    tk.Label(window, text="Enter operator (+, -, *, /, %, **, sqrt):").grid(row=2, column=0)
    operator_entry = tk.Entry(window, textvariable=operator_var)
    operator_entry.grid(row=2, column=1)
    
    # Buttons for operations
    calculate_button = tk.Button(window, text="Calculate", command=calculate)
    calculate_button.grid(row=3, column=0, columnspan=2)
    
    clear_button = tk.Button(window, text="Clear", command=clear)
    clear_button.grid(row=4, column=0, columnspan=2)
    
    exit_button = tk.Button(window, text="Exit", command=exit_calculator)
    exit_button.grid(row=5, column=0, columnspan=2)
    
    # Result label
    result_label = tk.Label(window, text="Result:")
    result_label.grid(row=6, column=0, columnspan=2)
    
    # History of calculations
    history_text = tk.StringVar()
    history_label = tk.Label(window, text="History of calculations:")
    history_label.grid(row=7, column=0, columnspan=2)
    
    history_display = tk.Label(window, textvariable=history_text, justify="left")
    history_display.grid(row=8, column=0, columnspan=2)
    
    window.mainloop()

# Run the calculator
calculator()
