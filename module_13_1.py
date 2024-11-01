
import asyncio


async def start_strongman(name, power):

    print(f"Силач {name} начал соревнования")

    for num in range(1, 6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {num} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():

    strongmen = [
        ('Pasha', 3),
        ('Denis', 4),
        ('Apollon', 5)

    ]

    for name, power in strongmen:
        print(f"'{name}', {power}")
    print("Результаты спортсменов: \n")
    tasks = [asyncio.create_task(start_strongman(name, power)) for name, power in strongmen]
    for task in tasks:
        await task

if __name__ == '__main__':
    print("Участники соревнования: \n")
    asyncio.run(start_tournament())