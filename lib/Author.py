# Import the Article class
from Articles import Article

class Author:
    # List to store all author instances
    all_authors = []
    
    def __init__(self, name):
        self.name = name
        self.articles = [] 
        Author.all_authors.append(self) 
        
    def name(self):
        return self.name
    
    def articles(self):
        return self.add_article
    
    def magazine(self):
        return [article.magazine() for article in self._articles]
    
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.articles.append(article)

        
    def topic_areas(self):
        return list(set([magazine.category() for magazine in self.magazines()]))
