import json
import logging

import azure.functions as func
import azure.durable_functions as df

def main(event: func.EventGridEvent, starter: str):
    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })
    logging.warning(f"Starter is {starter}")
    client = df.DurableOrchestrationClient(starter)
    entity_id = df.EntityId("Counter", "myCounter")
    client.signal_entity(entity_id, "add", 1)
    logging.info('Python EventGrid trigger processed an event: %s', result)
