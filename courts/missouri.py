import requests


def get_case(case_id: str) -> dict:
    url = f'https://www.courts.mo.gov/cnet/cases/newHeaderData.do?caseNumber={case_id}&courtId=CT12&isTicket=&locnCode='
    return requests.get(url).json()
