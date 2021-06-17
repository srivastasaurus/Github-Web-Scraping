import requests
from bs4 import BeautifulSoup
import pandas as pd
import webbrowser
import os

main_url = "https://github.com/topics"

response = requests.get(main_url) 
"""print(response.status_code)"""

content = response.text
"""print(content[:1000])"""

# save it in html file 

"""with open('webpage.html', 'w', encoding="utf-8") as f:
    f.write(content)"""


soup = BeautifulSoup(content , "html.parser") 


# extracting all the title of the topics using the specified class

topic_title_p_tags = soup.find_all("p", {"class" : "f3 lh-condensed mb-0 mt-1 Link--primary"})
#print(topic_title_p_tags[:10])

""" extracting the description of the topocs from p tag using class """

topic_desc = soup.find_all("p", {"class" :"f5 color-text-secondary mb-0 mt-1"})

"""print(topic_desc[:10])"""

""" extracting all the topic links with a tags with the class """ 
topic_link_tags = soup.find_all("a", {"class": "d-flex no-underline"})


base_url = "https://github.com/"

topic_links_list = []
for i in range(len(topic_link_tags)):
    topic_links_list.append(base_url + topic_link_tags[i]["href"])

topic_title = []
for i in range(len(topic_title_p_tags)):
    topic_title.append(topic_title_p_tags[i].text)

#print(topic_title)

topic_desc_list = []

for tag in topic_desc:
    topic_desc_list.append(tag.text.strip())

#print(topic_desc_list[:5])

# print(topic_links_list)

# creatinga csv file out of the data that we have extracted 
dict_topic = {"title" : topic_title ,
                "description" : topic_desc_list,             
    "url" :topic_links_list }
topics_df = pd.DataFrame(dict_topic)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    """print (topics_df)"""

topics_df.to_csv("topics.csv")


# now from each topic page (like from topic urls) we are going to extract information 

## getting information out of a topic page 

topic_page_url = topic_links_list[0]
"""print(topic_page_url)"""   

response2 = requests.get(topic_page_url)
print(response2.status_code)

topic_doc = BeautifulSoup(response2.text, "html.parser")

selection_class_forh1 = "f3 color-text-secondary text-normal lh-condensed"

repo_tags = topic_doc.find_all("h1", {"class" : selection_class_forh1})
"""print(len(repo_tags))"""


"""print(repo_tags[0])"""  # returns h1 class with two a tags 
a_tag = repo_tags[0].find_all("a")
"""print(a_tags)"""
"""print(a_tags[0].text.strip())""" # gives mr.doob
"""print(a_tags[1].text.strip())"""
"""print(a_tags[1]["href"])"""
# print(repo)


# function for grabbing stars

star_tags = topic_doc.find_all("a", {"class" : "social-count float-none"} )

"""print(star_tags[0].text.strip())"""

# converting stars k in numbers 

def parse_star_count(stars_str):
    stars_str = stars_str.strip()
    if stars_str[-1] == "k":
        return int(float(stars_str[:-1]) * 1000)
    else:
        return int(stars_str)



def get_repo_info(h1_tag , star_tags):
    a_tags = h1_tag.find_all("a")
    user_name = a_tags[0].text.strip()
    repo_name = a_tags[1].text.strip()
    repo_url = base_url + a_tags[1]["href"]
    stars = parse_star_count(star_tags.text.strip())
    return user_name , repo_name , stars , repo_url

get_repo_info(repo_tags[0] , star_tags[0])

topic_repos_dict = {"username" : [],
                    "repo_name" : [], 
                    "stars" : [] , 
                    "repo_url" : []
}
for each_repo in range(len(repo_tags)):
    repo_info = get_repo_info(repo_tags[each_repo] , star_tags[each_repo])
    topic_repos_dict["username"].append(repo_info[0])
    topic_repos_dict["repo_name"].append(repo_info[1])
    topic_repos_dict["stars"].append(repo_info[2])
    topic_repos_dict["repo_url"].append(repo_info[3])


"""print(topic_repos_dict)"""


topic_repos_df = pd.DataFrame(topic_repos_dict)
print(topic_repos_df) 

# starting part of html template
start_html_tag = """<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;

</style>
</head>
<body>

    <h1>Github Web Scraping</h1>
    <p>Table for github repository</p>\n"""

# main html tAG
html = topic_repos_df.to_html()

# the end part of html template in the end_tag variable
end_tag = """\n
</body>
</html>"""


#write html to file
text_file = open("index1.html", "w")
text_file.write(start_html_tag)
text_file.write(html)
text_file.write(end_tag)
text_file.close() 




# 1st method how to open html files in chrome using
filename = 'file:///'+os.getcwd()+'/' + 'index1.html'
webbrowser.open_new_tab(filename)
# have just done it for 3d but to automate it for other repos (creating a function) function takes topic_url

def get_topic_repo(topic_url):
    response = requests.get(topic_links_list)
    if response.status_code != 200:
        raise Exception("Failed to load page {}")


