import subprocess
import http.client

def lambda_handler(event, context):
    c = http.client.HTTPSConnection("raw.githubusercontent.com")
    c.request("GET", "/radix/planet-if/master/planet-if.conf")
    conf = c.getresponse().read().decode('utf-8')
    with open('/tmp/planet-if.conf', 'w') as f:
        f.write(conf)
    return subprocess.check_output(['python', 'venus/planet.py', '/tmp/planet-if.conf']).decode('utf-8').split('\n')

