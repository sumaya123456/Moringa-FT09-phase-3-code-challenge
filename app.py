from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()


    '''
        The following is just for testing purposes, 
        you can modify it to meet the requirements of your implmentation.
    '''

    # Create an author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid # Use this to fetch the id of the newly created author

    # Create a magazine
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid # Use this to fetch the id of the newly created magazine

    # Create an article
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   (article_title, article_content, author_id, magazine_id))

    conn.commit()

    # Query the database for inserted records. 
    # The following fetch functionality should probably be in their respective models

    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()

    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

    print("\nAuthors:")
    for author in authors:
        print(Author(author["id"], author["name"]))

    print("\nArticles:")
    for article in articles:
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))







# Set up the table
    # Initialize the database and create tables
create_tables()

  # Create an Article
article = Article.create(title="Test Content" ,author=author, magazine=magazine)
print(artical.title)

    # Delete the article
article_id=1
Article.delete_by_id(Article_id_to_delete)
print(f"Deleted Article with ID {Article_id_to_delete}")
    # Create an authors
author = Author.create(Name, "John Doe")
print(author.author.name) #should print "John Doe"
# Fetch and print all authors
all_authors = Author.get_all()
print("All authors:", all_authors)
#delete the author
author_id_to_delete = 4
Author.delete_by_id(author_id_to_delete)
print(f"Deleted author with ID {author_id_to_delete}")
# Create a new magazine
magazine = Magazine.create(name="Tech Monthly", category="Technology")
print(magazine.name.category) #should print "TechMonthly", "Technology"

# Delete the magazine 
mag_id = 3 
Magazine.delete_by_id(mag_id)
print(f"Deleted magazine with ID {mag_id}")


# Create an instance of the Article class
article = Article(1, "Sample Title", "Sample content", 1, 1)

# Printing the representation of the Article instance
print(article) 

#def main():
    # Initialize the database and create tables
   # create_tables()

    # Collect user input or create articles programmatically
   # article = Article(id=1, title="Sample Title", content="Sample content", author_id=000, magazine_id=1)
   # article.save()

    # Display the article before deletion
    #print("Article before deletion:")
   # print(article)

    # Delete the article
    #rticle.delete()
    #print(f"Article with ID {article.id} has been deleted.")
    # Create an author
author = Author(None, "John Doe")
author.save()
print(f"Created author: {author}")
# Fetch and print all authors
all_authors = Author.get_all()
print("All authors:", all_authors)
#delete by id
author_id_to_delete = 4
Author.delete_by_id(author_id_to_delete)
print(f"Deleted author with ID {author_id_to_delete}")
# Create a new magazine
mag = Magazine(name="Tech Monthly", category="Technology")
print(f"Created: {mag}")

# Delete the magazine by ID
mag_id = 3 
Magazine.delete_by_id(mag_id)
print(f"Deleted magazine with ID {mag_id}")



if __name__ == "__main__":
    main()
