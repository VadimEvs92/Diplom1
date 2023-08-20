import configuration
import requests
import data


def post_new_order(body):
      return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                          json=body)
response = post_new_order(data.order_body)
track = response.json()["track"]
print(response.json())
print(response.status_code)


def get_order_track(track):

     return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK, params={"t": track})
response = get_order_track(track)
print(response.json())
print(response.status_code)

