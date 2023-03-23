import studentsResultsCSVReader

def main():
    results, err = (studentsResultsCSVReader.openStudentsResultsCSV("test.csv"))
    for result in results:
        print(result)
    for e in err:
        print(e)

if __name__ == "__main__":
    main()