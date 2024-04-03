from types import SimpleNamespace

import requests

from courts.court_integration import CourtAndCase




def _get_case(court_id: str, case_id: str) -> dict:
    url = f'https://www.courts.mo.gov/cnet/cases/party.do?caseNumber={case_id}&courtId=CT12&isTicket=&locnCode='
    return requests.get(url).json()


def get_case(court_and_case: CourtAndCase):
    return _get_case(court_id=court_and_case.court_id, case_id=court_and_case.case_id)


def get_cases(cases: list[CourtAndCase]) -> list[any]:
    return [SimpleNamespace(**dict_case) for dict_case in (get_case(case) for case in cases)]
