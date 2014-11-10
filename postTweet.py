#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = 'DTfFCRDQGJKATAhJC2gg6MAUw'
CONSUMER_SECRET = 'PIpnAisRwtnWGAQbiL2UETAGAlp3eTY2p5qXuZea8Gwot8bWSe'
ACCESS_KEY = '59153514-bqnT1tCfyTseJSETFWMnWBIFfbiwt8WJR02l7LyPp'
ACCESS_SECRET = 'quYsjZP8BfhN6IKF3o5UZC31Gt2OH6qVorzZlWyUjNUMW'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])
