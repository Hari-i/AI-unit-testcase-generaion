from datasets import load_dataset

# Download the sanitized version (cleaned/tested)
mbpp = load_dataset("mbpp", "sanitized")

# Save as CSV
mbpp["train"].to_csv("mbpp_train.csv", index=False)

# Save as JSON
mbpp["train"].to_json("mbpp_train.json")