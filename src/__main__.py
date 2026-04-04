# from argparse import ArgumentParser, Namespace
# import sys
# import json


# def parse_args():
#     parser = ArgumentParser()
#     parser.add_argument('--input',
#                         default='../data/input/function_calling_tests.json',
#                         help='Json file for prompts',
#                         type=str)
#     parser.add_argument('--function_definition',
#                         default='../data/input/functions_definition.json',
#                         help='Json file for fuunction definitions')
#     parser.add_argument('--output',
#                         default='../data/output/function_calling_results.json')
#     return parser.parse_args()


# def validate_paths(args: Namespace):
#     pass


# def function_loader(path) -> json:
#     ...


# if __name__ == "__main__":
#     parser = parse_args()
#     functions = function_loader(parser.function_definition)
#     print(parser.function_definition)
#     sys.exit(0)

from llm_sdk import Small_LLM_Model

model = Small_LLM_Model()

prompt = "What is the capiltal of france"
input = model.encode(prompt)[0].tolist()
print(input)
output = []
for i in range(0, 20):
    logits = model.get_logits_from_input_ids(input)
    max_logits = max(logits)
    next = logits.index(max_logits)
    input.append(next)
    output.append(next)
print(model.decode(output))