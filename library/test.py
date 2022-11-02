from main import Book, db, app


# query = Book(title="Potttt", author="J. K. R.", rating=10.0)
# with app.app_context():
#     db.session.add(query)
#     db.session.commit()

# with app.app_context():
#     Book.query.filter_by(title="Pot").delete()
#     db.session.commit()

# with app.app_context():
#     update = Book.query.filter_by(id=2).first()
#     update.author = "Cez"
#     db.session.commit()

### READ ALL RECORDS ####
with app.app_context():
    all_books = db.session.query(Book).order_by(Book.rating).all()
    for book in all_books:
        print(book.id, book.title, book.author, book.rating)