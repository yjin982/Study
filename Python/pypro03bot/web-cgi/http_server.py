from http.server import CGIHTTPRequestHandler, HTTPServer
port = 8080

class Handler(CGIHTTPRequestHandler):
    cg_directories = ['cgi-bin']
    
serv = HTTPServer(('127.0.0.1', port), Handler)
print('챗봇 서버 서비스 중 ...')
serv.serve_forever()