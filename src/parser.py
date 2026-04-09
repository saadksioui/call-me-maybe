from argparse import Namespace, ArgumentParser
from src.models import FunctionModel
from typing import Dict, List
import json


def get_functions(path: str) -> List[FunctionModel]:
    with open(path, 'r') as f:
        data = json.load(f)
    if not isinstance(data, List):
        raise ValueError('f')
    return [FunctionModel(**item) for item in data]


def get_prompts(path: str) -> List[str]:
    prompts = []
    with open(path, 'r') as f:
        data = json.load(f)
    if not isinstance(data, List):
        raise ValueError('ddd')
    for item in data:
        if isinstance(item, str):
            prompts.append(item)
        elif isinstance(item, Dict):
            if "prompt" in item and isinstance(item['prompt'], str):
                prompts.append(item['prompt'])

    return prompts


def parse_args() -> Namespace:
    args = ArgumentParser()
    args.add_argument('--input',
                      default='data/input/function_calling_tests.json',
                      help='Input file containing function calling tests')
    args.add_argument('--functions_definition',
                      default='data/input/functions_definition.json',
                      help='Input file containing functions definition')
    args.add_argument('--output',
                      default='data/output/function_calls.json',
                      help='Output file containing function calls')
    return args.parse_args()
