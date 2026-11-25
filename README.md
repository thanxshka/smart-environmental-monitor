
# Smart Environmental Monitor

### IoT Capstone Project — Task 04

A software-based IoT environmental monitoring system that simulates temperature and humidity sensors, publishes readings through MQTT, and displays live data on a web dashboard.

## Features

- Simulated temperature and humidity sensor readings.
- MQTT communication using the Paho MQTT client.
- Live browser-based monitoring dashboard.
- Automatic MQTT reconnection.
- QoS 1 message publishing with delivery checks.
- Configurable sampling interval.
- Environment-variable-based configuration.
- Simulated battery monitoring.

## System Architecture

The system has three main components:

1. **Device:** Python program simulating environmental sensors.
2. **Transport:** MQTT broker transfers sensor readings.
3. **Dashboard:** HTML, CSS and JavaScript display incoming readings.

See `SYSTEM_ARCHITECTURE.md` for the system diagram.

## Project Structure

```text
smart-environmental-monitor/
├── capstone_device.py
├── requirements.txt
├── config.example.env
├── SYSTEM_ARCHITECTURE.md
├── .gitignore
├── README.md
└── dashboard/
    ├── index.html
    └── capstone-dashboard.png
```

## Requirements

- Python 3
- Internet connection
- Google Chrome or another modern browser

## Installation

Open Command Prompt in the project folder.

Create and activate a virtual environment:

```cmd
py -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```cmd
py -m pip install -r requirements.txt
```

## Running the IoT Device

Start the simulated device:

```cmd
py capstone_device.py
```

The device generates temperature and humidity readings every five seconds and publishes them to the MQTT broker.

## Running the Dashboard

1. Open `dashboard/index.html` in a browser.
2. Use the default MQTT WebSocket broker address:

`wss://test.mosquitto.org:8081`

3. Click Connect.
4. View the live temperature, humidity and received messages.

The device and dashboard must use the same MQTT topic.

## Configuration

The device supports these environment variables:

- `MQTT_BROKER`
- `MQTT_PORT`
- `MQTT_TOPIC`
- `SAMPLE_INTERVAL`

Example Windows configuration:

```cmd
set MQTT_BROKER=test.mosquitto.org
set MQTT_PORT=1883
set MQTT_TOPIC=aadav/smart-monitor/telemetry
set SAMPLE_INTERVAL=5
```

Run these commands in the same terminal before starting the device.

`config.example.env` is provided as a reference. It is not automatically loaded by the Python program.

## Reliability

- Automatic MQTT reconnection with increasing retry delays.
- QoS 1 publishing.
- Publish completion checks.
- Configurable sensor sampling interval.
- Dashboard reconnection handling.

## Power Considerations

The sampling interval can be increased to reduce how frequently the device generates and transmits readings.

Battery percentage is simulated for demonstration and is not a measurement of actual battery capacity.

## Security

- No passwords or broker credentials are hardcoded.
- Environment files and private key files are excluded using `.gitignore`.
- The public MQTT broker is used for demonstration only.
- Production deployment should use authenticated MQTT over TLS and secure credential storage.

## Testing

The device and dashboard were tested together using a public MQTT broker.

Successful testing demonstrated:
- MQTT connection.
- Sensor-data publishing.
- Dashboard subscription.
- Live temperature and humidity updates.

A dashboard screenshot is included in the `dashboard` folder.

## Limitations

This is a software-only IoT simulation. No physical microcontroller, sensor or battery was used.

The public MQTT broker is intended for testing and demonstration, not production deployment.

## Future Improvements

- Connect physical temperature and humidity sensors.
- Add historical data charts.
- Store readings in a database.
- Add authenticated MQTT communication.
- Implement real battery monitoring.

---

**Project:** Smart Environmental Monitor  
**Type:** IoT Capstone  
**Implementation:** Python, MQTT, HTML, CSS and JavaScript
