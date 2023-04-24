import typing


class Calculate:
    def __init__(self, results: typing.List[float]):
        self.results = results
        self.best = max(results)
        self.worst = min(results)
        self.number_of_results = len(results)
        self.average = round(sum(results) / self.number_of_results, 1)


def convertToCalculateList(results: typing.List[typing.Dict[str,
                                                            typing.Union[str, typing.List[float]]]], err: typing.List[str]):
    calculatedResults: typing.List[typing.Tuple[str, Calculate]] = []
    for student in results:
        if len(student["results"]) > 0:
            calculatedResults.append(
            (student["name"], Calculate(student["results"])))
        else:
            err.append(f"student {student['name']} has no results")
    return calculatedResults