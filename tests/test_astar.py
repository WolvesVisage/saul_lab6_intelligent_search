from lab6_intelligent_search.services.search_service import find_route

def test_astar_route():
    result = find_route('A', 'F')

    assert result['cost'] == 7
    assert result['path'][0] == 'A' and result['path'][-1] == 'F'
