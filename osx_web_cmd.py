
from subprocess import call
from bottle import route, run, template, redirect
from sh import df, ps, pmset, sw_vers, ifconfig, hostinfo

SUSPEND = '/System/Library/CoreServices/Menu\\ Extras/User.menu/Contents/Resources/CGSession -suspend'

TEXTPAGE = """
<html>
<head>
<title>OSX Web cmd {{title}}</title>
<meta name="viewport" content="width=device-width, user-scalable=yes"/>
</head>
<body style="font-family:monospace;">
<a href="/">Home</a>
<pre>
{{text}}
</pre>
<a href="/">Home</a>
</body>
</html>"""

HOME = """
<html>
<head>
<title>OSX Web cmd Home</title>
<meta name="viewport" content="width=device-width, user-scalable=yes"/>
</head>
<body style="font-family:monospace;">
<a href="lockscreen">Lock the OSX Screen</a><br/><br/>
<a href="pmset/displaysleepnow">Sleep the OSX Screen</a><br/><br/>
<a href="pmset/sleepnow">Sleep the OSX Computer</a><br/><br/><br/><br/>
<a href="command/df">df -h</a><br/><br/>
<a href="command/hostinfo">hostinfo</a><br/><br/>
<a href="command/ifconfig">ifconfig</a><br/><br/>
<a href="command/ps">ps -ef</a><br/><br/>
<a href="command/sw_vers">sw_vers</a><br/>
</body>
</html>"""

@route('/')
def home():
    return HOME

@route('/lockscreen')
def _lockscreen():
    try:
        call(SUSPEND, shell=True)
        return template(TEXTPAGE, title='Locked Screen', text='Locked Screen')
    except:
        return template(TEXTPAGE, title='Failed to Lock Screen', text='Failed to Lock Screen')

@route('/pmset/<cmd>')
def _pmset(cmd=''):
    if cmd in ('displaysleepnow', 'sleepnow'):
        try:
            pmset(cmd)
            cmd_text = 'pmset {0} Success'.format(cmd)
        except:
            cmd_text = 'pmset {0} Failed'.format(cmd)
        finally:
            return template(TEXTPAGE, title=cmd_text.upper(), text=cmd_text)
    else:
        redirect('/')

@route('/command/<cmd>')
def _command(cmd=''):
    if cmd == 'df':
        result = df('-h')
    elif cmd == 'ps':
        result = ps('-ef', _tty_out=False)
    elif cmd == 'ifconfig':
        result = ifconfig()
    elif cmd == 'hostinfo':
        result = hostinfo()
    elif cmd == 'sw_vers':
        result = sw_vers()    
    else:
        redirect('/')
    return template(TEXTPAGE, title=cmd.upper(), text=result)

run(host='0.0.0.0', port=8080, quiet=True)
