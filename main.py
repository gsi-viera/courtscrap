from pprint import pprint
from types import SimpleNamespace

from courts.missouri import get_case

URL = 'https://www.courts.mo.gov/cnet/cases/newHeaderData.do?caseNumber=171155061&courtId=CT12&isTicket=&locnCode='


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_cases() -> list[any]:
    return [SimpleNamespace(**get_case("171155061"))]


def print_cases(cases: list[any]):
    pprint(cases)


def scrap_court():
    # Use a breakpoint in the code line below to debug your script.
    cases = get_cases()
    print_cases(cases)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scrap_court()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
