from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QDialogButtonBox, QPushButton,
    QTableWidget, QTableWidgetItem, QRadioButton, QWidget, QHBoxLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHeaderView


class PowerMeterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Power Meter")

        self.devices = self.fake_discovery()
        self.layout = QVBoxLayout(self)

        # Table
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["", "Name", "S/N"])
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(False)
        self.table.setStyleSheet(
            "QHeaderView::section { background-color: lightgray; padding: 4px; }"
        )
        self.layout.addWidget(self.table)

        # Align headers left
        header = self.table.horizontalHeader()
        for i in range(self.table.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Fixed)
            item = self.table.horizontalHeaderItem(i)
            if item:
                item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        # Stretch last column
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

        # Buttons
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh_devices)
        self.layout.addWidget(self.refresh_button)

        self.button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

        self.refresh_devices()

        # Minimum dialog size
        self.setMinimumWidth(500)
        self.setMinimumHeight(300)

    def fake_discovery(self):
        return [
            {"model": "Thorlabs PM100D", "serial": "PM001"},
            {"model": "Newport 2936-R", "serial": "PM002"}
        ]

    def refresh_devices(self):
        self.table.setRowCount(0)
        self.radiobuttons = []

        for dev in self.devices:
            row = self.table.rowCount()
            self.table.insertRow(row)

            # Radio button
            rb = QRadioButton()
            self.radiobuttons.append(rb)
            cell_widget = QWidget()
            layout = QHBoxLayout(cell_widget)
            layout.addWidget(rb, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            self.table.setCellWidget(row, 0, cell_widget)

            # Name + serial
            self.table.setItem(row, 1, QTableWidgetItem(dev["model"]))
            self.table.setItem(row, 2, QTableWidgetItem(dev["serial"]))

            rb.toggled.connect(self.handle_radio_toggle)

        self.table.setColumnWidth(0, 50)   # radio button
        self.table.setColumnWidth(1, 200)  # name

        self.adjustSize()

    def handle_radio_toggle(self):
        checked = [rb for rb in self.radiobuttons if rb.isChecked()]
        if len(checked) > 1:
            for rb in self.radiobuttons:
                if rb is not checked[0]:
                    rb.setChecked(False)

    def get_selection(self):
        for i, rb in enumerate(self.radiobuttons):
            if rb.isChecked():
                return {
                    "model": self.devices[i]["model"],
                    "serial": self.devices[i]["serial"]
                }
        return None
