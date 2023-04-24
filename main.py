import studentsResultsCSVReader
import calculate
import render
import webserver

def main():
    results, err = (studentsResultsCSVReader.openStudentsResultsCSV("test.csv"))
    calculatedResults = calculate.convertToCalculateList(results, err)
    html = render.render(calculatedResults, err)

if __name__ == "__main__":
    main()