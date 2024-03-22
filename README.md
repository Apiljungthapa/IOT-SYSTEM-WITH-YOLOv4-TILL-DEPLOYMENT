# RFID Gate Security System with YOLOv4 Integration

This project implements an end-to-end IoT (Internet of Things) solution for a security gate system. The system combines RFID technology for access control with YOLOv4 (You Only Look Once) object detection for enhanced security. The Flask web application provides a user-friendly interface to interact with the system.

## Overview

The RFID gate security system with YOLOv4 integration consists of the following components:
- **RFID Reader**: Reads RFID tags to grant or deny access through the gate.
- **YOLOv4 Object Detection**: Detects and identifies objects in the vicinity of the gate using a YOLOv4 model trained on custom images.
- **Flask Web Application**: Provides a web interface for system configuration, monitoring, and access control.

## Features

- **RFID Access Control**: Grant or deny access based on RFID tag authentication.
- **Object Detection**: Identify objects in the vicinity of the gate, such as unauthorized persons or objects.
- **User Management**: Admin panel to manage user access rights and permissions.
- **Event Logging**: Log events such as gate openings, object detections, and user interactions.
- **Real-time Monitoring**: Monitor gate status and object detection in real-time through the web interface.

## Setup and Deployment

1. **Clone the Repository**: Clone this repository to your local machine.https://github.com/Apiljungthapa/IOT-SYSTEM-WITH-YOLOv4-TILL-DEPLOYMENT

2. **Install Dependencies**: Install the required Python dependencies using `:pip install yolo`

3. **Configuration**: Update the configuration settings in `config.py` file, including RFID reader settings, YOLOv4 model paths, Flask app configuration, etc.

4. **Model Configuration**: Ensure that the YOLOv4 model weights and configuration files are available in the specified paths.

5. **Run the Flask Application**: Start the Flask web application using the following command:


6. **Access the Web Interface**: Open a web browser and navigate to the address provided in the terminal (usually `http://localhost:5000`) to access the web interface.

7. **Deployment**: Deploy the Flask application to a production environment using a web server such as Nginx or Apache. Ensure proper security measures are implemented for production deployment.

## Repository Structure

- `app.py`: Main Flask application file.
- `config.py`: Configuration settings for the application.
- `models/`: Directory containing YOLOv4 model weights and configuration files.
- `static/`: Static files including CSS, JavaScript, and images for the web interface.
- `templates/`: HTML templates for the Flask application.
- `utils/`: Utility functions and modules for RFID, YOLOv4, and web application functionalities.

## Contributing

Contributions to improve system performance, add new features, enhance security, or fix bugs are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://github.com/Apiljungthapa/IOT-SYSTEM-WITH-YOLOv4-TILL-DEPLOYMENT/blob/master/LICENSE).


