from mcp import ClientSession
from mcp.client.sse import sse_client

async def run():
    async with sse_client(url="http://localhost:8000/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print(tools)

            # call a tool
            result = await session.call_tool("add", arguments={"a": 4, "b": 5})
            print(result.content[0].text)

            resources = await session.list_resources()
            print("resources", resources)

            content = await session.read_resource("resource://some_static_resource")
            print("content", content.contents[0].text)

            resources = await session.list_resources()
            print("resources", resources)

            content = await session.read_resource("greeting://shivam")
            print("content", content.contents[0].text)

            prompts = await session.list_prompts()
            print("prompts", prompts)

            prompt = await session.get_prompt("review_code", arguments={"code": "print(\"Hello world\")"})
            print("prompt", prompt.messages[0].content.text)

            prompt = await session.get_prompt("debug_error", arguments={"error": "SyntaxError: invalid syntax"})
            print("prompt", prompt.messages[0].content.text)



if __name__ == '__main__':
    import asyncio

    asyncio.run(run())