from datetime import datetime
import requests

USERNAME = "cesar96"
TOKEN = "akjashkdjhas1231231"
GRAPH1_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
}

# >>>>>>>>>>> Using requests.post to create user account <<<<<<<<<<<<<<<
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# >>>>>>>>>>> Create a graph definition <<<<<<<<<<<<<<<<

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": GRAPH1_ID,
#     "name": "Writing graph",
#     "unit": "Paragraphs",
#     "type": "int",
#     "color":"shibafu",
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

# >>>>>>>>>>>>>> Posting to the graph <<<<<<<<<<<<<<<<

graph_posting_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1_ID}"
todays_date = datetime.now()

graph_posting = {
    "date": todays_date.strftime("%Y%m%d"),
    "quantity": input("Quantos parágrafos escreveu hoje?\n"),
}

# graph_posting_response = requests.post(url=graph_posting_endpoint, json=graph_posting, headers=headers)
# print(graph_posting_response.text)

# >>>>>>>>>>>>>> Put requests to update the pixels in the graph <<<<<<<<<<<<<<<<<<<
date_to_be_edited = 20251405

pixel_editing_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1_ID}/{todays_date.strftime('%Y%m%d')}"

pixel_editing = {
    "quantity": "1"
}
#
# pixel_editing_response = requests.put(url=pixel_editing_endpoint, json=pixel_editing, headers=headers)
# print(pixel_editing_response.text)

# >>>>>>>>>>>>>> Delete Method to delet pixels <<<<<<<<<<<<<<<
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1_ID}/{todays_date.strftime('%Y%m%d')}"

pixel_deleting_response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(pixel_deleting_response.text)