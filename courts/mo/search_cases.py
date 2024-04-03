import requests


def create_search():
    session = requests.session()
    session.get(
        "https://www.courts.mo.gov/cnet/searchResult.do?countyCode=WRN&newSearch=Y&courtCode=CT12&startDate=03%2F24"
        "%2F2024&caseStatus=A&caseType=Traffic%2FMunicipal")
    return session


def search_cases():
    session = create_search()

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/json;charset=UTF-8',
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

    response = session.post('https://www.courts.mo.gov/cnet/searchResult.do', headers=headers, json=json_data).json()
    return response
