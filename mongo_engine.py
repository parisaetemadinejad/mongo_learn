# One library that provides a higher abstraction on top of PyMongo is MongoEngine. MongoEngine
# is an object-document mapper (ODM), which is roughly equivalent to an SQL-based object-relational mapper (ORM).
# MongoEngine provides a class-based abstraction, so all the models you create are classes.
from mongoengine import connect, Document, StringField, ListField, URLField

connect(db="my_database_3", host="localhost", port=27017)


# In MongoEngine, the class is equivalent to a collection, and its instances are equivalent to documents.
class Tutorial(Document):
    title = StringField(required=True, max_length=70)
    author = StringField(required=True, max_length=20)
    contributors = ListField(StringField(max_length=20))
    url = URLField(required=True)


tutorial1 = Tutorial(
    title="Beautiful Soup: Build a Web Scraper With Python",
    author="Martin",
    contributors=["Aldren", "Geir Arne", "Jaya", "Joanna", "Mike"],
    url="https://realpython.com/beautiful-soup-web-scraper-python/"
)

tutorial1.save()  # Insert the new tutorial
for doc in Tutorial.objects:
    print(doc.title)
