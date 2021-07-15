# INTRO
<br />

## Web scraping is the process of extracting and parsing data from websites in an automated fashion using a computer program. It's a useful technique for creating datasets for research and learning.[Want to learn more](https://towardsdatascience.com/https-medium-com-hiren787-patel-web-scraping-applications-a6f370d316f4) Follow these steps to build a web scraping project from scratch using Python and its ecosystem of libraries:

# Dependencies
<br />

## Python , Tensorflow , numpy , OpenCV , BeautifulSoup , Requests



## Getting Started

# Pick a website and describe your objective

Browse through different sites and pick on to scrape.  
Identify the information you'd like to scrape from the site. Decide the format of the output CSV file.

# Using Beautiful Soup and Requests libraries for extraction html content

Use the requests library to download web pages

```
Requests library : pip install requests
Beautiful Soup : pip install Beautiful Soup
```


Inspect the website's HTML source and identify the right URLs to download.
Download and save web pages locally using the requests library.
Create a function to automate downloading for different topics/search queries.
Use Beautiful Soup to parse and extract information

# create functions for extracting the useful information with a-tags , p-tags 

Create functions to extract from the page into lists and dictionaries.

# Put all the data in a dataframe 

Dataframe is a 2-D table helps to show the data in an organised manner .

# Create the base html template

Create the html head , body , title tag .
```
<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    </head>
    <body>
      
    </body>
</html>
```

# Convert dataframe to html table 

Converted the dataframe to html table using to_html function .

# Add the resulting table to html template 

# Formatting /Beatifying the html file 

Make links clickable , start index from 1 and add css styling .

Verify the information in the CSV files by reading them back using Pandas.
Document and share your work

