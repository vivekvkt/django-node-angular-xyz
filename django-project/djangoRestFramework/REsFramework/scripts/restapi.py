import json
import requests
import os

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/jwt-token/"
REFRESH_AUTH_ENDPOINT = AUTH_ENDPOINT + "jwt-refresh-token/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join(os.getcwd(), "vk.jpeg")


headers= {
    "Content-Type": "application/json"
}

data = {
    'username':'vivek',
    'password':'hellovivek'
}

r = requests.post(AUTH_ENDPOINT,data=json.dumps(data),headers=headers)
token = r.json()['token']
#print(token)



headers = {
    #"Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

with open(image_path, 'rb') as image:
    file_data = {
        'image': image
    }
    data = {
        "content": "update  some data ",
       
    }
    json_data = json.dumps(data)
    #posted_response = requests.post(ENDPOINT , data=data, headers=headers, files=file_data)
    posted_response = requests.put(ENDPOINT + str(26) + "/", data=data, headers=headers, files=file_data)
    #posted_response = requests.get(ENDPOINT)
    #print(posted_response.text)


headers = {
    #"Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

data = {
    "content": "Updated description"
}
json_data = json.dumps(data)
posted_response = requests.put(ENDPOINT + str(27) + "/", data=data, headers=headers)
print(posted_response.text)




# refresh_data = {
#     'token': token
# }

# new_response = requests.post(REFRESH_AUTH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()#['token']

# print(new_token)




# data = {
#     'username':'vivek',
#     'password':'hellovivek'
# }

# r = requests.post(AUTH_ENDPOINT,data=data)
# #print(r.json())

# token = r.json()['token']
# print(token)














# get_endpoint = ENDPOINT  + str(12)
# post_data =  json.dumps({"content":"some random content"})

# r = requests.get(get_endpoint)
# print(r.text)

# r2 = requests.get(ENDPOINT)
# print(r2.status_code)

# post_headers ={
#     'content_type':'application/json'
# }
# post_response = requests.post(ENDPOINT,data=post_data,headers = post_headers)
# print(post_response.text)





# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data = {
#                 'image': image
#             }
#             r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r



# do_img(
#     method='put', 
#     data={'id': 23, 'user': 1, "content": "Some new content"}, 
#     is_json=False, 
#     img_path=image_path
#     )





# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r



# do(data={'id': 500})

# do(method='delete', data={'id': 13})

# do(method='put', data={'id': 13, "content": "some cool new content", 'user': 1})

# do(method='post', data={"content": "some cool new content", 'user': 1})

# create
# retrieve / list
# update
# delete