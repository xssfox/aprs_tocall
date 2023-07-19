#def lookup_online():
import yaml
import os
import re
import urllib.request

class Parser():
    def __init__(self, offline=True):
        if offline:
            stream = open(f'{os.path.dirname(__file__)}/tocalls.yaml', 'r')
        else:
            stream = urllib.request.urlopen('https://raw.githubusercontent.com/aprsorg/aprs-deviceid/main/tocalls.yaml')
        self.data = yaml.safe_load(stream)
        stream.close()
    def return_data(self, data): # so we can format data in a standard way
        del data['specific_count']
        return data   
    def lookup(self,call):
        # always check in upper
        call = call.upper()
        #check wildcard matches starting from most specific
        matches = []
        for matching_call in self.data['tocalls']: # loop through all calls in tocalls.txt
            matcher = matching_call['tocall']
            matcher = matcher.replace("?",'\w')
            matcher = matcher.replace("n",'\d')
            matcher = matcher.replace("*",'\w')
            if re.match(matcher, call):
                matched = matching_call
                specific_count = matching_call['tocall'].count("n") + matching_call['tocall'].count("?") + matching_call['tocall'].count("*")
                matched["specific_count"] = specific_count
                matches.append(matched)
        # try to get the most specific
        matches = sorted(matches, key=lambda d: d['specific_count']) 
        if matches:
            return self.return_data(matches[0])
        raise IndexError("Not found in tocalls.yaml")