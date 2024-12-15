class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self,author_id, magazine_id, title):
        return f'<Article {self.title}>'
        # Insert the article into the articles table (simulating DB insertion)
        sql = """
        INSERT INTO articles (title, author_id, magazine_id)
        VALUES (?, ?, ?)
        """
        cursor.execute(sql, (title, author_id, magazine_id))
        return cursor.conncursor # Returns the last inserted id
    
    @property
    def author(self):
        # Use SQL JOIN to get the author of the article
        sql = """
        SELECT authors.id, authors.name
        FROM articles
        JOIN authors ON articles.author_id = authors.id
        WHERE articles.id = ?
        """
        cursor.execute(sql, (self.id,))
        result = cursor.conncursor()
        return Author(id=result[0], name=result[1])

    @property
    def magazine(self):
        # Use SQL JOIN to get the magazine of the article
        sql = """
        SELECT magazines.id, magazines.name, magazines.category
        FROM articles
        JOIN magazines ON articles.magazine_id = magazines.id
        WHERE articles.id = ?
        """
        cursor.execute(sql, (self.id,))
        result = cursor.conncursor()
        return Magazine(id=result[0], name=result[1], category=result[2])