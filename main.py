from ollama import chat
from ollama import ChatResponse
import argparse

# Parse command line arguments, the argument is the instruction for the model to generate a devops file (Dockerfile, docker-compose, etc.)
parser = argparse.ArgumentParser(description='Generate a devops file using Ollama.')
parser.add_argument('instruction', type=str, help='Instruction for the model to generate a devops file')
args = parser.parse_args()

response: ChatResponse = chat(model='codellama', messages=[
  {
    'role': 'user',
    'content': 'Generate a devops file for the following instruction: ' + args.instruction + '. Output ONLY devops file that can be pasted straightaway and used straightaway. Do not include any additional text or explanations in the output. Just the file without anything else. The output should be ready to be copied and pasted into a file. It should be just like if you were writing a Dockerfile or docker-compose file directly. Do not include any comments or explanations in the output of the file or your reasoning. Just the devops file.',
  },
])

print(response.message.content)
