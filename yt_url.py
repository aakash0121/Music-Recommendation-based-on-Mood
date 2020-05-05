import urllib.request
import urllib.parse
import re

def url(input_str):
    query_string = urllib.parse.urlencode({"search_query" : input_str})
    # print(query_string)
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    url = "http://www.youtube.com/watch?v=" + search_results[0]
    return url

if __name__ == "__main__":
    print(url("sad songs"))