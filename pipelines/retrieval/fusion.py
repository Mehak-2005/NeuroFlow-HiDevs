def reciprocal_rank_fusion(result_lists, k=60):
    scores = {}

    for result_list in result_lists:
        for rank, item in enumerate(result_list):
            scores[item] = scores.get(item, 0) + 1 / (k + rank + 1)

    return sorted(scores, key=scores.get, reverse=True)