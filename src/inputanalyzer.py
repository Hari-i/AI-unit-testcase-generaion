from datasets import load_dataset

ds = load_dataset("openai/openai_humaneval")

ds['test'].to_json("humaneval_test.jsonl")
ds['train'].to_json("humaneval_train.jsonl") if 'train' in ds else None
ds['validation'].to_json("humaneval_validation.jsonl") if 'validation' in ds else None