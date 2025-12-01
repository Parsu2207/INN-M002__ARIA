# ui/main_window.py
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QTableView, QMessageBox
)
from .alerts_table_model import AlertsTableModel
from .api_client import ApiClient


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.api = ApiClient()# ui/main_window.py
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

        # ---------- MAIN CONTAINER ----------
        central = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(20)
        central.setLayout(main_layout)
        self.setCentralWidget(central)

        # ---------- BACKGROUND COLOR ----------
        central.setStyleSheet("background-color: #e0f2f7;")  # soft blue-grey background

        # ---------- TITLE LABEL ----------
        title = QLabel("SOC Alert Monitoring Dashboard")
        title.setFont(QFont("courier", 22, QFont.Bold))
        title.setStyleSheet("color: #1F2937;")  # dark grey
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # ---------- TOP CONTROL BAR ----------
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
                background-color: #0057B8;  /* professional deep blue */
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

        # ---------- SEPARATOR ----------
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: #B0B0B0;")  # lighter separator for contrast
        main_layout.addWidget(separator)

        # ---------- TABLE VIEW ----------
        self.table = QTableView()
        self.model = AlertsTableModel()
        self.table.setModel(self.model)

        # Alternating row colors
        self.table.setAlternatingRowColors(True)
        pal = self.table.palette()
        pal.setColor(QPalette.Base, QColor("#FFFFFF"))  # table background
        pal.setColor(QPalette.AlternateBase, QColor("#F1F4F8"))  # subtle alternate
        self.table.setPalette(pal)

        # Header styling
        self.table.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #0F172A;  /* very dark blue header */
                color: white;
                padding: 6px;
                font-size: 12px;
                font-family:'Segoe UI';
                border: 1px solid #C0C0C0;
            }
        """)

        # Table styling
        self.table.setStyleSheet("""
            QTableView {
                font-size: 12px;
                font-family:'Segoe UI';
                gridline-color: #D0D0D0;
                selection-background-color: #CCE4FF;  /* soft selection */
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

        # Load initial alerts
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
