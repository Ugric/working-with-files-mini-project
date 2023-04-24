import csv
import typing


def parseStudentsTable(students2DArray: typing.List[list]) -> (
    typing.Tuple[typing.List[typing.Dict[str,
                                         typing.Union[str, typing.List[float]]]], typing.List[str]]
):
    errors: typing.List[str] = []
    titles = students2DArray[0]
    if "Student name" not in titles:
        errors.append(
            r"no 'Student name' column, so all students will be named 'unnamed student {x}'")
        StudentNameColumn = -1
    else:
        StudentNameColumn = titles.index("Student name")
    dataRows = students2DArray[1:]
    students: typing.List[typing.Dict[str,
                                      typing.Union[str, typing.List[float]]]] = []
    for i in range(len(dataRows)):
        student: typing.Dict[str, typing.Union[str, typing.List[float]]] = {
            "name": f'unnamed student {i + 1}',
            "results": []
        }
        if StudentNameColumn != -1:
            student["name"] = dataRows[i][StudentNameColumn]
        for j in range(len(dataRows[i])):
            if j != StudentNameColumn:
                try:
                    student["results"].append(float(dataRows[i][j]))
                except ValueError:
                    pass
        students.append(student)
    return students, errors


def openStudentsResultsCSV(path: str):
    csvfile = list(csv.reader(open(path, 'r')))
    return parseStudentsTable(csvfile)
