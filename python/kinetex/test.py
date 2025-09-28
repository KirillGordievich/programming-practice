import random
import asyncio
from datetime import datetime, UTC

from pydantic import BaseModel
from uuid import UUID, uuid4
from secrets import token_urlsafe

# Задача 1: составить модель транзакции и сделать список случайных транзакций
class Transaction(BaseModel):
    id: UUID
    status: str
    created_at: datetime
    sender: str
    receiver: str
    amount: int

users = [token_urlsafe() for _ in range(5)]
txs = [Transaction(
        id=uuid4(),
        status='PENDING',
        created_at=datetime.now(tz=UTC),
        sender=random.choice(users),
        receiver=random.choice(users),
        amount=random.randint(1, 10000)
    ) for _ in range(100)]

# Задача 2: найти транзакцию с максимальным амаунтом
# print(max(txs, key=lambda t: t.amount))

# Задача 3: составить словарь где ключ айди транзанкции, а значение сама транзакция
# d = { t.id: t for t in tx }
# print(d)

# Задача 4: составить словарь, где юзер это ключ, а значение список его транзакций
# users_txs = {}
# for tx in txs:
#     if tx.sender not in users_txs:
#         users_txs[tx.sender] = []
#     users_txs[tx.sender].append(tx)
#
# print(users_txs)

# Задача 5: случайно генерировать транзакции в асинхронном генераторе
async def generate_tx():
    while True:
        yield Transaction(
            id=uuid4(),
            status='PENDING',
            created_at=datetime.now(tz=UTC),
            sender=random.choice(users),
            receiver=random.choice(users),
            amount=random.randint(1, 10000)
        )
        await asyncio.sleep(random.randint(1, 3))

lock = asyncio.Lock()

# Задание 6: написать примитивный синхронизатор запущенных генераторов
def block(func):
    async def new_fn(*args, **kwargs):
        async with lock:
            res = await func(*args, **kwargs)
            return res
    return new_fn

@block
async def consume_tx(tx: Transaction):
    # async with lock:
    await asyncio.sleep(random.randint(1, 3))

    print('Computing...')

    await asyncio.sleep(random.randint(1, 3))

    print(tx.id)

async def run_async_generator():
    async for tx in generate_tx():
        await consume_tx(tx)


async def main():
    tasks = [
        asyncio.create_task(run_async_generator()),
        asyncio.create_task(run_async_generator()),
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())

"""
SELECT
    (SELECT count(*) FROM transaction) AS total,
    t.sender,
    count(t.*)
FROM transaction AS t
GROUP BY t.sender
HAVING count(t.*) > 5

SELECT colum1
UNION
SELECT colum2
"""