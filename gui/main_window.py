from PyQt6.QtWidgets import QMainWindow, QTabWidget
from .devices_tab import DevicesTab
from .setup_tab import SetupTab
from .measurement_tab import MeasurementTab
from .results_tab import ResultsTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laser Beam M² Measurement")

        tabs = QTabWidget()
        tabs.addTab(DevicesTab(), "Devices")
        #tabs.addTab(SetupTab(), "Setup")
        tabs.addTab(MeasurementTab(), "Measurement")
        tabs.addTab(ResultsTab(), "Results")

        self.setCentralWidget(tabs)
