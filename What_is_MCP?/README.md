# MCP (Model Context Protocol): 
it is an communicaiton layer between LLM's by which the resources(like context anad tools) are accessible for Training LLM's to get train.
MCP server provides access to the external service with the functionality and tools in it. The basic architechture:

### The MCP components:
- Prompts
- Resources
- Tools
  
<img width="750" height="600" alt="image" src="https://github.com/user-attachments/assets/e68a1adb-cf52-45c1-a666-05b988058484" />


Following is the Working Flow of an MCP, yes it a little bit complex but it provides us the functionality and tools, 
which we don't have to write manually and the inclusion of Claude will make it more easier because with "NLP", 
it will do the technical work and writing command just like that by a simple "Prompt"

<img width="1000" height="850" alt="image" src="https://github.com/user-attachments/assets/7db5923d-a75b-444a-b4ca-f9d8b0ee672a" />


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
### #TIPS: "PYTHON MCP SDK" is lot easier than writing to writing json schema defination manually:

### Key Benefits of the SDK Approach:
- No manual JSON schema writing required
- Type hints provide automatic validation
- Clear parameter descriptions help Claude understand tool usage
- Error handling integrates naturally with Python exceptions
- Tool registration happens automatically through decorators

The MCP Python SDK transforms tool creation from a complex schema-writing exercise into simple Python function definitions. This approach makes it much easier to build and maintain MCP servers while ensuring Claude receives properly formatted tool specifications.

# The Server Inspector:

As it provides a in built browser Debugger because of "PYTHON SDK" this will be help full while adding functionalities to our "MCP Server", 
so we can make sure the Server is working properly.

- make sure that our python environment is activated.

run this command in terminal:
```
mcp dev mcp_server.py
```
this will open an server listening to a speacific port where mcp inspector will appear.

### Inspector Interface:

The inspector interface is actively being developed, so it may look different when you use it. However, the core functionality remains consistent. Look for these key elements:

- A Connect button to start your MCP server
- Navigation tabs for Resources, Tools, Prompts, and other features
- A tools listing and testing panel
- Testing Tools interaction.

Click the Connect button first to initialize your server. You'll see the connection status change from "Disconnected" to "Connected".

### Development Workflow:

The MCP Inspector becomes an essential part of your development process. Instead of writing separate test scripts or connecting to full applications, you can:

- Quickly iterate on tool implementations
- Test edge cases and error conditions
- Verify tool interactions and state management
- Debug issues in real-time

This immediate feedback loop makes MCP server development much more efficient and helps catch issues early in the development process.

# Connecting the "MCP Client":

### The MCP client consists of two main components:

- MCP Client - A custom class we create to make using the session easier
- Client Session - The actual connection to the server (part of the MCP Python SDK)


### understanding the architecture of mcp client:

<img width="750" height="600" alt="image" src="https://github.com/user-attachments/assets/8559bdc6-15bc-4528-a9a5-a3da6dda9cfb" />

The client session requires careful resource management - we need to properly clean up connections when we're done. That's why we wrap it in our own class that handles all the cleanup automatically.

once all the changes is done run the python client script (mcp_client.py) be carefull and check if the use of "uv" is required or not.
please go through the (mcp_client.py) script in which functionalities are added to test this:

run this command:
```
# using "uv" 
uv run mcp_client.py
```
or 
```
# without "uv"
python mcp_client.py
```

after checking the functionalities are working properly

run the command with or without "uv" in terminal:
```
un run main.py
```
or 
```
python main.py
```
## Now Ask you claude or query about the documents example (ask for content of "document.txt"). it should response the content of document.txt 
## and Here is our "CLI ChatBot" project is completed.

### Here's what happens behind the scenes:

- Your application uses the client to get available tools
- These tools are sent to Claude along with your question
- Claude decides to use the read_doc_contents tool
- Your application uses the client to execute that tool
- The result is returned to Claude, who then responds to you

The client acts as the bridge between your application logic and the MCP server's functionality, making it easy to integrate powerful tools into your AI workflows.
