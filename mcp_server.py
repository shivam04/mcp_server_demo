from mcp.server.fastmcp import FastMCP

# create an MCP sever
mcp = FastMCP()

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print(f"Adding {a} and {b}")
    return a + b

@mcp.resource("resource://some_static_resource")
def get_static_resource() -> str:
    """Static resource data"""
    return "Any static data can be returned"

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Greeting resource data"""
    return f"Hello, {name}"

@mcp.prompt()
def review_code(code: str) -> str:
    """Review code"""
    return f"Please review this code:\n\n{code}"

@mcp.prompt()
def debug_error(error: str) -> list[tuple]:
    return [
        ("user", "I'm seeing this error:"),
        ("user", error),
        ("assistant", "I will help debug that. What have you tried so far?")
    ]

if __name__ == "__main__":
    mcp.run(transport='sse')