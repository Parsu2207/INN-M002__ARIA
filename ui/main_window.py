
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QTableView, QMessageBox
)
from .alerts_table_model import AlertsTableModel
from .api_client import ApiClient


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.api = ApiClient()
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QTableView, QLabel, QFrame
)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt
from .alerts_table_model import AlertsTableModel
from .api_client import ApiClient


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.api = ApiClient()
        self.setWindowTitle("ARIA Desktop – Alert & Response Intelligence Agent")
        self.resize(1200, 650)

        central = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(20)
        central.setLayout(main_layout)
        self.setCentralWidget(central)

        central.setStyleSheet("background-color: #e0f2f7;")  

        title = QLabel("SOC Alert Monitoring Dashboard")
        title.setFont(QFont("courier", 22, QFont.Bold))
        title.setStyleSheet("color: #1F2937;") 
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        control_bar = QHBoxLayout()
        control_bar.setSpacing(15)

        label = QLabel("Priority Filter:")
        label.setFont(QFont("Segoe UI", 11))
        control_bar.addWidget(label)

        self.priority_filter = QComboBox()
        self.priority_filter.addItems(["ALL", "CRITICAL", "HIGH", "MEDIUM", "LOW"])
        self.priority_filter.setFixedWidth(160)
        self.priority_filter.setStyleSheet("""
            QComboBox {
                padding:5px;
                font-size:12px;
                font-family:'Segoe UI';
                border: 1px solid #C0C0C0;
                border-radius: 5px;
                background-color: white;
            }
        """)
        control_bar.addWidget(self.priority_filter)

        self.refresh_btn = QPushButton("Refresh Alerts")
        self.refresh_btn.setStyleSheet("""
            QPushButton {
                background-color: #0057B8;  
                color: white;
                font-weight: bold;
                padding: 6px 20px;
                border-radius: 5px;
                font-size: 12px;
                font-family: 'Segoe UI';
            }
            QPushButton:hover {
                background-color: #003F7F;
            }
        """)
        self.refresh_btn.clicked.connect(self.refresh_alerts)
        control_bar.addWidget(self.refresh_btn)

        control_bar.addStretch()
        main_layout.addLayout(control_bar)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: #B0B0B0;")  
        main_layout.addWidget(separator)

        self.table = QTableView()
        self.model = AlertsTableModel()
        self.table.setModel(self.model)

        self.table.setAlternatingRowColors(True)
        pal = self.table.palette()
        pal.setColor(QPalette.Base, QColor("#FFFFFF")) 
        pal.setColor(QPalette.AlternateBase, QColor("#F1F4F8")) 
        self.table.setPalette(pal)

        self.table.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #0F172A; 
                color: white;
                padding: 6px;
                font-size: 12px;
                font-family:'Segoe UI';
                border: 1px solid #C0C0C0;
            }
        """)

        self.table.setStyleSheet("""
            QTableView {
                font-size: 13px;
                font-family:'Segoe UI';
                gridline-color: #D0D0D0;
                selection-background-color: #CCE4FF;  
                border-radius: 5px;
            }
            QTableView::item:selected {
                color: black;
            }
        """)

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setSortingEnabled(True)

        main_layout.addWidget(self.table)

        self.refresh_alerts()

    def refresh_alerts(self):
        try:
            priority = self.priority_filter.currentText()
            if priority == "ALL":
                priority = None

            alerts = self.api.get_alerts(priority=priority)
            self.model.update_alerts(alerts)
        except Exception as e:
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Error", f"Failed to load alerts: {e}")

        self.setWindowTitle("ARIA Desktop – Alert & Response Intelligence Agent")
        self.resize(1100, 600)

        central = QWidget()
        layout = QVBoxLayout()
        controls = QHBoxLayout()

        self.priority_filter = QComboBox()
        self.priority_filter.addItems(["ALL", "CRITICAL", "HIGH", "MEDIUM", "LOW"])

        self.refresh_btn = QPushButton("Refresh Alerts")
        self.refresh_btn.clicked.connect(self.refresh_alerts)

        controls.addWidget(self.priority_filter)
        controls.addWidget(self.refresh_btn)

        self.table = QTableView()
        self.model = AlertsTableModel()
        self.table.setModel(self.model)

        layout.addLayout(controls)
        layout.addWidget(self.table)
        central.setLayout(layout)
        self.setCentralWidget(central)

        self.refresh_alerts()

    def refresh_alerts(self):
        try:
            priority = self.priority_filter.currentText()
            if priority == "ALL":
                priority = None
            alerts = self.api.get_alerts(priority=priority)
            self.model.update_alerts(alerts)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load alerts: {e}")
