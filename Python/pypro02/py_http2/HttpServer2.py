'''
SimpleHTTPRequestHandler를 확장한 CGIHTTPRequestHandler 사용
py 문서 내에서 html 태그를 기술
'''
from http.server import CGIHTTPRequestHandler, HTTPServer

port = 7777

class Handler(CGIHTTPRequestHandler):
    cg_directories = ['/cgi-bin']
    
serv = HTTPServer(('192.168.0.61', port), Handler)
print('웹 서비스 시작')
serv.serve_forever()
