import configparser
import re

import requests
from bs4 import BeautifulSoup
from idna import unicode
from pymongo import MongoClient
from fake_useragent import UserAgent



alists = []
tlists = []
azipt = []

def book_label_spider():
    ua = UserAgent()
    print(ua.chrome)
    config = configparser.RawConfigParser()
    config.read("cookie.conf")
    Cookie=config['Cookie']['cookie']
    # #Cookie='acw_tc=276aede515746601737068163e3ae844c6090617d427845a03b064a9d119fa; acw_sc__v2=5ddb7a98fe1386ee06c0cae25c614c02c9c80647; XSRF-TOKEN=eyJpdiI6InZzS1wvYkVsRWxaSFJFQW5udFh5a1dBPT0iLCJ2YWx1ZSI6IlBacVI5WDBnUTdLQ2tRUEp5ZGV4NFU1ZmQrWUNiXC96ZGtOMkVcL3Azdzhwd21iZ2ROYmMrQnhoMng4NnM3Z3d2bCIsIm1hYyI6IjliNGZiNjEwMzFlOWExNzRjNmViZTNiYzFmZjY2ZTk5Yzg4MzBkZWU1NWZjMjAyODIwNDJkYjkxMzEwNGU4NmUifQ%3D%3D; laravel_session=eyJpdiI6IkR4MjZyWkZEUHFaTFdocEs1eUpTWmc9PSIsInZhbHVlIjoiSHFzTXpMd1FmVmRQZ3JOKzBKTk1zRFBTV0ZLRVI3Y083RG5OM0thUlNzV29Qdit5dkpVZTlLUk1sSFYrMEgxbSIsIm1hYyI6IjE4ZGEzZTZkMzg0NDRhYmI5OWNhMzQxZDg2ZjU3Y2U4NGIxNTQyNGY5OGZkY2M0ZGI1MmY1NmQxZWUxOWQ0OTYifQ%3D%3D; GwWNJx8BBODucBOvyrYeNtNba7m8t9Yc3UGqp8Jw=eyJpdiI6IkUrWUQwdUh6TmhMVE55VnAxZFVaS1E9PSIsInZhbHVlIjoiRmRlb2IrR0daeHBVYlVHZzVETno4OUNweHQyZTJjN2IwdTQycHRsNUpUblVOVDBcL1NzNDBPTVhRR3ZMZkZnWmRWdXBQb1BoYjFySjd4TEJtMzFIQWM3dGJQSUQ4eUlPdDl3aFdlZTIwRXFxR1NlUmNTelNoamlrQnFFSkFDcVhwQnVpZHBUWmJmVGlBakE5ZFo3bXhLSWQ2XC9HcytOM3E1MUx6dkpscVA2RGl0TFwvRmZuTVwvREE3cmFObFBleXZnQ1pPb0hBUVZKdU9Qc1wvdDBaNnY1M3pTSTdZdVc1WEJJRFwvTFptckFoZ2g1Q2libnNHZnNsTDlPbW9SZW1RN0FibmE1XC9uTDVjVGxFM0lTUzcyXC9TMzhLZnFuTFwvTEl3U1l2Nm14WVVKM2RVbjFXVERlbmJGcWVTS3FJdm9qM3dkSU02Z2hZbmdCblwvMFdRXC9Mc05CaGxvVEszcGg5XC9CY3FUbXNMRkZpQ2JZR1dYSUNxMHdOVWRMa01BVldiNGxRV0V3Tm1mU0hDZlVQNDdyUTRQeWhDVXVkdz09IiwibWFjIjoiZWVjNTc5ZGRjZGQ1MzVkZDBhNmM0ZWQ2NTg1Y2Y4MzgwOWY1OWE5OTRkYTBhYzg1M2Y0ZGZlNWU4NzcwYzU0NiJ9; _ga=GA1.2.1837741689.1574660177; _gid=GA1.2.546554535.1574660177; _gat=1; _globalGA=GA1.2.1069284513.1574660177; _globalGA_gid=GA1.2.125608325.1574660177; _gat_globalGA=1; intercom-id-yttqkdli=60b49d6d-1c63-414a-87d0-df25e3be5c6d'
    url = 'https://btc.com/0000000000000000000d71c818dc4099c35c8980e8c43bd128cdb07731a8a457?page=1&order_by=tx_block_idx&asc=1'
    # #Cookie='276aede515746601737068163e3ae844c6090617d427845a03b064a9d119fa; acw_sc__v2=5ddb7a98fe1386ee06c0cae25c614c02c9c80647;XSRF-TOKEN=eyJpdiI6Inc1dnM2c2F2amUxRHpTQ0FiQU9XS0E9PSIsInZhbHVlIjoiNithU1lVRzVrOTFlRXJ6d0I1YVljYitxaXZXZjI3XC9EMTIyektwaXl1UDJcL0Z1UkM3bEI0RlplQWFRc2hNUW1yIiwibWFjIjoiNzNjYzA0NzM0Mjk2ODQyZTNiZTQxNTFlY2Y3NDk4MDE2ZmRlM2EzMGMzYTMyZTc0NzhhNjA0ZWI3NDViYjg0MSJ9; expires=Mon, 25-Nov-2019 08:58:12 GMT; Max-Age=7200; path=/, laravel_session=eyJpdiI6InFjUVQ1ZDFFSUNOVzdtVGpIMG5JWXc9PSIsInZhbHVlIjoiVnhSUStsZVdEdks1eXBcLytBRkJ3dG5INUwxTWlNbzBUTHBTQU1UdXZHM2xWVm9IRUpSUzFxOTc5cERaQ1dzXC9UIiwibWFjIjoiY2YzMTE4YzdjNjc4NzFmZWViMmE4MzhiMjc1YTA2NzE1ZGRkY2IxYjQyODI2YTUxNTExODIxYzM4YjQzYTQ5ZCJ9; expires=Mon, 25-Nov-2019 08:58:12 GMT; Max-Age=7200; path=/; httponly, GwWNJx8BBODucBOvyrYeNtNba7m8t9Yc3UGqp8Jw=eyJpdiI6IlwvazJZYWFBcGJ6bVh0YzVXSFNzaWdnPT0iLCJ2YWx1ZSI6IlZ0RnhRTWF4OTlmSjRCcHBucnBIQUh0TjVySzFTU2JkZktJTlB5MFg3RXZRZmZVQ282c2JCYUViVTFIXC8xb0tiZVJlVk14c3Vjb1lnOE9UQVkza29HSUdiRFJseG1aWVFXZkpZeTZlYmFVbVpUV2xyclFodFdWRGZzK2cySEFTT2syMDFKcGUyYkl0MDhKUnE0VXAyZU42djVtRitic216eWVicDFEbG41bFFmYXo0bW1TYTdvUUNRRk4xNHgxVkxEWVllSTkyYzJURmhHNHpNR2lMSVB6QmN0THJjUHE1aVRQRWp0ZXpTT016eFdQak5EQllCZ3BrbkZxdkR0U1J4c211ZzVDbE1IUGg3WDJCWDRLSGdxem5ZeGFwek5DVkx4Y0NFeE9RZWx4T2wyelJWb2NXRTBVZTVpK3EzZlZrSmZYUDVqMjVURGx6dmFzMThoRkZIVDVjZFFUVmtHVE1XWENDT1RxbkVHY2xtRklKbVhYTGVcL1lrbUQ5ZGQ5cWdJSW5mYXg3S0g4Yms5SUUwVWtiRXRyaDZCWlFTa1lhS1pMdHNOTGxjVURIT3U2UWk5QW1TVXlEaFM0THdIa0grUSIsIm1hYyI6ImM0ZjAyOGJmN2JiOTdmYTA0M2VjNTZjMDU4NzkwZjRiZGMwZWI4MWFhZjU3ZDYzZGVjZmQ3YWY1M2IyNDUzNjMifQ%3D%3D; expires=Mon, 25-Nov-2019 08:58:12 GMT; Max-Age=7200; path=/; httponly,XSRF-TOKEN=eyJpdiI6InlZTm1peFhmY2N0WFwvSGRRXC9nVitjdz09IiwidmFsdWUiOiI5SVwvdmV3azhzcnQ4cnA3NlI4b1JwTG5FZUtsSVBySXRIWWFKTWNmRTVQXC9KcVwvME9iUVdydFVLcXZLQVl2eU00IiwibWFjIjoiNzY5ODQ3ZDk5NTU1ZGI1OGQwMjJlZDI0NGM5NjE2NThhNzBmNDNmNDY4NGIxN2U0MjBlZTk3NDBhOWU4MWVjYSJ9; expires=Mon, 25-Nov-2019 08:58:13 GMT; Max-Age=7200; path=/, laravel_session=eyJpdiI6Imx2bUpVOTRnYm50a0dIOE5ZdTFIenc9PSIsInZhbHVlIjoiVGpBQWlkaDR2XC8wQ0w4SFdSck1ldDRYQVBPZWJjQ3c4K2NrWitPXC9CWWZON214Z2k2bkx4dFozZXp0WnZxSThhIiwibWFjIjoiMDM5M2YwM2FhMzYwZTc4Y2U0ZDVmOThlZGFkZThlMGY1NDI5ZDA2ZmQ5YTlmNWQ4YmIwZjc4NmFhYTI3NjkyOCJ9; expires=Mon, 25-Nov-2019 08:58:13 GMT; Max-Age=7200; path=/; httponly, PmJSx8WYeiH0HOSxU5AYx1Rui49IQPJpm91JZDY6=eyJpdiI6InFxdnF0Slk3aVJLdjU0RjJOUDB1amc9PSIsInZhbHVlIjoiQUFGTTYzSDRTUzlXUVR0Zk9sR21yRVlJN0N1b2VwelZaYVFXaVJabDd3dThGcjJHTXJqcE1rYWozbzhjZVB4ak1sN1ZWWktGQlkwZnVFNVhGNGc5SVQwRjN0b0dXSjNGTEhDbFF6QkM0UndsYXVcL3ZybFdUTjFuSlkrR1k3ZllCQ091QmdwWldacENcL3VwMHhUTU15Tyt1VzV1V2hEM2Q0VWk2VCtXclIxXC9aVUFYNVRNTmNLZU5jVFRudVgwQ1FVcTQrTzkxeEg0NjVOUStkVGR5aEtwc29TYjdrb3FFUGlrcU11VjNkdFFTV1duOFIrNEhiVDVEb1hvS3V6ZGdCT0xoa0FvWGQyUm80QzlHUkV2dVpRQ3JyamhSMXZsUWpHdk9QeFNHVDc5dWI1UUlVdktKQjNOTVYwK2RHRng4U0d5cmVkaWRaOUxUdjZ0TzF0UTZNdlVRTE9qd1JPcjBIXC93YUp1VU9NRjlRVTNEVWliVG5ETTErb0kyZ25HYWNqaHZzMnk0b011VThJMmh4V3V0XC9MVWdaNGhWVHlzcXdiSHk1eU05RVNpbmNDcUk5WlwvUHdmU0NXSGI0N1NtYXExZCIsIm1hYyI6IjhlZDU4NWVjNGQ5NmQ5MzA5MzA3MmYzNzY3ODMxYzJmY2Q3YjUyMDU0OWVkMmIxYWZiNDlhYWU4YjU1ZGE0MGQifQ%3D%3D; expires=Mon, 25-Nov-2019 08:58:13 GMT; Max-Age=7200; path=/; httponly,acw_tc=276aede515746601737068163e3ae844c6090617d427845a03b064a9d119fa; acw_sc__v2=5ddb7a98fe1386ee06c0cae25c614c02c9c80647;XSRF-TOKEN=eyJpdiI6InlZTm1peFhmY2N0WFwvSGRRXC9nVitjdz09IiwidmFsdWUiOiI5SVwvdmV3azhzcnQ4cnA3NlI4b1JwTG5FZUtsSVBySXRIWWFKTWNmRTVQXC9KcVwvME9iUVdydFVLcXZLQVl2eU00IiwibWFjIjoiNzY5ODQ3ZDk5NTU1ZGI1OGQwMjJlZDI0NGM5NjE2NThhNzBmNDNmNDY4NGIxN2U0MjBlZTk3NDBhOWU4MWVjYSJ9; expires=Mon, 25-Nov-2019 08:58:13 GMT; Max-Age=7200; path=/, laravel_session=eyJpdiI6Imx2bUpVOTRnYm50a0dIOE5ZdTFIenc9PSIsInZhbHVlIjoiVGpBQWlkaDR2XC8wQ0w4SFdSck1ldDRYQVBPZWJjQ3c4K2NrWitPXC9CWWZON214Z2k2bkx4dFozZXp0WnZxSThhIiwibWFjIjoiMDM5M2YwM2FhMzYwZTc4Y2U0ZDVmOThlZGFkZThlMGY1NDI5ZDA2ZmQ5YTlmNWQ4YmIwZjc4NmFhYTI3NjkyOCJ9; expires=Mon, 25-Nov-2019 08:58:13 GMT; Max-Age=7200; path=/; httponly, PmJSx8WYeiH0HOSxU5AYx1Rui49IQPJpm91JZDY6=eyJpdiI6InFxdnF0Slk3aVJLdjU0RjJOUDB1amc9PSIsInZhbHVlIjoiQUFGTTYzSDRTUzlXUVR0Zk9sR21yRVlJN0N1b2VwelZaYVFXaVJabDd3dThGcjJHTXJqcE1rYWozbzhjZVB4ak1sN1ZWWktGQlkwZnVFNVhGNGc5SVQwRjN0b0dXSjNGTEhDbFF6QkM0UndsYXVcL3ZybFdUTjFuSlkrR1k3ZllCQ091QmdwWldacENcL3VwMHhUTU15Tyt1VzV1V2hEM2Q0VWk2VCtXclIxXC9aVUFYNVRNTmNLZU5jVFRudVgwQ1FVcTQrTzkxeEg0NjVOUStkVGR5aEtwc29TYjdrb3FFUGlrcU11VjNkdFFTV1duOFIrNEhiVDVEb1hvS3V6ZGdCT0xoa0FvWGQyUm80QzlHUkV2dVpRQ3JyamhSMXZsUWpHdk9QeFNHVDc5dWI1UUlVdktKQjNOTVYwK2RHRng4U0d5cmVkaWRaOUxUdjZ0TzF0UTZNdlVRTE9qd1JPcjBIXC93YUp1VU9NRjlRVTNEVWliVG5ETTErb0kyZ25HYWNqaHZzMnk0b011VThJMmh4V3V0XC9MVWdaNGhWVHlzcXdiSHk1eU05RVNpbmNDcUk5WlwvUHdmU0NXSGI0N1NtYXExZCIsIm1hYyI6IjhlZDU4NWVjNGQ5NmQ5MzA5MzA3MmYzNzY3ODMxYzJmY2Q3YjUyMDU0OWVkMmIxYWZiNDlhYWU4YjU1ZGE0MGQifQ%3D%3D; expires=Mon, 25-Nov-2019 08:58:13 GMT; Max-Age=7200; path=/; httponly'
    h = {
        'User-Agent': 'Mozilla/5.1 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.39',
        'Cookie': Cookie
    }
    response = requests.get(url, headers=h)
    # print( response.headers)
    cs = response.headers['Set-Cookie']
    Cookie = 'acw_tc=276aede515746601737068163e3ae844c6090617d427845a03b064a9d119fa; acw_sc__v2=5ddb7a98fe1386ee06c0cae25c614c02c9c80647;'
    Cookie = Cookie + cs
    config.set("Cookie", "cookie", Cookie)
    # print(cs)
    # print(Cookie)
    text = response.text
    #print(text)
    soup = BeautifulSoup(text, 'html.parser')
    divs=soup.find_all('div',class_='tx-item')
    for div in divs:
        tx_hash=div.find('a',class_='tx-item-summary-hash').string.strip()
        tx_time=div.find('span',class_='tx-item-summary-timestamp -btc-time-localization').string.strip()
        txio=div.find_all('ul')
        #print(txio)
        if len(txio)==2:
            # print(txio)
            # print(tx_hash)
            # print(tx_time)
            tx_from_block=txio[0].find(class_='txio-address').string
            if tx_from_block!=None:
                tx_from_block=tx_from_block.strip()
            txio_from_amount=float([text.strip() for text in txio[0].find(class_='txio-amount')(text=True) if text.parent.name !='span' and text.strip()][0])

            for li in  txio[1].find_all('li'):
                #print(li)
                tx_to_block = li.find(class_='txio-address').string
                if tx_to_block != None:
                    tx_to_block = tx_to_block.strip()
                txio_to_amount =float([text.strip() for text in li.find(class_='txio-amount')(text=True) ][0])
                # print(tx_hash)
                print(tx_time)
                print(tx_from_block)
                print(txio_from_amount)
                print(tx_to_block)
                print(txio_to_amount)
                print('/n')

    #print(div)



if __name__ == '__main__':
    book_label_spider()





