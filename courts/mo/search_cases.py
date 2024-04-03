from dataclasses import dataclass, asdict
from types import SimpleNamespace
from typing import Optional

import requests
import urllib


@dataclass
class CaseSearchParams:
    newSearch: Optional[str] = None
    courtCode: Optional[str] = None
    startDate: Optional[str] = None
    caseType: Optional[str] = None
    caseStatus: Optional[str] = None
    countyCode: Optional[str] = None


def create_search(params: CaseSearchParams):
    session = requests.session()
    params_dict = asdict(params, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})
    url_params = urllib.parse.urlencode(
        params_dict
    )
    _ = session.get(f"https://www.courts.mo.gov/cnet/searchResult.do?{url_params}")
    return session


def search_cases():
    params = CaseSearchParams(
        newSearch="Y",
        courtCode="CT12",
        startDate="03/24/2024",
        caseStatus="A",
        caseType="Traffic/Municipal",
        # countyCode="WRN"
    )
    session = create_search(params)
    response = get_search_results(session, draw=1)
    count = response.recordsTotal
    records = response.data
    while len(records) < count:
        response = get_search_results(session, draw=response.draw + 1)
        records.extend(response.data)
    return records


def get_search_results(session: any, draw: int):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/json;charset=UTF-8',
    }
    json_data = {
        'draw': draw,
        'columns': [
            {
                'data': 0,
                'name': '',
                'searchable': True,
                'orderable': True,
                'search': {
                    'value': '',
                    'regex': False,
                },
            },
            {
                'data': 'initFiling',
                'name': '',
                'searchable': True,
                'orderable': True,
                'search': {
                    'value': '',
                    'regex': False,
                },
            },
            {
                'data': 'caseNumber',
                'name': '',
                'searchable': True,
                'orderable': True,
                'search': {
                    'value': '',
                    'regex': False,
                },
            },
            {
                'data': 'caseStyle',
                'name': '',
                'searchable': True,
                'orderable': True,
                'search': {
                    'value': '',
                    'regex': False,
                },
            },
            {
                'data': 'caseType',
                'name': '',
                'searchable': True,
                'orderable': True,
                'search': {
                    'value': '',
                    'regex': False,
                },
            },
            {
                'data': 'countyDesc',
                'name': '',
                'searchable': True,
                'orderable': True,
                'search': {
                    'value': '',
                    'regex': False,
                },
            },
        ],
        'order': [
            {
                'column': 0,
                'dir': 'asc',
            },
        ],
        'start': 0,
        'length': 10,
        'search': {
            'value': '',
            'regex': False,
        },
    }
    response = session.post('https://www.courts.mo.gov/cnet/searchResult.do', headers=headers, json=json_data).json()
    return SimpleNamespace(**response)
