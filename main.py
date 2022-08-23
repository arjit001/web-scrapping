import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL from which pdfs to be downloaded
file = pd.read_excel('image list.xlsx', 'Sheet 1')
ur = "https://www.your-site.com/"
for j in range(len(file)):
    url = "https://www.your-site.com/search?q={}".format(file.loc[j]['Vendor1 SKU'])
    print(url)

    # Requests URL and get response object
    response = requests.get(url)

    # Parse text obtained
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all hyperlinks present on webpage
    links = soup.find_all('a')
    i = 0
    # print(links)
    # From all links check for pdf link and
    # if present download file
    for link in links:
        if str.lower(file.loc[j]['Vendor1 SKU']) in link.get('href', []):
            url1 = str(link.get('href'))
            print(url1)
            response1 = requests.get(url1)
            soup1 = BeautifulSoup(response1.text)
            links1 = soup1.find_all('a')
            for link1 in links1:
                if '.jpg' and str(file.loc[j]['Vendor1 SKU']) in link1.get('href', []):
                    i += 1
                    print("Downloading file: ", i)
    
                    # Get response object for link
                    response = requests.get(link.get('href'))

                    # Write content in pdf file
                    pdf = open(file.loc[j]['SKU'] + ".jpg", 'wb')
                    print(pdf)
                    pdf.write(response.content)
                    pdf.close()
                    print("File ", i, " downloaded")
            print("All images files downloaded")
