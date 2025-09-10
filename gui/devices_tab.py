from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from .dialogs.power_meter_dialog import PowerMeterDialog
from .dialogs.stages_dialog import StagesDialog


class DevicesTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.connect_pm_button = QPushButton("Connect Power Meter")
        self.connect_stages_button = QPushButton("Connect Stages")
        self.status_label = QLabel("Status: Not connected")

        layout.addWidget(self.connect_pm_button)
        layout.addWidget(self.connect_stages_button)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        # Connect signals
        self.connect_pm_button.clicked.connect(self.show_pm_dialog)
        self.connect_stages_button.clicked.connect(self.show_stages_dialog)

    def show_pm_dialog(self):
        dialog = PowerMeterDialog(self)
        if dialog.exec():
            selected = dialog.get_selection()
            if selected:
                self.status_label.setText(f"Power Meter connected: {selected['model']} (S/N {selected['serial']})")

    def show_stages_dialog(self):
        dialog = StagesDialog(self)
        if dialog.exec():
            selected = dialog.get_selection()
            if selected:
                # Display which stage is assigned to which axis
                axes_info = ", ".join(f"{s['model']}→{s['axis']}" for s in selected)
                self.status_label.setText(f"Stages connected: {axes_info}")
