import requests
from requests import post

session = None


def _maybe_setup_session():
    global session
    if session is None:
        session = requests.session()
    session.get("https://www.courts.mo.gov/cnet/searchResult.do")


def search_cases():
    global session
    # _maybe_setup_session()

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': f'JSESSIONID=00018AyD23UHxgAHrkgrArPuQsz:-1PCB'
    }

    json_data = {
        'draw': 1,
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

    response = requests.post('https://www.courts.mo.gov/cnet/searchResult.do', headers=headers, json=json_data).json()
    return response
