## Synchronous Programming Example 
import time
def greet(name):
    print(f"Hello, {name}!")
    time.sleep(2)
    print(f"Goodbye, {name}!")
greet("Umer")
greet("Ayesha")
greet("Mustafa")

## Asynchronous Programming Example
import asyncio
async def greet(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(2)
    print(f"Goodbye, {name}!")
async def main():
    await asyncio.gather(
        greet("Umer"),
        greet("Ayesha"),
        greet("Mustafa")
    )
asyncio.run(main())

