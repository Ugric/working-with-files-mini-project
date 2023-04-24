import jinja2
import typing
import calculate

templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template("results.html")

def render(studentsResults: typing.List[typing.Tuple[str, calculate.Calculate]], errors: typing.List[str]):
    outputText = template.render(studentsResults=studentsResults, errors=errors)
    return outputText