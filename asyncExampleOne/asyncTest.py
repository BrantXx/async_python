import asyncio

async def func_one():
	await asyncio.sleep(5)
	return "Finished #1"

async def func_two():
	await asyncio.sleep(5)
	return "Finished #2"

async def func_three():
	await asyncio.sleep(5)
	return "Finished #3"

async def start_one():
	try:
		print(await func_one())
		await start_two()
	except Exception as e:
		print(e)
	finally:
		print("Finished All 3")

async def start_two():
	print(await func_two())
	await start_three()

async def start_three():
	print(await func_three())

async def main():
	await start_one()

# Start Loop
loop = asyncio.get_event_loop()

# Run the Loop until main() is complete
loop.run_until_complete(main())

# Close the Loop
loop.close()
