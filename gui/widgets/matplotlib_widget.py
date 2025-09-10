from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6.QtWidgets import QWidget, QVBoxLayout


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


        self.figure = Figure(figsize=(5, 3))
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def clear(self):
        """Clear the plot."""
        self.figure.clear()
        self.canvas.draw()

    def plot_example(self):
        """Draw a simple placeholder plot."""
        self.clear()
        ax = self.figure.add_subplot(111)
        ax.plot([0, 1, 2], [0, 1, 0], label="Example")
        ax.legend()
        self.canvas.draw()
