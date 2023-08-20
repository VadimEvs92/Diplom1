
 # Евсеев Вадим Земля 7 - Финальный проект
import request


def test_return_status_code():

    order_response = request.get_order_track(request.track)

    assert order_response.status_code == 200

    if order_response.status_code == 200:
        print("Инфо получено")
    else:
        print("ERROR")
