
# Smart Environmental Monitor — System Architecture

```mermaid
flowchart TD
    A["Simulated IoT Device<br/>Temperature + Humidity"]
    B["MQTT Client<br/>Python + Paho"]
    C["Public MQTT Broker<br/>test.mosquitto.org"]
    D["Web Dashboard<br/>HTML + JavaScript"]
    E["Live Readings<br/>Temperature + Humidity"]

    A --> B
    B -->|"MQTT publish, QoS 1"| C
    C -->|"MQTT over WebSocket"| D
    D --> E

    F["Reconnection and retry"]
    G["Configurable sampling interval"]
    H["Environment-based configuration"]

    B -.-> F
    A -.-> G
    B -.-> H
```

## Data flow

1. The simulated device generates temperature and humidity readings.
2. The Python MQTT client publishes readings to the MQTT broker.
3. The browser dashboard subscribes to the same MQTT topic.
4. Incoming messages are displayed as live sensor readings.

## Reliability

- MQTT automatic reconnection is configured.
- The device uses QoS 1 for message delivery.
- Sampling interval is configurable.
- The dashboard attempts to reconnect when disconnected.

## Power considerations

- Sensor sampling is controlled by a configurable interval.
- A longer sampling interval can reduce device activity.
- Battery percentage is simulated for demonstration only.

## Security considerations

- No broker credentials or passwords are hardcoded.
- Broker settings can be configured using environment variables.
- The public test broker is used for demonstration, not production.
- Production deployment should use authenticated MQTT over TLS.
