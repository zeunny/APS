import re, collections

def solution(word, pages):
    answer = []
    
    basic_score = collections.defaultdict(int)
    external_links = collections.defaultdict(int)
    outside_links = collections.defaultdict(list)
    
    p_strings = re.compile(r'[a-z]+')
    p_myurl = re.compile(r'<meta property="og:url" content="([^"]+)"/>')
    p_outsideurl = re.compile(r'<a href="([^"]+)">')
    
    urls = []
    for page in pages:
        myurl = p_myurl.search(page).group(1)
        urls.append(myurl)
        for p_string in p_strings.findall(page.lower()):
            if word.lower() == p_string:
                basic_score[myurl] += 1
        for link in p_outsideurl.findall(page):
            outside_links[link].append(myurl)
        external_links[myurl] += len(p_outsideurl.findall(page))
    
    for index, url in enumerate(urls):
        link_score = 0
        for outside_link in outside_links[url]:
            link_score += basic_score[outside_link] / external_links[outside_link]
        answer.append((-(basic_score[url] + link_score), index))
    
    answer.sort()
    
    return answer[0][1]