import subprocess
import http.client

def lambda_handler(event, context):
    c = http.client.HTTPSConnection("raw.githubusercontent.com")
    c.request("GET", "/radix/planet-if/master/planet-if.conf")
    conf = c.getresponse().read().decode('utf-8')
    with open('/tmp/planet-if.conf', 'w') as f:
        f.write(conf)
    cmd = ['python', 'venus/planet.py', '/tmp/planet-if.conf']
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode('utf-8').split('\n')
    except subprocess.CalledProcessError as e:
        print(e.output)
        raise
    print("OK!")
