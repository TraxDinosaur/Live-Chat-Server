# Live Chat Server

![Live Chat Server Logo](https://i.ibb.co/J3m4yjj/Picsart-24-03-30-22-01-13-742.png)

## Overview

The Live Chat Server is a real-time chat application built using Flask and SocketIO. It allows users to engage in live conversations, sending and receiving messages instantly.

## Features

- Real-time messaging: Users can send and receive messages instantly without page refresh.
- User authentication: Access to the chat requires a secret code, ensuring a secure environment.
- Dynamic user interface: The interface dynamically adjusts to accommodate various screen sizes and devices.

## Installation

To set up the Live Chat Server locally, follow these steps:

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/TraxDinosaur/Live-Chat-Server.git
   ```

2. Navigate to the project directory.
   ```bash
   cd live-chat-server
   ```

3. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables.
   ```bash
   export SECRET_KEY='your_secret_key'
   ```

5. Run the application.
   ```bash
   python server.py
   ```

6. Access the application in your web browser at `http://localhost:5000`.

#### How to Run in Replit 🌐

To experience Live-Chat-Server in Replit, simply click the button below:

[![Run in Replit](https://replit.com/badge/github/TraxDinosaur/Live-Chat-Server)](https://replit.com/@TraxDinosaur/Live-Chat-Server)

## Usage

1. Enter the secret code to authenticate and join the chat.
2. Enter your name to start chatting.
3. Type your message in the input field and hit "Send" or press Enter to send the message.
4. Enjoy real-time communication with other users!

## Technologies Used

- Python
- Flask
- SocketIO
- HTML5
- CSS3
- JavaScript

## Contributing

Contributions are welcome! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact [TraxDinosaur](https://traxdinosaur.github.io/).
