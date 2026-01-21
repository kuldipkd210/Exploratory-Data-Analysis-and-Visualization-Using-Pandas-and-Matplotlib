import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, OptionMenu, StringVar

# Load CSV
df = pd.read_csv("data.csv")

# Detect numeric columns dynamically
numeric_cols = df.select_dtypes(include='number').columns.tolist()

# Calculate averages dynamically
averages = df[numeric_cols].mean().round(2)

# Function to show averages in main window
def show_averages():
    avg_text = "Averages of Numeric Columns:\n"
    for col in numeric_cols:
        avg_text += f"{col}: {averages[col]}\n"
    
    avg_label.config(text=avg_text)
    

# Function to plot Bar Chart
def plot_bar_chart():
    plt.figure(figsize=(8,6))
    plt.bar(numeric_cols, averages, color=plt.cm.tab20.colors[:len(numeric_cols)])
    plt.title("Average of Numeric Columns")
    plt.xlabel("Columns")
    plt.ylabel("Average Value")
    plt.show()

# Function to plot Scatter Plot (dynamic)
def plot_scatter():
    x_col = x_var.get()
    y_col = y_var.get()
    if x_col == y_col:
        avg_text = "Please select different columns for X and Y"
        avg_label.config(text=avg_text)
        return
    plt.figure(figsize=(8,6))
    plt.scatter(df[x_col], df[y_col], color='orange')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"Scatter Plot: {x_col} vs {y_col}")
    plt.grid(True)
    plt.show()

# Function to plot Heatmap
def plot_heatmap():
    corr = df[numeric_cols].corr()
    plt.figure(figsize=(7,6))
    plt.imshow(corr, cmap='coolwarm', interpolation='none')
    plt.colorbar(label='Correlation')
    plt.xticks(range(len(numeric_cols)), numeric_cols)
    plt.yticks(range(len(numeric_cols)), numeric_cols)
    plt.title("Correlation Heatmap")
    plt.show()

# Tkinter GUI
root = Tk()
root.title("Dynamic Data Visualization")

# Buttons
Button(root, text="Show Averages", command=show_averages, width=30, bg='lightyellow').pack(pady=5)
Button(root, text="Bar Chart (Averages)", command=plot_bar_chart, width=30, bg='lightblue').pack(pady=5)
Button(root, text="Heatmap (Correlation)", command=plot_heatmap, width=30, bg='salmon').pack(pady=5)

# Scatter plot column selectors
Label(root, text="Scatter Plot Columns:", font=("Arial", 12)).pack(pady=5)

x_var = StringVar(root)
x_var.set(numeric_cols[0])  # default X
y_var = StringVar(root)
y_var.set(numeric_cols[1] if len(numeric_cols) > 1 else numeric_cols[0])  # default Y

OptionMenu(root, x_var, *numeric_cols).pack(pady=2)
OptionMenu(root, y_var, *numeric_cols).pack(pady=2)

Button(root, text="Plot Scatter", command=plot_scatter, width=30, bg='lightgreen').pack(pady=5)

# Label to display averages
avg_label = Label(root, text="", font=("Arial", 12), justify="left")
avg_label.pack(pady=10)

root.geometry("400x500")
root.mainloop()
