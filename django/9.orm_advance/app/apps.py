from django.apps import AppConfig

class AppConfig(AppConfig):
    name = 'app'
    def ready(self):
        from .models import Author, Book, Category

        def createDatabase():
            Author(code="AUTH_0001", name="Author 1").save()
            Category(code="C1", name="Category 1").save()
            Category(code="C2", name="Category 2").save()
            book = Book(code="B1", name="Book 1", author=Author.objects.get(id=1))
            book.save()
            book.categories.add(*Category.objects.all())
            book.save()
            
        try:
            if Book.objects.count() == 0:
                createDatabase()

            book = Book.objects.get(id=1)
            print(book.code, book.name, book.categories.all())

            categ = Category.objects.get(id=1)
            print(categ.code, categ.name, categ.book_set.all())
        except:
            pass