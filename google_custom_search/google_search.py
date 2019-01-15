def hujambo():
    print('''
#####################################################
# Tool    : Google Custom Search (using Google API) #
# Version : 1.0                                     #
# Source  : https://github.com/pr2h/                #
# Coded with Python 3.7.2                           #
#####################################################
    ''')

import urllib
import requests
import json
# For supressing warning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def gsearch():
  # API key can be created from "http://code.google.com/apis/console"
  key = "<ENTER_KEY_HERE>"
  # cx (Control Panel) value can be generated from "https://cse.google.com/all"
  cx = "<ENTER_CX_HERE>"
  
  # Search query
  searchquery = "<ENTER_SEARCH_QUERY_HERE>"
  searchquery = urllib.parse.quote_plus(searchquery)

  # URL Source: https://developers.google.com/custom-search/v1/using_rest
  URL = "https://www.googleapis.com/customsearch/v1?key="+key+"&cx="+cx+"&q="+searchquery
  # Obtaining search results
  response = requests.get(URL, verify = False).content

  # Displaying search results
  print("\n\n[*] Response as bytes:\n")
  print(response)

  print("\n\n[*] Response in dictionary:\n")
  response_as_dictionary = json.loads(response)
  print(response_as_dictionary)

  # Returning appropriate response
  return(response_as_dictionary)

if __name__ == '__main__':
  # Welcome function
  hujambo()
  # Google search main code
  response = gsearch()
