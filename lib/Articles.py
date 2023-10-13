# Import the Author and Magazine classes
from Author import Author
from Magazine import Magazine

class Article:
    # List to store all article instances
    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        # Adding the article instance to the list of all articles
        Article.all_articles.append(self)
        # Adding the article to the list of articles by this author
        author.articles().append(self)
        # Adding the author to the list of contributors for this magazine
        magazine.contributors().append(author)

    def title(self):
        return self.title
    
    # Class method to get a list of all article instances
    @classmethod
    def all(cls):
        return cls.all_articles
   
   # Method to get the author of the article 
    def author(self):
        return self.author

    # Method to get the magazine of the article
    def magazine(self):
        return self.magazine