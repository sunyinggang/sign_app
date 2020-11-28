import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.iai.v20200303 import iai_client, models

from app import app

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