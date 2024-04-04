from pprint import pprint

from courts.court_integration import CourtAndCase
from courts.mo.missouri import get_cases
from courts.mo.search_cases import search_cases

URL = 'https://www.courts.mo.gov/cnet/cases/newHeaderData.do?caseNumber=171155061&courtId=CT12&isTicket=&locnCode='


def print_cases(cases: list[any]):
    pprint(cases)


def scrap_court():
    # Use a breakpoint in the code line below to debug your script.
    cases = search_cases()
    pprint(cases)
    # cases = get_cases([CourtAndCase("CT16", "171155061")])
    # print_cases(cases)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scrap_court()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
