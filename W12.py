import os

import requests

API_URL = "https://ollama.com/api/chat"
HEADERS = {"Authorization": "Bearer " + os.environ["OLLAMA_API_KEY"]}
while tool_called:
     
     tool_schema = {
            "type": "function",
            "function": {
                "name": "read_file",
                "description": "Use this when the user wants to read in a file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "the path of the file to read in is"},
                    },
                "required": ["path"]
                }
            }
        }

tool_schema = {
    "type": "function",
    "function": {
        "name": "read_file",
        "description": "Use this when the user wants to read in a file.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "the path of the file to read in is"},
            },
        "required": ["path"]
        }
    }
}

if function_name == "read_file" :

    list_files_schema = {
"type": "function",
"function": {
"name": "list_files",
"description": "Use this when the user wants to list files in the current working directory.",
"parameters": {
"type": "object",
"properties": {},
"required": []
}
}
}
def agent(messages):
tools = [
tool_schema, list_files_schema
]
payload = {
"model": "gpt-oss:120b",
"messages": messages,
"stream": False,
"tools": tools
}
response = requests.post(
API_URL,
headers=HEADERS,
json=payload,
timeout=300,
)
response.raise_for_status()
data = response.json()
message = data["message"]
return message
tool_called = True
messages = [
{"role": "user",
"content": "add 11 to the number of files i have in the current working
directory. use the tools for list_files and add2."}
]
while tool_called:
    message = agent(messages)
    tool_called = "tool_calls" in message

    if tool_called:
        print("tool called!")
        tool_calls = message["tool_calls"]
        tool_call = tool_calls[0]
        function_name = tool_call["function"]["name"]
        function_arguments = tool_call["function"]["arguments"]

    if function_name == "list_files":
        path = "."
        files = "\n".join(os.listdir(path))
        output = f"The output of {function_name} is: {files}"

    if function_name == "add2":
        arg1 = int(function_arguments["arg1"])
        arg2 = int(function_arguments["arg2"])
        print(f"function_name: {function_name}")
        print(f"arg1: {arg1}")
        print(f"arg2: {arg2}")
        output = arg1 + arg2
        tool_message = {
            "role": "tool",
            "content": f"The output of tool {function_name} is: {output}"
    }
    messages.append(tool_message)
else:
    ai_message = {
        "role": message["role"],
        "content": message["content"]
}
messages.append(ai_message)
last_message = messages[-1]
import pprint
printer = pprint.pprint
# printer(last_message)
print