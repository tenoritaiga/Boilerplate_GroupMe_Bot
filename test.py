import requests

def get_quote(symbol,token):
    try:
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + token}
        url = "https://api.tdameritrade.com/v1/marketdata/"+symbol+"/quotes"
        r = requests.get(url,headers=headers)
        resp = r.json()[symbol]
        return resp['description'] + ' - Last price: ' + resp['lastPrice']
    except Exception as e:
        print("ERROR: {}".format(e))
    
token = """v0WHk50UyKM1tvBEO6GqG9m0ER7GDElfQkvZTIU7Mf2YTj1LavVDvWy1W1C5S2zSskJ43HfHQFcA/5l2L09cGmjrUtMYzeXEf0iCDVbDhqdTelAExNF8pNN69NPXqsViZSBx46vvdqmrwHmPqMFXym1Q0V9ZuPcR9KtfYWDvp2rnQBT3StG0OzZ3qcJXXQgDTybilDO5buOY5H+w8Xaph+J/P96nyvIqrAXr4nE6+JPn1CuPLWxR0fMw+iICPj81tU28WDyBoVsY0w5vd+mUFBd2Jqc2Rnosv7aQW8KA6cuRdy7v9tiecbAJCuVEK8VmznzVAiPEAPFIjFhelSOWea/Sh8WiDdBxI/fbwKml8G3JUYCmiRsdRf/ktFXLfPDWdMc9vtk+TxVUOpgC3oESXB4bl7l1avrfjqlTSJyVaeWCVQ8J1t63m2PbAPDRuUwY+qVoDEJapc9Q9mp1XTV/POTO6jF100MQuG4LYrgoVi/JHHvlSgD/4fpqGRxe+QMsMRBB0QYll/URuoylgLbEWsbord9nlOa4Zx42YG/TniVcPfxj236P+1qxpvBlrUuDLn9OBM0S/oLkLmGFYsH9Y0O73Z0Go59fM/CzHnu3KToVcsOGAHTpIZWF8aG7ZrCnpXiVlUBMMTswfolMrIsNVs6Q+J07Oyy9HPiSDEg1MNseH4iZBZhgPnYzgmRVSSzQUEzpioyMftWWRRcNT3iLKc4KTz2no698QRGxoVPnIOPuqE0OiYjlLftZ2jDERWkDh4X7v3ZpWe3OBG8XFLxc5W7TaZYtaBiyl/WkTfU5EvcCxsNVGl/P7MLVTRjGDszkPrmvuvodR86hsFe7rRkNYlHnPuxWrjP5ckvJ8rbwvpyRPrtMm7BstIr9QlIHbTgcWTwYfOxEK5LGB6si2Ums1twdTzT11fRPV9/l6+fdVHu/+iQtnOp6KIMMb61i+kDlh6ZCqn8pIss=212FD3x19z9sWBHDJACbC00B75E"""    
print(get_quote('AAPL',token))