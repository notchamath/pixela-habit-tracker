import requests

from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "notchamath"

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_id = "readingtracker"
headers = {
    "X-USER-TOKEN": PW,
}


# ************************* Create User ****************************
# user_params = {
#     "token": PW,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# res = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(res.text)


# ************************* Create Graph ****************************
#
# graph_config = {
#     "id": graph_id,
#     "name": "Reading Tracker",
#     "unit": "pages",
#     "type": "int",
#     "color": "momiji",
# }
#
# res = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(res.text)


# ************************* Add Pixels to Graph ****************************
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{graph_id}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "6",
}
res = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)
print(res.text)
