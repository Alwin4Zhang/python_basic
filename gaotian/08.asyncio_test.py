import time
import asyncio

"""
crountine

async def   叫crountine function  返回的是crountine object  本质上和生成器有点像
进行async模式，event loop；转换为task
asyncio.run  (1) 建立起event loop (2)将crountine编程event loop里面的第一个task
"""
# async def main():
#     print("hello")
#     await asyncio.sleep(1)
#     print("world")


# coro = main()
# # 从同步切换到异步
# asyncio.run(coro)


async def say_after(delay, what):
    await asyncio.sleep(delay)
    # print(what)
    return f"{what} - {delay}"


async def main():
    print(f"started at {time.strftime('%X')}")
    # await 将say_after变为crountine
    # await say_after(1, 'hello')  # crountine被包装成了task 主动权交给event loop  等待1s
    # await say_after(2, 'world')  # crountine被包装成了task  等待2s

    # 总共等待了3s  其实还可以效率更高，协程就是来解决这个问题

    # 这种方式可以让await没有先后顺序同时执行
    # crountine被asyncio创建为task 后需要await task
    # task1 = asyncio.create_task(say_after(1, 'hello'))
    # task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"finished at {time.strftime('%X')}")
    # ret1 = await task1
    # ret2 = await task2
    # print(ret1)
    # print(ret2)

    # ret = await asyncio.gather(task1, task2)

    # asyncio.gather可以直接把crountine直接变为
    ret = await asyncio.gather(
        say_after(1, 'hello'),
        say_after(2, 'world')
    )
    print(ret)  # 若干task的结果放到list里面

    print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())
