#-*- coding: utf-8 -*-
from flask import Flask, g, request, Response, make_response, session
from flask import render_template, jsonify
from datetime import datetime, date, timedelta

app = Flask(__name__)
app.debug = True
app.config['SERVER_NAME'] = 'localhost:5000'
#app.jinja_env.trim_blocks = True
app.config.update(
    SECRET_KEY='X1234yRH1lkjdfal',
    SESSION_COOKIE_NAME='pyweb_flask_session',
    PERMANENT_SESSION_LIFETIME=timedelta(31)
)


#################### html ################
@app.route("/tmp1")
def tmp1():
    #templates directory 는 flask가 설정해둬서 바로 불러도 됨
    return render_template('index.html', title="Title")


########## Request Event Handler ##########
#web filter(euc-kr이 들어오면 utf-8로 변경한다던가)
@app.before_request
def before_request():
    print("before_request!!!")
    g.str = "한글"  #g는 application Context의 영역

@app.before_first_request
def before_first_request():
    print("before_first_request")

#db close 같은거 매번 해야할때
# @app.after_request
# def after_request(response):
#     print("after_request response")

#destroy
@app.teardown_request
def teardown_request(exception):
    print("teardown_request exception", "None" if exception == None else exception)

#applicationContext가 끝났을때
@app.teardown_appcontext
def teardown_appcontext(exception):
    print("teardown_appcontext exception", "None" if exception == None else exception)


########## Routing ##########
#@app.route('/test', methods=['POST', 'PUT'])
#def ...

#URI에 param을 받았을 경우 ex) /test/param(tid)
# @app.route('test/<tid>')
# def test3(tid):
#     print("tid is", tid)

# @app.route('/test', defaults={'page': 'index'})
# @app.route('/test/<page>')
# def xxx(page):

#입력 도매인에 따라 다른 page
# @app.route('/test', host='abc.com')

# @app.route('/test', redirect_to='/new_test')
################################

########## subdomain ##########
#http://g.localhost:5000/sub
@app.route("/sub")
def hellowwrld_local():
    return "Hello Local.com!"

@app.route("/sub", subdomain="g")
def helloworldSubG():
    return "Hello G.Local.com!"

################################


########## Request Parameter ##########
#MultiDict Type
#methods: get, getlist, clear, etc
#get('param name', default-value, type)
@app.route('/rp')
def rp():
    #unicode -> str
    # q = request.args.get('q').encode('utf8')
    # print("JJ", type(q))
    # return "q= %s" % q

    #rp?q=한글&q=English
    q = request.args.getlist('q')
    sss = ', '.join([s.encode('utf8') for s in q])
    return "q= %s" % sss


# GET
#request.args.get('q')

# POST
#request.form.get('p', 123)

#GET or POST
#request.values.get('v')

#Parameters
#request.args.getlist('qs')
################################



########## Request Parameter Custom Function Type ##########

#from datetime import datetime, date
def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans

@app.route('/dt')
def dt():
    #ymd() 는 trans()로 치환 된 후 date값을 trans의 인자로 넘김
    #JComent : A값에 B,C,D로 어쩌구 저쩌구 할때 사용하면 된다. date값을 fmt값으로 전환
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    ustr = u"우리나라 시간 형식: ".encode('utf8') + str(datestr)
    return ustr
################################



########## request.environ ##########
# @app.route('/reqenv')
# def reqenv():
#     return ('REQUEST_METHOD: %(REQUEST_METHOD) s <br>' #request.environ['REQUEST_METHOD']
#         'SCRIPT_NAME: %(SCRIPT_NAME) s <br>'
#         'PATH_INFO: %(PATH_INFO s <br>'
#         'QUERY_STRING: %(QUERY_STRING) s <br>'
#         'SERVER_NAME: %(SERVER_NAME) s <br>'
#         'SERVER_PORT: %(SERVER_PORT) s <br>'
#         'SERVER_PROTOCOL: %(SERVER_PROTOCOL) s <br>'
#         'wsgi.version: %(wsgi.version) s <br>'
#         'wsgi.url_scheme: %s(wsgi.url_scheme) s <br>'
#         'wsgi.input: %(wsgi.input) s <br>'
#         'wsig.errors: %(wsgi.errors) s <br>'
#         'wsgi.multithread: %(wsgi.multithread) s <br>'
#         'wsgi.multiprocess: %(wsgi.multiprocess) s <br>'
#         'wsgi.run_once: %(wsgi.run_once) s') % request.environ
################################


########## request ##########
# request.is_xhr #ajax 로 호출했는지?
# request.endporint #내 uri
# request.get_json() #ajax로 불렀을때 & body type이 json인 data(json)을 준다
# app.config.update(MAX_CONTENT_LENGTH=1024*1024) #편지지에 쓸 수 있는 최대 BYTE
# request.max_content_length #현재 max_content_length 크기
################################

########## response object ##########
# Response attributes
# -headers
# -status
# -status_code
# -data
# -mimetype

# ex)
# res = Response("Test")
# res.headers.add('Program-Name','Test Response')
# res.set_Data("This is Test Program.")
# res.set_cookie("UserToken", "A12Bc9")

################################


########## cookie ##########
#Cookie __init__ Arguments
# - key
# - value
# - max_age -> 기간을 줌 1day
# - expires -> 오늘밤 12시 date를 줌
# - domain
# - path

# ex)
# res = Response("Test")
# res.set_cookie("UserToken", "A123Bc0")

# #other request
# request.cookieis.get("UserToken", "default_token")

#http://localhost:5000/writecookie?key=token&val=abcabc
#f12 application cookie에서 확인
@app.route('/writecookie')
def writecookie():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response("SET COOKIE")
    res.set_cookie(key, val)
    session['Token'] = '123X'
    return make_response(res)

#http://localhost:5000/readcookie?key=token
@app.route('/readcookie')
def readcookie():
    key = request.args.get('key')
    print(type(key), "key")
    val = request.cookies.get(key)
    print(type(val), "val")
    return "cookie[" + key + "]=" + val + " , " + session.get('Token')

################################


#################### session ####################
# from flask import session
# app.secret_key ='X1234yRH1lkjdfal'
# or
# app.config.update(
#     SECRET_KEY='X1234yRH1lkjdfal',
#     SESSION_COOKIE_NAME='pyweb_flask_session',
#     PERMANENT_SESSION_LIFETIME=timedelta(31) #31 days
# )

#Save to Memory, file or DB

@app.route('/setsess')
def setsess():
    session['Token'] = '123X'
    return u"Session이 설정되었습니다!".encode('utf8')

@app.route('/getsess')
def getsess():
    return session.get('Token')

@app.route('/delsess')
def delsess():
    if session.get('Token'):
        del session['Token']
    return u"Session이 삭제되었습니다.".encode('utf8')

################################################################


@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [ ('Content-Type', 'text/plain'),
                    ('Content-Lengh', str(len(body)))]
        start_response('200 OK', headers)
        return [body]

    return make_response(application)


@app.route("/res1")
def res1():
    #header에 test:ttt가 추가됨
    custom_res = Response("Custom Response", 200, {'test': 'ttt'})
    return make_response(custom_res)


@app.route("/res2")
def res2():
    return make_response("custom response")


@app.route("/gg")
def helloworld2():
    return "Hello Flask World!" + getattr(g, 'str', 'default 111')

@app.route("/")
def helloworld():
    return "Hello Flask World!"





