from ucimlrepo import fetch_ucirepo

# Fetch dataset
iris = fetch_ucirepo(id=53)

# Get data
X = iris.data.features
y = iris.data.targets

# Find total number of records
total_records = len(X)

# Find different flower names
different_flowers = y.iloc[:, 0].unique().tolist()

# Find total number of different flowers
total_flowers = len(different_flowers)

print("Total number of records:", total_records)
print("Total number of different flowers:", total_flowers)
print("Names of different flowers:", different_flowers)