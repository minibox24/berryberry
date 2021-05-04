# StrawberryDonut/Interpreter commit 47c31c7 modification version

import asyncio

from interpreter import Parser, Execute
from interpreter.Execute import toString


code = """
import "local:main"

bb = BerryBerry()

bb.run(bb, "Hello, World!")
"""


async def main():
    exe = Execute.ExecuteClass({})

    parse_res = Parser.parse(code)

    execute_res = await exe.execute(parse_res)
    if execute_res:
        print(toString(execute_res))


asyncio.run(main())