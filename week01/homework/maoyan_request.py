import requests
from bs4 import BeautifulSoup as bs
import pandas


def get_top10_url(url, headers):
    urls_list = []
    response = requests.get(url=url, headers=headers)
    # print(response.status_code)
    soup = bs(response.text, 'html.parser')
    for tags in soup.find_all('div', attrs='movie-item-hover', limit=2):
        for atags in tags.find_all('a', ):
            url = atags.get('href')
            url = "https://maoyan.com" + url
            urls_list.append(url)
    # print(urls_list)
    return urls_list

def get_movie_datails(url, headers):
    headers['referer'] = url
    soup = bs(requests.get(url=url, headers=headers).text, 'html.parser')
    
    for tags in soup.find_all('div', attrs='movie-brief-container'):
        f_name = tags.find('h1').text
        f_type = []
        f_li = []
        for atags in tags.find_all('a'):
            for atag in atags:
                f_type.append(atag)

        for lis in tags.find_all('li'):
            for li in lis:
                f_li.append(li)
        f_time = f_li[-1]
        f_type = str(f_type)
    
        mydata = [f_name, f_type, f_time]
        
        return mydata


        
if __name__ == "__main__":
    ori_url = "https://maoyan.com/films?showType=3"
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
    headers['cookie'] = '__mta=244135226.1598191230234.1598191842812.1598192314260.5; uuid_n_v=v1; uuid=12A8D810E54911EABACC073A21454EB2845AF04E15F64E9EB6F076EC02CF13E1; _csrf=4a8b3526b5f90173e2c8284a187e9ce9638e3ce316b95b10e3caeefd11e7f069; _lxsdk_cuid=1741b9edc6ec8-08f723bd5d32c-37647e02-13c680-1741b9edc6ec8; _lxsdk=12A8D810E54911EABACC073A21454EB2845AF04E15F64E9EB6F076EC02CF13E1; mojo-uuid=9455dc764808635c54fae52e65852a0d; mojo-session-id={"id":"69c7c410e0f7ba6623ec7c79edabf2f6","time":1598191230681}; lt=UeApFimLdENIeZ24PHMyY68PhpwAAAAAVgsAAJgRzPYFkQXukIkWy5tYksyLMVVOjYD-MLPqMgZOh5mzNp3JDh2BVYVqPZ846rl4bA; lt.sig=AV2Tm8bBBTPuK_d8UO73b99AeFY; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598191230,1598194144; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598194144; mojo-trace-id=11; __mta=244135226.1598191230234.1598192314260.1598194144124.6; _lxsdk_s=1741b9edc6f-77f-913-4c3%7C%7C19'
    

    
    for url in get_top10_url(ori_url, headers):
        mydata = get_movie_datails(url, headers)
        movie1 = pandas.DataFrame(data=mydata)
        movie1.to_csv('./movie1.csv', encoding='utf-8', index=False, header=False)   