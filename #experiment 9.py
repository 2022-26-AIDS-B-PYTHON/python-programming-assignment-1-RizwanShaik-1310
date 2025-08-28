#experiment 9

import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact, Dropdown

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [85, 70, 90, 60, 75],
    "Age": [20, 21, 19, 22, 20]
}
df = pd.DataFrame(data)

def visualize(chart_type):
    plt.figure(figsize=(6, 4))
    if chart_type == "Line Plot":
        plt.plot(df["Name"], df["Marks"], marker="o")
        plt.title("Line Plot of Marks")
    elif chart_type == "Bar Chart":
        plt.bar(df["Name"], df["Marks"])
        plt.title("Bar Chart of Marks")
    elif chart_type == "Pie Chart":
        plt.pie(df["Marks"], labels=df["Name"], autopct="%1.1f%%")
        plt.title("Pie Chart of Marks")
    plt.show()

interact(
    visualize,
    chart_type=Dropdown(
        options=["Line Plot", "Bar Chart", "Pie Chart"],
        value="Line Plot",
        description="Choose Chart:"
    )
)