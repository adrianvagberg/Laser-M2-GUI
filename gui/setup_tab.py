from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout, QGroupBox, QRadioButton


class SetupTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.wl_input = QLineEdit()
        self.wl_input.setPlaceholderText("Wavelength (nm)")

        self.dof_input = QLineEdit()
        self.dof_input.setPlaceholderText("Depth of Field (mm)")

        self.jog_forward = QPushButton("Jog Z Forward")
        self.jog_backward = QPushButton("Jog Z Backward")
        self.set_waist_button = QPushButton("Set Waist Position")

        self.mode_group = QGroupBox("Measurement Mode")
        mode_layout = QVBoxLayout()
        self.m2_mode = QRadioButton("M² Measurement")
        self.div_mode = QRadioButton("Divergence Only")
        self.m2_mode.setChecked(True)
        mode_layout.addWidget(self.m2_mode)
        mode_layout.addWidget(self.div_mode)
        self.mode_group.setLayout(mode_layout)

        layout.addWidget(QLabel("Experiment Setup"))
        layout.addWidget(self.wl_input)
        layout.addWidget(self.dof_input)

        jog_layout = QHBoxLayout()
        jog_layout.addWidget(self.jog_backward)
        jog_layout.addWidget(self.jog_forward)
        layout.addLayout(jog_layout)

        layout.addWidget(self.set_waist_button)
        layout.addWidget(self.mode_group)

        self.setLayout(layout)
