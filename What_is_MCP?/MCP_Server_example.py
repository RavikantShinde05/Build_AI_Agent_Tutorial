# These is an other example of creating an mcp Server using "PYTHON MCP SDK'S".
# Where as in most of the cases we need to create "MCP Client" only but to understand we are going to
# create "MCP CLIENT & SERVER"

# The following is the package use to establish an MCP server.
from pydantic import Field
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("documentsMCP", log_levels="ERROR")

# here all the list of documents are store only in memory.
docs = {
    "Document.md": "The company docs",
    "Financial.docx": "The company docs",
    "presentation.docx": "the slide for the presentation of current year production report",
    "Formats.txt": "The required formats for all the legal documents and company policies according to Annexure",
    "report.pdf": "this is the report for the current year production results"
}

# Write a "TOOL TO READ THE DOCUMENTS":


@mcp.tool(
    name="read_document",
    # Write is clear to understand by claude and when to use it.
    description="Read the content of the document and return it as a string"

)
def read_document(
    doc_id: str = Field("Id of the document to be Read")
):
    if doc_id not in docs:  # If the ID does not exist in the list of Docs.
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]


# Write a "TOOL TO EDIT THE DOCUMENT0":
@mcp.tool(
    name="edit_document",
    description="Edit a Document by Replacing a String in the document content with a new string"
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(
        description="The text to replace. Must match the exactly, including whitespace"),
    new_str: str = Field(
        description="The new text to be insert in place of old text")

):
    if doc_id not in docs:  # If the document does not exist in the list of Document.
        raise ValueError(f"the doc with id {doc_id} is not found")

# Replace the "old string" with "new string"
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)
