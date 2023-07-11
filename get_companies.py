import requests
from lxml import html

def get_company_with_registration(registration_number):
    url = "https://application.ocr.gov.np/faces/CompanyDetails.jsp"

    payload = f'j_id_jsp_826405674_6=j_id_jsp_826405674_6&j_id_jsp_826405674_6%3AregistrationNumber={registration_number}&j_id_jsp_826405674_6%3Aj_id_jsp_826405674_16=Search&javax.faces.ViewState=j_id2077%3Aj_id2096'
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSESSIONID=94EBADC98D57DC8CE580912DC0324F29',
    'Origin': 'https://application.ocr.gov.np',
    'Referer': 'https://application.ocr.gov.np/faces/CompanyDetails.jsp',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    tree = html.fromstring(response.content)
    table_rows = tree.xpath('//tbody[contains(@id,"companyDetails")]/tr')
    for table_row in table_rows:
        table_data = table_row.xpath('.//td')
        if len(table_data) > 1 :
            table_datas = [x.xpath('.//text()')[0] for x in table_data if len(x.xpath('.//text()')) > 0]
            with open("companies.csv", "a") as myfile:
                myfile.write(",".join(table_datas) + "\n")
            


if __name__ == "__main__":
    for i in range(1, 1000000):
        get_company_with_registration(i)


