# -*- coding: utf-8 -*-

"""
    [Quickstart](https://docs.python-eve.org/en/stable/quickstart.html)
    ~~~~~~~~~~~~~~~~~

    1. Testing CLI Commands
        - read 
            - `curl -i http://your.hostname.com:5000`
            - `curl -i http://your.hostname.com:5000/people` OR `curl -i http://your.hostname.com:5000/people?pretty`
            - `curl -i http://your.hostname.com:5000/people/obama`
        - write
            - `curl -i -d '[{"firstname": "barack", "lastname": "obama"}, {"firstname": "mitt", "lastname": "romney"}]' -H 'Content-Type: application/json' http://your.hostname.com:5000/people`
        - filtering
            - `curl -i http://your.hostname.com:5000/people?where={%22lastname%22:%20%22Doe%22}`
            - `curl -i -g http://your.hostname.com:5000/people?where={"lastname": "Doe"}`
        - sorting 
            - browser: `http://your.hostname.com:5000/people?sort=[("lastname", -1)]`
"""

from eve import Eve
app = Eve()

if __name__ == '__main__':

    # development env.
    app.run(debug = True, host="0.0.0.0")

    # production env.
    #app.run(host="0.0.0.0")
