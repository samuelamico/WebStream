from page import PageAccess

import asyncio


def main():
    try:
        asyncio.run(producer_event())
    except KeyboardInterrupt as e:
        print("shutting down")


async def producer_event():
    """Produces data into the Kafka Topic"""

    while True:
        p = PageAccess()
        p.run()
        await asyncio.sleep(1.5)

if __name__ == "__main__":
    main()
