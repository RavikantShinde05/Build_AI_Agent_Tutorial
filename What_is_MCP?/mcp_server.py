# "PYTHON MCP SDK" is lot easier than writing to writing schema defination manually
from pydantic import Field
from mcp.server.fastmcp import FastMCP

# These file is at root project directory
mcp = FastMCP("DocumentMCP", log_levels="ERROR")

# These are the Colloction of document defined only in memory:
docs = {
    "Document.md": "The company docs",
    "Document.docx": "the slide for the presentation of current year production report",
    "Document.txt": "The required formats for all the legal documents and company policies according to Annexure",
    "Document.pdf": "this is the company broucher"

}
# we gonna create a tool using python SDK's, these SDK will help us to build our "Mcp Server"


@mcp.tool(
    name="add_ints"
    # Description must be clear to know When to use this Tool for claude.
    description="Adding the two integers"
)
def tool_fn(
        a=Field(description="First integer to add"),
        b=Field(description="Second integer to add")

) -> int:
    return a + b


if name == " main ":
    mcp.run(transport="stdio")
