import typing


class Calculate:
    def __init__(self, results: typing.List[float]):
        self.results = results
        self.best = max(results)
        self.worst = min(results)
        self.number_of_results = len(results)
        self.average = sum(results) / self.number_of_results