from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello':'world'}

api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
    app.run(host='218.51.230.215')


"""
이더넷 어댑터 로컬 영역 연결:
   연결별 DNS 접미사. . . . :
   링크-로컬 IPv6 주소 . . . . : fe80::e84c:feb7:1c63:5d9c%11
   IPv4 주소 . . . . . . . . . : 218.51.230.215 <- 이 주소
   서브넷 마스크 . . . . . . . : 255.255.255.0
   기본 게이트웨이 . . . . . . : 218.51.230.1
"""