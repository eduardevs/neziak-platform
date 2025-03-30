def individual_algo(algo):
    return {
        "_id": str(algo["_id"]),
        "name": str(algo["name"]),
        "description": str(algo["description"]),
        "complexity": str(algo["complexity"]),
        "is_done": str(algo["is_done"]),
        "creation": str(algo["creation"]),
    }

    # name: str
    # description: str
    # complexity: BigOComplexity
    # is_done: bool = False
    # creation: int = int( datetime.timestamp(datetime.now()))


def all_algorithms(algos):
    return [individual_algo(algo) for algo in algos]
