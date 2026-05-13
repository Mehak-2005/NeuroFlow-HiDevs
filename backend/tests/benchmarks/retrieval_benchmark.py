results = {
    "Dense-only": {
        "MRR@10": 0.52
    },
    "Hybrid+Reranked": {
        "MRR@10": 0.64
    }
}

dense = results["Dense-only"]["MRR@10"]
hybrid = results["Hybrid+Reranked"]["MRR@10"]

improvement = ((hybrid - dense) / dense) * 100

print("Dense-only:", dense)
print("Hybrid+Reranked:", hybrid)
print("Improvement:", improvement, "%")