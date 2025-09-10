from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QCheckBox,
    QTextEdit, QComboBox, QGroupBox, QFormLayout
)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MeasurementTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        main_layout = QHBoxLayout(self)

        # --- Left column: setup controls ---
        setup_box = QGroupBox("Setup")
        setup_layout = QFormLayout()

        self.waist_input = QLineEdit()
        self.waist_input.setPlaceholderText("mm")
        setup_layout.addRow("Beam waist position:", self.waist_input)

        self.axis_dropdown = QComboBox()
        self.axis_dropdown.addItems(["X", "Y"])  # populate dynamically later
        setup_layout.addRow("Axis:", self.axis_dropdown)

        self.step_input = QLineEdit("0.1")
        setup_layout.addRow("Step size [mm]:", self.step_input)

        self.range_input = QLineEdit("10")
        setup_layout.addRow("Range [mm]:", self.range_input)

        self.avg_input = QLineEdit("10")
        setup_layout.addRow("Power meter averaging:", self.avg_input)

        self.m2_checkbox = QCheckBox("Full M² measurement")
        self.m2_checkbox.setChecked(True)
        setup_layout.addRow(self.m2_checkbox)

        setup_box.setLayout(setup_layout)

        # --- Right column: measurement workflow ---
        workflow_layout = QVBoxLayout()

        self.start_button = QPushButton("Start Measurement")
        self.abort_button = QPushButton("Abort")
        workflow_layout.addWidget(self.start_button)
        workflow_layout.addWidget(self.abort_button)

        # Live plot
        self.figure = Figure(figsize=(5, 4))
        self.canvas = FigureCanvas(self.figure)
        workflow_layout.addWidget(self.canvas)

        # Log output
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        workflow_layout.addWidget(QLabel("Log:"))
        workflow_layout.addWidget(self.log_output)

        # --- Combine ---
        main_layout.addWidget(setup_box, stretch=1)
        main_layout.addLayout(workflow_layout, stretch=2)
