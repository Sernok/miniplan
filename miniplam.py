from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCalendarWidget, QTimeEdit, QListWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import QDateTime
import sys
class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Минипланировщик")
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        # Calendar widget
        self.calendarWidget = QCalendarWidget()
        layout.addWidget(self.calendarWidget)
        # Time edit widget
        self.timeEdit = QTimeEdit()
        layout.addWidget(self.timeEdit)
        # Event title input
        self.eventTitle = QLineEdit()
        self.eventTitle.setPlaceholderText("Введите название события")
        layout.addWidget(self.eventTitle)
        # Add event button
        self.addButton = QPushButton("Добавить событие")
        self.addButton.clicked.connect(self.add_event)
        layout.addWidget(self.addButton)
        # Event list widget
        self.eventList = QListWidget()
        layout.addWidget(self.eventList)
    def add_event(self):
        # Get selected date, time and event title
        selected_date = self.calendarWidget.selectedDate()
        selected_time = self.timeEdit.time()
        event_title = self.eventTitle.text()
        # Combine date and time into a single QDateTime object
        event_datetime = QDateTime(selected_date, selected_time)
        # Add formatted event to the list
        event_text = f"{event_datetime.toString('yyyy-MM-dd hh:mm:ss')} - {event_title}"
        self.eventList.addItem(event_text)
        self.eventTitle.clear()
        # Sort events by date and time
        self.sort_events()
    def sort_events(self):
        # Extract event items, sort them, and re-add to the eventList
        events = []
        for index in range(self.eventList.count()):
            events.append(self.eventList.item(index).text())
        events.sort()  # Sort events based on datetime
        self.eventList.clear()
        self.eventList.addItems(events)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimplePlanner()
    window.show()
    sys.exit(app.exec_())