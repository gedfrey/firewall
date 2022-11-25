import requests
from lxml import html,etree

headers= {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
}

def get_first_or_fail(items):

    if len(items) != 1:

        raise Exception(
            "Error, Debe existir mas de un elemento"
        )
    
    return items[0]

def get_ipaddress_ipinfo():

    main = requests.post(
        "http://www.find-ip-address.org/ip-country/",
        data={
            "country": "CL",
            "prefix": "",
            "output": "cidr"
        }
    )

    tree_main = html.fromstring(main.content)
    print(etree.tostring(tree_main, pretty_print=True))
    ips = tree_main.xpath("//p/text()")

    print("ips",ips[1].replace("\n","").split(" ")[1:])

    return ips[1].replace("\n","").split(" ")[1:]
    
    # session = requests.Session()
    # print(session.cookies.get_dict())
    # response = session.get('https://ipinfo.io/countries/cl')
    # print(session.cookies.get_dict())
    # main = requests.get(
    #     "https://ipinfo.io/countries/cl",
    #     headers={
    #         "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
    #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    #         "Accept-Language": "es-CL,es;q=0.8,en-US;q=0.5,en;q=0.3",
    #         "Alt-Used": "ipinfo.io",
    #         "Upgrade-Insecure-Requests": "1",
    #         "Sec-Fetch-Dest": "document",
    #         "Sec-Fetch-Mode": "navigate",
    #         "Sec-Fetch-Site": "none",
    #         "Sec-Fetch-User": "?1"
    #     }
    # )
    # print(main.cookies)
    # print("main",main.text)

    # tree_main = html.fromstring(main.content)
    # asns = tree_main.xpath('//div[@class="container my-5 py-3 container-markdown"]/div//table/tr/td[1]/a/@href')
    # print(asns)

    # print("main headers",main.headers)
    # print(session.cookies.get_dict())
    # for asn in asns[0:1]:

    #     req_asn_detail = requests.get(
    #             "https://ipinfo.io" + asn
    #         )
        
    #     tree_details = html.fromstring(req_asn_detail.content)
        
    #     print(etree.tostring(tree_details, pretty_print=True))

    #     # netblocks = tree_details.xpath(
    #     #     '//table[]/tr'
    #     # )

    # print(etree.tostring(href[0], pretty_print=True))
