# from llm_sdk import Small_LLM_Model
from src.parser import parse_args, get_prompts, get_functions
import json


def main() -> None:
    program_args = parse_args()
    try:
        prompts = get_prompts(program_args.input)
        print("Prompts:", prompts)
        functions = get_functions(program_args.functions_definition)
        print("Functions:", functions)
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        exit(1)
    except FileNotFoundError as e:
        print(f"Error: The file '{e.filename}' was not found.")
        exit(1)
    except ValueError as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
