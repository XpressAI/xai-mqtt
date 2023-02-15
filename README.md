# xai-mqtt
A [Xircuits](https://xircuits.io) component library for MQTT

## Installation

You can add this component library to you xai_components folder.


## Usage

Use the `MQTTConnect` component to connect to the broker.

To subscribe to messages in your xircuits diagram, add a `MQTTSubscribe` node
and specify a topic. Next connect the components you want to use to process the
messages to the `on_message` tirangle.

Finally add a `MQTTStartLoop` to begin the processing.  Execution will not 
continue after the `MQTTStartLoop` component as it loops forever.

To publish a message using xircuits add a `MQTTPublish` node to the diagram and
specify a topic and message to send.  The message will be sent immediately.

