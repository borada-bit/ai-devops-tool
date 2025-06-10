# ai-devops-tool

A command-line tool that uses Ollama's LLM to generate DevOps files (such as Dockerfile, docker-compose, etc.) from natural language instructions.

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) running locally
- Dependencies from `requirements.txt`

## Installation

1. Clone this repository.
2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the tool with your instruction as an argument:

```sh
python main.py "Node.js app with MongoDB using Docker Compose"
```

The output will be a ready-to-use DevOps file (e.g., Dockerfile or docker-compose.yml) with no extra explanations or comments. Codellama is the recommended model.

## Example

```sh
python main.py "Simple Python Flask app Dockerfile"
```

## License

MIT