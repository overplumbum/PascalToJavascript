from pparser import render
from glob import glob
from zipfile import ZipFile
from ConfigParser import ConfigParser

plugins = []
for fn in glob(r'maps/*.zmp'):
    print "handling", fn, ":"
    
    f = ZipFile(fn, 'r')

    print "Parsing ini"
    config = ConfigParser()
    config.readfp(f.open('params.txt', 'r'))
    params  = config.items('PARAMS')
    params = [(k, v.decode('cp1251')) for k, v in params]

    print "Converting pascal to js"
    js = render(f.open('GetUrlScript.txt', 'r').read().decode('windows-1251')) 
    params.append(('GetUrlScript', js))
    
    w = open('js/' + fn + '.js', 'w')
    js = """
// test input data
geturlbase = 'http://geturlbase.se/';
getz = 10;
gety = 20;
getx = 30;
getllon = 40;
getrlon = 50;
getblat = 60;
gettlat = 70;

// pascal functions emulation
copy = function(s, from1, len) { return s.substr(from1-1, len); };
external = function(dllfunc) { return 80; }
pi = Math.PI;
length = function(s) { return s.length; }
insert = function(ins, str, pos1) { return str.substr(0, pos1-1) + ins + str.substr(pos1-1+ins.length); }

""".lstrip() + js + """
console.log(resulturl);
"""
    w.write(js)
    w.close()
    
    f.close()
    params = dict(params)

    plugins.append(params)
    
from json import dumps
print dumps(plugins)