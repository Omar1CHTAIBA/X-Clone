# Chat App

This is a chat application that allows users to register, log in, and send messages. It features a backend server built with Falcon and Waitress, and a frontend built with PyQt6 for the user interface. Users can send and receive messages in real-time, with messages stored and fetched from the backend.

---

## Features

- **User Registration**: Users can sign in with a unique username and user ID.
- **Chat Functionality**: Users can send and receive messages in real-time.
- **Stylish UI**: The app has a modern design with smooth animations and color schemes.
- **Message Persistence**: Messages are stored and fetched from the backend.

---

## Technologies Used

- **Frontend**:
  - PyQt6 (for the UI)
- **Backend**:
  - Falcon (for building the API)
  - SQLite (for storing user data)
  - Waitress (for serving the API)
- **Design**:
  - Custom CSS styles for a modern, sleek design.

---

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- PyQt6
- Requests
- SQLite (already included with Python)
- Falcon
- Waitress

### Install Dependencies

You can install the required dependencies using `pip`:

```bash
pip install PyQt6 requests falcon waitress
```

## Usage
#### Sign Up: Upon launching the frontend app, you will be asked to enter a username and user ID. If the user ID already exists in the database, you'll be prompted to choose a different one.
#### Send Messages: After logging in, you can type a message in the text box and click the "Tweet" button to send the message to the chat window.
#### Receive Messages: The chat window updates every 2 seconds with new messages from other users.


## DEMO

![Image](https://github.com/user-attachments/assets/1f9c718d-df5c-4361-a13d-2253a931d014)

![Image](https://github.com/user-attachments/assets/c6332432-11e8-45b6-a540-b180a886a04f)

