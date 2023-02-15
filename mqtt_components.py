from xai_components.base import InArg, OutArg, InCompArg, Component, BaseComponent, xai_component
from paho.mqtt import client as mqtt_client
import os


@xai_component
class MQTTConnect(Component):
    broker: InArg[str]
    port: InArg[int]
    client_id: InArg[str]
    username: InArg[str]
    password: InArg[str]

    def __init__(self):
        self.done = False
        self.broker = InArg.empty()
        self.port = InArg.empty()
        self.client_id = InArg.empty()
        self.username = InArg.empty()
        self.password = InArg.empty()

    def execute(self, ctx) -> None:
        client = mqtt_client.Client(self.client_id.value)
        if self.username.value is not None:
            client.username_pw_set(self.username.value, self.password.value)
        client.connect(self.broker.value, self.port.value)
        ctx['mqtt_client'] = client

@xai_component
class MQTTPublish(Component):
    topic: InArg[str]
    message: InArg[str]
    result: OutArg[int]

    def __init__(self):
        self.done = False
        self.topic = InArg.empty()
        self.message = InArg.empty()
        self.result = OutArg.empty()

    def execute(self, ctx) -> None:
        client = ctx['mqtt_client']
        result = client.publish(self.topic.value, self.message.value)
        client.loop()
        self.result.value = result[0]

@xai_component
class MQTTSubscribe(Component):
    on_message: BaseComponent
    topic: InArg[str]
    message: OutArg[str]

    def __init__(self):
        self.done = False
        self.topic = InArg.empty()
        self.message = OutArg.empty()

    def execute(self, ctx) -> None:
        client = ctx['mqtt_client']
        client.subscribe(self.topic.value)
        client.on_message = lambda c, data, msg: self.process_message(ctx, c, data, msg)

    def process_message(self, ctx, client, userdata, message):
        self.message.value = message.payload.decode()
        ctx['mqtt_message'] = message
        ctx['mqtt_userdata'] = userdata
        is_done, next_body = self.on_message.do(ctx)
        while next_body:
            is_done, next_body = next_body.do(ctx)

@xai_component
class MQTTStartLoop(Component):
    def __init__(self):
        self.done = False

    def execute(self, ctx) -> None:
        client = ctx['mqtt_client']

        try:
            client.loop_forever()
        except e:
            print(e)


@xai_component
class MQTTDisconnect(Component):
    def __init__(self):
        self.done = False

    def execute(self, ctx) -> None:
        client = ctx['mqtt_client']

        try:
            client.loop_stop()
        except e:
            print(e)

