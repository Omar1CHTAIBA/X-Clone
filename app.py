import sys
import requests
import sqlite3
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit, QPushButton, QLineEdit, QLabel, \
    QStackedWidget

db = sqlite3.connect('app.db')

cr = db.cursor()

cr.execute(
    "CREATE TABLE IF NOT EXISTS users(username TEXT, user_id TEXT)"
)

data = []

# Add these color constants at the top
COLORS = {
    'primary': '#1DA1F2',
    'background': '#15202B',
    'card_bg': '#192734',
    'text': '#FFFFFF',
    'secondary_text': '#8899A6',
    'border': '#38444D',
    'hover': '#162D40',
}


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.start_polling()
        self.send_button.clicked.connect(self.send_message)

    def initUI(self):
        self.setWindowTitle('X')
        self.setFixedSize(800, 800)  # Larger, more modern size

        # Set window background
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {COLORS['background']};
                color: {COLORS['text']};
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            }}
        """)

        # Main layout with margins
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(15)
        self.setLayout(self.layout)

        # Chat display area
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet(f"""
            QTextEdit {{
                background-color: {COLORS['card_bg']};
                color: {COLORS['text']};
                font-size: 15px;
                padding: 15px;
                border: 1px solid {COLORS['border']};
                border-radius: 15px;
                line-height: 1.5;
            }}
            QScrollBar:vertical {{
                background-color: {COLORS['card_bg']};
                width: 12px;
                margin: 0px;
            }}
            QScrollBar::handle:vertical {{
                background-color: {COLORS['border']};
                border-radius: 6px;
                min-height: 30px;
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
        """)
        self.layout.addWidget(self.chat_display)

        # Message input area
        self.message_input_layout = QHBoxLayout()
        self.message_input_layout.setSpacing(10)

        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("What's happening?")
        self.message_input.setStyleSheet(f"""
            QLineEdit {{
                background-color: {COLORS['card_bg']};
                color: {COLORS['text']};
                font-size: 15px;
                padding: 12px 20px;
                border: 2px solid {COLORS['border']};
                border-radius: 25px;
                min-height: 25px;
            }}
            QLineEdit:focus {{
                border: 2px solid {COLORS['primary']};
            }}
        """)
        self.message_input_layout.addWidget(self.message_input)

        self.send_button = QPushButton('Tweet')
        self.send_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.send_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {COLORS['primary']};
                color: {COLORS['text']};
                font-size: 15px;
                font-weight: bold;
                padding: 12px 25px;
                border: none;
                border-radius: 25px;
                min-width: 100px;
            }}
            QPushButton:hover {{
                background-color: #1991DA;
            }}
            QPushButton:pressed {{
                background-color: #0F7BBF;
            }}
        """)
        self.message_input_layout.addWidget(self.send_button)
        self.layout.addLayout(self.message_input_layout)

    def send_message(self):
        if not self.message_input.text().strip():
            return

        message = data[0] + " (With ID: " + data[1] + ") " + ": " + self.message_input.text()
        self.message_input.clear()
        try:
            requests.post('http://ip_adress:8000/messages', json={'message': message}, timeout=5)
            self.update_chat()
        except requests.exceptions.RequestException:
            self.chat_display.append("Error: Couldn't send message. Please try again.")

    def update_chat(self):
        response = requests.get('http://ip_adress:8000/messages')
        messages = response.json()
        self.chat_display.clear()
        for message in messages:
            self.chat_display.append(message['message'])

    def start_polling(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_chat)
        self.timer.start(2000)  # Poll every 2 seconds


class UserName(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initSettings()
        self.initUI()
        self.admit.clicked.connect(self.admit_logic)

    def initSettings(self):

        self.setWindowTitle('X (Login Page)')
        self.setFixedSize(800, 800)

    def initUI(self):
        self.setFixedSize(800, 800)
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {COLORS['background']};
                color: {COLORS['text']};
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            }}
            QLabel {{
                font-size: 15px;
                color: {COLORS['secondary_text']};
            }}
            QLineEdit {{
                background-color: {COLORS['card_bg']};
                color: {COLORS['text']};
                font-size: 15px;
                padding: 12px 20px;
                border: 2px solid {COLORS['border']};
                border-radius: 25px;
                min-height: 25px;
            }}
            QLineEdit:focus {{
                border: 2px solid {COLORS['primary']};
            }}
        """)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(40, 40, 40, 40)
        self.layout.setSpacing(15)

        # Title with X logo
        self.title = QLabel('Welcome to X')
        self.title.setStyleSheet("""
            font-size: 42px;
            font-weight: bold;
            color: #FFFFFF;
            margin: 40px 0px;
            letter-spacing: 1px;
        """)

        # Input fields with labels
        self.username_label = QLabel('USERNAME')
        self.username_label.setStyleSheet("""
            font-size: 13px;
            font-weight: bold;
            letter-spacing: 1.5px;
            margin-left: 15px;
            margin-bottom: 5px;
        """)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Enter your username")
        self.username.setMinimumHeight(50)  # Taller input field

        self.user_id_label = QLabel('USER ID')
        self.user_id_label.setStyleSheet("""
            font-size: 13px;
            font-weight: bold;
            letter-spacing: 1.5px;
            margin-left: 15px;
            margin-bottom: 5px;
            margin-top: 15px;
        """)

        self.user_id = QLineEdit()
        self.user_id.setPlaceholderText("Enter your user ID")
        self.user_id.setEchoMode(QLineEdit.EchoMode.Password)
        self.user_id.setMinimumHeight(50)  # Taller input field

        # Login button
        self.admit = QPushButton("Sign In")
        self.admit.setCursor(Qt.CursorShape.PointingHandCursor)
        self.admit.setStyleSheet(f"""
            QPushButton {{
                background-color: {COLORS['primary']};
                color: {COLORS['text']};
                font-size: 16px;
                font-weight: bold;
                padding: 15px 0px;
                border: none;
                border-radius: 25px;
                min-width: 200px;
                margin-top: 40px;
                letter-spacing: 0.5px;
            }}
            QPushButton:hover {{
                background-color: #1991DA;
                transform: scale(1.02);
                transition: all 0.2s ease;
            }}
            QPushButton:pressed {{
                background-color: #0F7BBF;
                transform: scale(0.98);
            }}
        """)

        # Add widgets to layout
        self.layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username)
        self.layout.addWidget(self.user_id_label)
        self.layout.addWidget(self.user_id)
        self.layout.addWidget(self.admit, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addStretch()

        self.setLayout(self.layout)

    def admit_logic(self):
        username = self.username.text()
        userid = self.user_id.text()

        # Debug prints
        print("Checking for userid:", userid)
        cr.execute("SELECT user_id FROM users")
        all_users = [row[0] for row in cr.fetchall()]
        print("All existing user IDs:", all_users)
        print("Is userid in all_users?", userid in all_users)

        condition = True

        if username and userid:
            if userid in all_users:
                print("Found duplicate user ID!")
                self.user_id.clear()
                self.user_id.setPlaceholderText('This user_id already exists')
                condition = False

            if condition:
                print("Adding new user to database")
                data.append(username)
                data.append(userid)
                cr.execute("INSERT INTO users(username, user_id) VALUES (?, ?)", (username, userid))
                db.commit()
                self.stacked_widget.setCurrentIndex(1)
        elif username:
            self.user_id.setPlaceholderText('You did not fill the USER-ID blank')
        elif userid:
            self.username.setPlaceholderText('You did not fill the USERNAME blank')
        else:
            self.username.setPlaceholderText('You did not fill the USERNAME blank')
            self.user_id.setPlaceholderText('You did not fill the USER-ID blank')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()
    loging_window = UserName(stacked_widget)
    main_window = ChatWindow()

    stacked_widget.addWidget(loging_window)
    stacked_widget.addWidget(main_window)

    stacked_widget.setCurrentIndex(0)

    stacked_widget.show()

    sys.exit(app.exec())