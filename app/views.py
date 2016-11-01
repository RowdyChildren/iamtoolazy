from app import app
from flask import render_template,request
import json
import subprocess as sub

@app.route('/')
@app.route('/index')
def index():
    title = "test"
    switches = read_switches()
    print(switches)
    return render_template("index.html", title=title, switches=switches)

@app.route('/off')
def switch_off():
    network_id = request.args.get('netid')
    print("toggling {}".format(network_id))
    sub.call('hacklet off -n {} -s 0'.format(network_id), shell=True)
    sub.call('hacklet off -n {} -s 1'.format(network_id), shell=True)
    return index()

@app.route('/on')
def switch_on():
    network_id = request.args.get('netid')
    print("toggling {}".format(network_id))
    sub.call('hacklet on -n {} -s 0'.format(network_id), shell=True)
    sub.call('hacklet on -n {} -s 1'.format(network_id), shell=True)
    return index()

def read_switches():
    switch_file = open("data/switches.json")
    switches = json.load(switch_file)
    return switches
    
