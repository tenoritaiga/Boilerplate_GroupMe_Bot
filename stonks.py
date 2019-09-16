import requests

# https://developer.tdameritrade.com/authentication/apis/post/token-0
def getOauthToken():
    td_oauth_url = "https://api.tdameritrade.com/v1/oauth2/token"
    payload = {'grant_type':'authorization_code','code':}
    r = requests.get(td_oauth_url)



# Respond to stonks command
def stonks(stonk):
    try:
        td_url = "https://api.tdameritrade.com/v1/oauth2/token"