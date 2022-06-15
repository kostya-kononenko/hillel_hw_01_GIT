def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page_1?password=123456&login=hello') == {'password': '123456', 'login': 'hello'}
    assert parse('https://example.com/path/to/page_2?age=30') == {'age': '30'}
    assert parse('https://example.com/path/to/page_3?city=Kiev') == {'city': 'Kiev'}
    assert parse('https://example.com/path/to/page_4?street=Khreshchatyk') == {'street': 'Khreshchatyk'}
    assert parse('https://example.com/path/to/page_5?number_house=8A') == {'number_house': '8A'}
    assert parse('https://example.com/path/to/page_6?number_flat=42') == {'number_flat': '42'}
    assert parse('https://example.com/path/to/page_7?credit_card_number=5265585987451231') == {'credit_card_number': '5265585987451231'}
    assert parse('https://example.com/path/to/page_8?validity_month=12&validity_year=2026') == {'validity_month': '12', "validity_year": "2026"}
    assert parse('https://example.com/path/to/page_9?CVV=232') == {'CVV': '232'}
    assert parse('https://example.com/path/to/page_10?poscode=326548') == {'poscode': '326548'}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
