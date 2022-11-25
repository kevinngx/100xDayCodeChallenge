from bs4 import BeautifulSoup
import requests

def main():
    response = requests.get("https://news.ycombinator.com/")
    soup = BeautifulSoup(response.text, "html.parser")
    
    article_texts = []
    article_links = []

    article_tags = soup.find_all(name="a", class_="storylink")
    for article_tag in article_tags:
        # Obtain data from tags
        article_text = article_tag.getText()
        article_link = article_tag.get("href")
        
        # Append to lists
        article_texts.append(article_text)
        article_links.append(article_link)
       
    article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]
    print(article_texts)
    print(article_links)
    print(article_upvotes)
    max_index = article_upvotes.index( max(article_upvotes) )
    print("max: " + str(max_index))
    print("Text: " + article_texts[max_index])
    print("Link: " + article_links[max_index])
    print("Upvotes: " + str(article_upvotes[max_index]))


    
 
    
   

if __name__ == '__main__':
    main()