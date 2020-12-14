import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.iai.v20200303 import iai_client, models

from app import app

# teacher_face id:2
# student_face id:3

def create_group():
    try:
        cred = credential.Credential(app.config['TENCENT_SECRET_ID'], app.config['TENCENT_SECRET_KEY'])
        httpProfile = HttpProfile()
        httpProfile.endpoint = "iai.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = iai_client.IaiClient(cred, "ap-beijing", clientProfile)

        req = models.CreateGroupRequest()
        params = {
            "GroupName": "people_face",
            "GroupId": "1"
        }
        req.from_json_string(json.dumps(params))

        resp = client.CreateGroup(req)
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)


def add_person():
    try:
        cred = credential.Credential(app.config['TENCENT_SECRET_ID'], app.config['TENCENT_SECRET_KEY'])
        httpProfile = HttpProfile()
        httpProfile.endpoint = "iai.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = iai_client.IaiClient(cred, "ap-beijing", clientProfile)

        req = models.CreatePersonRequest()
        params = {
            "GroupId": "1",
            "PersonName": "孙迎港测试",
            "PersonId": "1",
            "Url": "https://face-1253387449.cos.ap-beijing.myqcloud.com/sun1.jpg"
        }
        req.from_json_string(json.dumps(params))

        resp = client.CreatePerson(req)
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)

def search_face(info):
    #info{group_id,image}
    try:
        cred = credential.Credential(app.config['TENCENT_SECRET_ID'], app.config['TENCENT_SECRET_KEY'])
        httpProfile = HttpProfile()
        httpProfile.endpoint = "iai.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = iai_client.IaiClient(cred, "ap-beijing", clientProfile)

        req = models.SearchFacesRequest()
        params = {
            "GroupIds": info["group_id"],
            "Image": info["image"]
        }
        req.from_json_string(json.dumps(params))

        resp = client.SearchFaces(req)
        return resp.to_json_string()

    except TencentCloudSDKException as err:
        print(err)



if __name__ == '__main__':
    add_person()