from sklearn.datasets import load_breast_cancer

dataset = load_breast_cancer()

print("=== dataset.data ===")
print("type: {type(dataset.data)}")
print(f"shape: {dataset.data.shape}")
print(f"head: \n{dataset.data[:5]}\n")

print("=== dataset.target ===")
print(f"type: {type(dataset.target)}")
print(f"shape: {dataset.target.shape}")
print(f"head: {dataset.target[:5]}\n")

print("=== dataset.feature_names ===")
print(f"type: {type(dataset.feature_names)}")
print(f"length: {len(dataset.feature_names)}")
print(f"values: {dataset.feature_names}\n")

print("=== dataset.target_names ===")
print(f"type: {type(dataset.target_names)}")
print(f"shape: {dataset.target_names.shape}")
print(f"values: {dataset.target_names}")