#!/bin/sh
zip lambda.zip -x '*.pyc' '*.tmplc' -r venus/planet.py venus/planet lambda.py templates
