
import json
import os
import random
import time
import socket
import uuid
from datetime import datetime, timezone

import paho.mqtt.client as mqtt

BROKER = os.getenv("MQTT_BROKER", "test.mosquitto.org")
PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPIC = os.getenv("MQTT_TOPIC", "aadav/smart-monitor/telemetry")
INTERVAL = float(os.getenv("SAMPLE_INTERVAL", "5"))

DEVICE_ID = "environment-monitor-" + socket.gethostname()
CLIENT_ID = "capstone-" + uuid.uuid4().hex[:8]


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected to MQTT broker!")
        print("Publishing to:", TOPIC)
    else:
        print("Connection failed:", reason_code)


def on_disconnect(client, userdata, disconnect_flags, reason_code, properties):
    print("Disconnected. MQTT client will attempt to reconnect.")


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id=CLIENT_ID
)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.reconnect_delay_set(min_delay=1, max_delay=30)

print("SMART ENVIRONMENTAL MONITOR")
print("Device ID:", DEVICE_ID)
print("Broker:", BROKER)
print("Sampling interval:", INTERVAL, "seconds")
print("Press Ctrl+C to stop.\n")

try:
    client.connect(BROKER, PORT, keepalive=60)
    client.loop_start()

    reading_number = 0

    while True:
        reading_number += 1

        temperature = round(random.uniform(22.0, 35.0), 1)
        humidity = round(random.uniform(35.0, 80.0), 1)
        battery = max(0, 100 - (reading_number * 0.05))

        payload = {
            "device_id": DEVICE_ID,
            "reading": reading_number,
            "temperature": temperature,
            "humidity": humidity,
            "battery_percent": round(battery, 1),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        message = json.dumps(payload)

        if client.is_connected():
            result = client.publish(TOPIC, message, qos=1)

            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                try:
                    result.wait_for_publish(timeout=10)

                    if result.is_published():
                        print("PUBLISHED:", message)
                    else:
                        print("Message delivery not confirmed.")

                except RuntimeError:
                    print("Message delivery failed or timed out.")

            else:
                print("Publish failed. MQTT will reconnect.")

        else:
            print("Waiting for MQTT connection...")

        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print("\nStopping device...")

except Exception as error:
    print("Device error:", error)

finally:
    client.loop_stop()
    client.disconnect()
    print("Device stopped.")