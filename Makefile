install:
	cd llm_sdk && uv sync

run:
	uv run python -m src --functions_definition data/input/functions_definition.json \
							--input data/input/function_calling_tests.json \
							--output data/output/function_calls.json