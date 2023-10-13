# Import the Author and Magazine classes
from Author import Author
from Magazine import Magazine

class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)
        author.articles().append(self)
        magazine.contributors().append(author)

    def title(self):
        return self.title
    
    @classmethod
    def all(cls):
        return cls.all_articles
    
    def author(self):
        return self.author

    def magazine(self):
        return self.magazine