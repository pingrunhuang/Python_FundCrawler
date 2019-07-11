import requests
import re
import datetime

current = datetime.datetime.now()
yesterday = str(current.month)+"-"+str(current.day-1)
today = str(current.month)+"-"+str(current.day)
timestamp = str(current.year)+str(current.month)+str(current.day)


index_url = 'http://fund.eastmoney.com/ZS_jzzzl.html#os_0;isall_0;ft_;pt_5'
HEADERS = {"User-Agent":r"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"}

response = requests.get(index_url, headers=HEADERS)
b_html = response.content
html = b_html.decode('gbk')

def split(content):
    funds = content.split('<td class="xh">')
    print(funds[1:2])

"""
<td class="xh">9</td>
<td class="bzdm">501105</td>
<td class="tol">
<nobr><a title="建信金融债8-10年(LOF)" href="http://fund.eastmoney.com/501105.html">
建信金融债8-10年(L</a>
<a href="http://fund.eastmoney.com/501105.html">估值图</a>
<a href="http://jijinba.eastmoney.com/topic,501105.html">基金吧</a>
</nobr></td>
<td class="dwjz black">1.1271</td>
<td class="ljjz black">1.1271</td>
<td class="dwjz black">1.1252</td>
<td class="ljjz black">1.1252</td>
<td class="rzzz  red">0.0019</td>
<td class="rzzl bg red">0.17%</td>
<td class="sgzt">开放</td>
<td class="shzt">开放</td>
<td><div class="yhfl"><div class="rate_f"><a class="zkf" href="http://fundf10.eastmoney.com/jjfl_501105.html">0.04%</a></div></div></td>

only keep the <div id="tableDiv"> part
"""

if __name__ == "__main__":
    with open(timestamp,'w') as f:
        f.write(html)