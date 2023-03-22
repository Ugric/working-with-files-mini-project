import csv
import typing


def parseStudentsTable(students2DArray: typing.List[list]) -> (
        typing.Tuple[typing.List[typing.Dict[str, typing.Union[str, list]]], typing.List[str]]
                 ):
    errors: typing.List[str] = []
    titles = students2DArray[0]
    if "Student name" not in titles:
        errors.append(r"no 'Student name' column, so all students will be named 'unnamed student {x}'")
        StudentNameColumn = -1
    else:
        StudentNameColumn = titles.index("Student name")
    dataRows = students2DArray[1:]
    students: typing.List[typing.Dict[str, typing.Union[str, list]]] = []
    for i in range(len(dataRows)):
        student: typing.Dict[str, typing.Union[str, list]] = {
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
                    errors.append(
                        f"row {i + 2}, column {j + 1}: {student['name']}'s result for '{titles[j]}' not a number, so it was ignored")
        students.append(student)
    return students, errors

def openStudentsResultsCSV(path: str):
    csvfile = list(csv.reader(open(path, 'r')))
    return parseStudentsTable(csvfile)
