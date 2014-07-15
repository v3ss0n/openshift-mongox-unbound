import sys
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])


if __name__ == '__main__':
    temp_dir  = os.environ.get('OPENSHIFT_TMP_DIR')
    app_name = os.environ.get('OPENSHIFT_GEAR_NAME')
    host = os.environ.get('OPENSHIFT_DIY_IP')
    port = os.environ.get('OPENSHIFT_DIY_PORT')
    pid = str(os.getpid())
    pidfile = temp_dir +app_name + ".pid"
    file(pidfile, 'w').write(pid)
    application.listen(host,port)
    tornado.ioloop.IOLoop.instance().start() 
