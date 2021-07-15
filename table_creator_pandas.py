# module pyopen.xls
# target read 

""" importing modules """

import pandas as pd
import os
import numpy as np

""" reading the file and loading the excel file as a dataframe """
saved_file = pd.read_excel(r"C:\Users\prern\Documents\GitHub\web_scrape\saved_file.xlsx")


saved_file = pd.DataFrame(saved_file)

#  capitalize the heading of the columns
saved_file.columns = saved_file.columns.str.capitalize()



a = 10


    # target _blank to open new window
    # extract clickable text to display for your link
for i in range(len(saved_file["Url"])):
  saved_file["Url"][i] = f'<a target="_blank" href="{saved_file["Url"][i]}">{saved_file["Url"][i]}</a>'


# link is the column with hyperlinks


print(saved_file["Url"][0])

""" converting the default index from 0 to 1"""
saved_file.index = np.arange(1, len(saved_file) + 1)
print(saved_file)


""" converting the dataframe into a html file , and reading the contents of the file , and assigning a class for the table """

saved_file.to_html("data.html")
with open("data.html") as file:
	file = file.read()
file = file.replace('<table border="1" class="dataframe">', '<table class="w3-table-all w3-hoverable">')

"""opening a new html file and writing the contents of the html file in it"""

with open("data.html", "w" , encoding="utf8") as file_to_write:
	file_to_write.write(file) 
# os.startfile("data.html") 

""" making the starting part of the html"""
start_html_tag = """<!DOCTYPE html>
<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>
<div class="w3-container">
    <h1>Github Web Scraping</h1>
    <p>This is a table for containing useful urls, description of each of the topics in github which has been extracted by using Web Scraping</p>
    <br />\n"""
    
# main html tAG
with open('data.html', 'r') as f2:
    html = f2.read()


# the end part of html template in the end_tag variable
end_tag = """\n
<br />
</div>
</body>
</html>"""


#write html to file
text_file = open("index1.html", "w")
text_file.write(start_html_tag)
text_file.write(html)
text_file.write(end_tag)

#input file

fin = open("index1.html", "rt")
#output file to write the result to
fout = open("output_data.html", "wt")  
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
  # print('\n' + line + '\n')
  # going to each line in the html file where "&lt" and "&gt"
  if "&lt;" in line:
    x = line.replace('&lt;', '<')
    x = x.replace('&gt;', '>')
    fout.write(x)
  #   fout.write(line.replace('&lt;', '<'))
  # elif "&gt;" in line:
  #   fout.write(line.replace('&gt;', '>'))
  else:
    fout.write(line)
  # fout.write(line.replace('&gt;', '>'))
#close input and output files
fin.close()
fout.close()
        


        

os.startfile("output_data.html") 

