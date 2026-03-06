# MCP (Model Context Protocol): 
it is an communicaiton layer between LLM's by which the resources(like context anad tools) are accessible for Training LLM's to get train.
MCP server provides access to the external service with the functionality and tools in it. The basic architechture:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e68a1adb-cf52-45c1-a666-05b988058484" />


Following is the Working Flow of an MCP, yes it a little bit complex but it provides us the functionality and tools, 
which we don't have to write manually and the inclusion of Claude will make it more easier because with "NLP", 
it will do the technical work and writing command just like that by a simple "Prompt"

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7db5923d-a75b-444a-b4ca-f9d8b0ee672a" />


# Create an MCP Server by writing Tools in it:
### 1. create a file name mcp_server.py:
```
# These is an example of creating an mcp Server using "PYTHON MCP SDK'S".
# Where as in most of the cases we need to create "MCP Client" only but to understand we are going to create "MCP CLIENT & SERVER"

from pydantic import Field
from mcp.server.fastmcp import FastMCP

# These file is at root project directory
mcp = FastMCP("DocumentMCP", log_levels="ERROR")

```

### 2. These are the Colloction of document defined only in memory:

```
docs = {
    "Document.md": "The company docs",
    "Document.docx": "the slide for the presentation of current year production report",
    "Document.txt": "The required formats for all the legal documents and company policies according to Annexure",
    "Document.pdf": "this is the company broucher"

}
```
### 3. we gonna create a tool using python SDK's, these SDK will help us to build our "Mcp Server"
```
@mcp.tool(
    name= "add_ints"
    description ="Adding the two integers" # Description must be clear to know When to use this Tool for claude.
)
def tool_fn(
        a = Field(description = "First integer to add"),
        b = Field(description = "Second integer to add")

)-> int:
    return a + b
    

if name == " main ":
    mcp.run(transport="stdio")

```
### #TIPS: "PYTHON MCP SDK" is lot easier than writing to writing json schema defination manually

Key Benefits of the SDK Approach:
- No manual JSON schema writing required
- Type hints provide automatic validation
- Clear parameter descriptions help Claude understand tool usage
- Error handling integrates naturally with Python exceptions
- Tool registration happens automatically through decorators

The MCP Python SDK transforms tool creation from a complex schema-writing exercise into simple Python function definitions. This approach makes it much easier to build and maintain MCP servers while ensuring Claude receives properly formatted tool specifications.
