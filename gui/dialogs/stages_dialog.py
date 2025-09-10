from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QDialogButtonBox, QPushButton,
    QTableWidget, QTableWidgetItem, QCheckBox, QComboBox, QWidget, QHBoxLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHeaderView


class StagesDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Stages")

        self.devices = self.fake_discovery()
        self.layout = QVBoxLayout(self)

        # Table
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["", "Name", "S/N", "Axis"])
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(False)
        self.table.setStyleSheet(
            "QHeaderView::section { background-color: lightgray; padding: 4px; }"
        )
        self.layout.addWidget(self.table)

        # Align headers left + stretch last column
        header = self.table.horizontalHeader()
        for i in range(self.table.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Fixed)
            item = self.table.horizontalHeaderItem(i)
            if item:
                item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

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
        self.setMinimumWidth(650)
        self.setMinimumHeight(350)

    def fake_discovery(self):
        return [
            {"model": "Thorlabs Kinesis XYZ", "serial": "ST001"},
            {"model": "Newport Linear Stage", "serial": "ST002"}
        ]

    def refresh_devices(self):
        self.table.setRowCount(0)
        self.checkboxes = []
        self.comboboxes = []

        for dev in self.devices:
            row = self.table.rowCount()
            self.table.insertRow(row)

            # Checkbox
            cb = QCheckBox()
            self.checkboxes.append(cb)
            cell_widget = QWidget()
            layout = QHBoxLayout(cell_widget)
            layout.addWidget(cb, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            self.table.setCellWidget(row, 0, cell_widget)

            # Name + serial
            self.table.setItem(row, 1, QTableWidgetItem(dev["model"]))
            self.table.setItem(row, 2, QTableWidgetItem(dev["serial"]))

            # Axis dropdown (fixed width, disabled by default)
            combo = QComboBox()
            combo.addItems(["X", "Y", "Z"])
            combo.setEnabled(False)
            combo.setFixedWidth(80)
            self.table.setCellWidget(row, 3, combo)
            self.comboboxes.append(combo)

            # Enable dropdown only if checkbox is checked
            cb.toggled.connect(combo.setEnabled)
            cb.toggled.connect(self.update_axis_options)

        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 150)

        self.adjustSize()

    def update_axis_options(self):
        used_axes = set()
        for cb, combo in zip(self.checkboxes, self.comboboxes):
            if cb.isChecked():
                used_axes.add(combo.currentText())

        for cb, combo in zip(self.checkboxes, self.comboboxes):
            if not cb.isChecked():
                available = [axis for axis in ["X", "Y", "Z"] if axis not in used_axes]
                current = combo.currentText()
                combo.blockSignals(True)
                combo.clear()
                combo.addItems(available)
                if current in available:
                    combo.setCurrentText(current)
                combo.blockSignals(False)

    def get_selection(self):
        selected = []
        for i, cb in enumerate(self.checkboxes):
            if cb.isChecked():
                selected.append({
                    "model": self.devices[i]["model"],
                    "serial": self.devices[i]["serial"],
                    "axis": self.comboboxes[i].currentText()
                })
        return selected
