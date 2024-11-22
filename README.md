
<p align="center">
  <a href="https://github.com/XpressAI/xircuits/tree/master/xai_components#xircuits-component-library-list">Component Libraries</a> •
  <a href="https://github.com/XpressAI/xircuits/tree/master/project-templates#xircuits-project-templates-list">Project Templates</a>
  <br>
  <a href="https://xircuits.io/">Docs</a> •
  <a href="https://xircuits.io/docs/Installation">Install</a> •
  <a href="https://xircuits.io/docs/category/tutorials">Tutorials</a> •
  <a href="https://xircuits.io/docs/category/developer-guide">Developer Guides</a> •
  <a href="https://github.com/XpressAI/xircuits/blob/master/CONTRIBUTING.md">Contribute</a> •
  <a href="https://www.xpress.ai/blog/">Blog</a> •
  <a href="https://discord.com/invite/vgEg2ZtxCw">Discord</a>
</p>



<p align="center"><i>Xircuits Component Library for MQTT. Easily connect, subscribe, and publish using MQTT in Xircuits workflows.</i></p>

Welcome to the xai-mqtt component library! This library provides the necessary components to work with MQTT in your Xircuits workflows. You can easily connect to an MQTT broker, subscribe to topics, and publish messages within your Xircuits pipelines.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Prerequisites](#prerequisites)
- [Installing an MQTT Broker](#installing-an-mqtt-broker)
  
  - [Installing Mosquitto on Ubuntu/Debian](#installing-mosquitto-on-ubuntu-debian)
  - [Installing Mosquitto on Windows](#installing-mosquitto-on-windows)
  - [Installing Mosquitto on macOS](#installing-mosquitto-on-macos)
- [Installation](#installation)
- [Getting Started with Xai-MQTT](#getting-started-with-xai-mqtt)
- [Running the Example Workflow](#running-the-example-workflow)
- [Testing Mosquitto](#testing-mosquitto)
- [MQTT Workflow](#mqtt-workflow)
  - [Subscribing to Topics](#subscribing-to-topics)
  - [Publishing Messages](#publishing-messages)

## Prerequisites

Before you begin, ensure you have the following:

1. Python 3.9+.
2. Xircuits.


## Installing an MQTT Broker
To use the xai-mqtt library, you'll need to have an MQTT broker installed on your device. One popular option is **Mosquitto**, an open-source message broker that implements the MQTT protocol.



### Installing Mosquitto on Ubuntu/Debian

1. Update your package lists and install Mosquitto:

   ```bash
   sudo apt-get update
   sudo apt-get install -y mosquitto mosquitto-clients
   ```

2. Enable Mosquitto to start on boot and then start the service:

   ```bash
   sudo systemctl enable mosquitto
   sudo systemctl start mosquitto
   ```

3. Verify that Mosquitto is running by checking its status:

   ```bash
   sudo systemctl status mosquitto
   ```

### Installing Mosquitto on Windows

1. Download the Mosquitto installer from the [official Mosquitto website](https://mosquitto.org/download/).
2. Run the installer and follow the instructions to complete the setup.
3. Once installed, open a terminal and start the Mosquitto broker:

   ```bash
   mosquitto
   ```

4. You can also install it as a service during the installation process to ensure it runs automatically.

### Installing Mosquitto on macOS

1. Install Mosquitto via Homebrew:

   ```bash
   brew install mosquitto
   ```

2. Start the Mosquitto service:

   ```bash
   brew services start mosquitto
   ```

3. Verify that Mosquitto is running:

   ```bash
   brew services list
   ```

## Installation

To use this component library, ensure that you have an existing [Xircuits setup](https://xircuits.io/docs/main/Installation). You can then install the MQTT library using the [component library interface](https://xircuits.io/docs/component-library/installation#installation-using-the-xircuits-library-interface), or through the CLI using:

```
xircuits install mqtt
```

You can also install it manually by cloning the repository and installing it:

```
# base Xircuits directory
git clone https://github.com/XpressAI/xai-mqtt xai_components/xai_mqtt
pip install -r xai_components/xai_mqtt/requirements.txt
```

## Getting Started with Xai-MQTT

Once installed, you can start using the xai-mqtt component library to connect, subscribe, and publish to an MQTT broker in your Xircuits workflows.

## Running the Example Workflow

Before testing Mosquitto, **you need to run the `mqtt_sample.xircuits` example workflow** provided in the library. This workflow demonstrates how to connect, subscribe, and publish messages using the MQTT components in Xircuits.

Once you have run the example, you can manually test Mosquitto using the following steps:

## Testing Mosquitto

After running the example workflow, you can manually test Mosquitto using the following steps:

1. **Subscribe to a topic** by running this command in one terminal:

   ```bash
   mosquitto_sub -h localhost -p 1883 -t "testing_reply"
   ```

2. **Publish a message** by running this command in another terminal:

   ```bash
   mosquitto_pub -h localhost -p 1883 -t "testing" -m "anyword"
   ```

   The output in the subscriber terminal will be the message sent in the publisher command. If you publish `"anyword"`, the result will display:

   ```
   anyword!!!
   ```

## MQTT Workflow

### Subscribing to Topics

1. Use the `MQTTConnect` component to connect to the MQTT broker by providing the broker address.
2. Add the `MQTTSubscribe` component to your Xircuits diagram and specify the topic you want to subscribe to.
3. Connect the components you want to use to process the messages to the `on_message` triangle of the `MQTTSubscribe` component.
4. Finally, add the `MQTTStartLoop` component to start processing. Execution will not continue past the `MQTTStartLoop` component as it enters a loop to process incoming messages.

### Publishing Messages

1. Use the `MQTTPublish` component to publish messages to a specified topic.
2. Specify the topic and message content in the `MQTTPublish` component, and the message will be sent immediately.

These components allow you to fully integrate MQTT messaging within your Xircuits workflows, providing an easy way to connect, subscribe, and publish to MQTT topics.

## Contributing

We welcome contributions to the **Mqtt XAI Components Library**! If you would like to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Open a pull request with a detailed description of your changes.

Please feel free to suggest new components, improvements, or optimizations. If you encounter any issues or have ideas for enhancements, you can open an issue in the repository.

---

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.