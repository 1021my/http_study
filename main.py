from socket import *
import requests

#소켓 객체 생성
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
#동시 접속 허용 갯수
serverSock.listen(1)

#접속 허용
connectionSock, addr = serverSock.accept()

#받기 소켓에서 1024바이트만큼을 가져옴
data = connectionSock.recv(1024)
requested_http_message = data.decode('utf-8')
print('받은 데이터 : ', data.decode('utf-8'))

#url일 때
'''
indeed_url = "http://"
indeed_result = requests.get(indeed_url)

print(indeed_result.text)
'''
method = ""; query_string = ""; path = ""

# requested_http_message -> 이 변수를 분석 하는것
massage = requested_http_message.split('\r\n')
line1 = massage[0]
if 'HTTP/1.1'in line1:
    version = "HTTP/1.1"
if 'GET' in line1:
    f = open('C:/Users/JMY/Desktop/index.html')
    r = f.read()
    r=r.replace("\n", "")
    length= len(r)
    method = "GET"
    path = "C:/Users/JMY/Desktop/index.html"
    res_http_message = """
    {version} 200 OK
    context-type = text/html
    date = 
    content-length = {length}

    method = {method}
    path = {path}
    query_string = {query_string}
    {r}
    """.format(version=version,length=length,method=method,
               path=path,query_string=query_string, r=r)

#보내기 encode() 메소드는 문자열을 byte로 변환
connectionSock.send(res_http_message.encode('utf-8'))