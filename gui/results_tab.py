from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from .widgets.matplotlib_widget import MatplotlibWidget


class ResultsTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.results_label = QLabel("Results will appear here.")
        self.save_csv_button = QPushButton("Save CSV")
        self.export_plot_button = QPushButton("Export Plot")

        self.results_plot = MatplotlibWidget()

        layout.addWidget(self.results_label)
        layout.addWidget(self.save_csv_button)
        layout.addWidget(self.export_plot_button)
        layout.addWidget(QLabel("M² Plot:"))
        layout.addWidget(self.results_plot)

        self.setLayout(layout)
