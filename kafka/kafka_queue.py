from aiokafka import AIOKafkaProducer
import asyncio

async def send_one():
    producer = AIOKafkaProducer(bootstrap_servers='51.38.185.58:9092')
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait("exo1", """Merci monsieur""")
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

asyncio.run(send_one())