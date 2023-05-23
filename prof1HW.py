from pydantic import BaseModel

class GetDifficulty(BaseModel):
    progressPercent: float
    difficultyChange: float
    estimatedRetargetDate: float
    remainingBlocks: int
    remainingTime: int
    previousRetarget: float
    previousTime: int
    nextRetargetHeight: int
    timeAvg: int
    timeOffset: int
    expectedBlocks: float

class GetAddress(BaseModel):
    address: str
    chain_stats: dict
    mempool_stats: dict

class GetRewardStats(BaseModel):
    startBlock: int
    endBlock: int
    totalReward: int
    totalFee: int
    totalTx: int


from aiohttp import ClientSession
from ujson import dumps, loads

async def get_difficulty():
    async with ClientSession(
            base_url='https://mempool.space',
            json_serialize=dumps
    ) as session:
        response = await session.get(
            url='/api/v1/difficulty-adjustment'
        )

        return await response.json(loads=loads)

async def get_address():
    async with ClientSession(
        base_url='https://mempool.space',
        json_serialize=dumps
    ) as session:
        response = await session.get(
            url='/api/address/1wiz18xYmhRX6xStj2b9t1rwWX4GKUgpv'
        )
        return await response.json(loads=loads)

async def get_reward_stats():
    async with ClientSession(
        base_url='https://mempool.space',
        json_serialize=dumps
    ) as session:
        response = await session.get(
            url='/api/v1/mining/reward-stats/100'
        )
        return await response.json(loads=loads)

if __name__ == '__main__':
    import asyncio
    asyncio.run(get_difficulty())
    asyncio.run(get_address())
    asyncio.run(get_reward_stats())

    get_difficulty1 = GetDifficulty(**asyncio.run(get_difficulty()))
    get_adress1 = GetAddress(**asyncio.run(get_address()))
    get_reward_stats1 = GetRewardStats(**asyncio.run(get_reward_stats()))

print(get_difficulty1)
print(get_adress1)
print(get_reward_stats1)