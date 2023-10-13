# Import the Article class
from Articles import Article

class Magazine:
    all_maz_instances = []
    
    def __init__ (self, name, category):
        self.name = name
        self.category = category
        self.contributors = [] 
        Magazine.all_maz_instances.append(self)
        
    def name(self):
        return self.name()
        
    def category(self):
        return self.category
    
    @classmethod
    def all(cls):
        return cls.all_maz_instances
    
    #2
    def contributors(self):
        return self.contributors #author instance list
    
    #3
    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls.all_maz_instances if magazine.name() == name), None)

    #  - Returns an list strings of the titles of all articles written for that magazine
    @classmethod   
    def article_titles(cls, magazine_name):
        magazine = cls.find_by_name(magazine_name)
        if magazine:
            return [article.title() for article in magazine.contributors()]
        return []
        
    def contributing_authors(self):
        authors_count = {}  # Dictionary to store authors and their article counts
        for author in self.contributors:
            authors_count[author] = authors_count.get(author, 0) + 1
        return [author for author, count in authors_count.items() if count > 2]

    