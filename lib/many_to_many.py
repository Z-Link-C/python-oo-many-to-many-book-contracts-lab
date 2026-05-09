class Author:
    all=[]
    def __init__(self,name):
        self.name=name
        Author.all.append(self)
    def contracts(self):
        return [cont for cont in Contract.all if cont.author==self]
    def books(self):
        return[cont.book for cont in Contract.all if cont.author==self]
    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)
    def total_royalties(self):
        return sum(cont.royalties for cont in Contract.all if cont.author==self)   

class Book:
    all=[]
    def __init__(self,title):
        self.title=title
        Book.all.append(self)
    def authors(self):
        return[cont.author for cont in Contract.all if cont.book==self]
    def contracts(self):
        return[contract for contract in Contract.all if contract.book==self]

class Contract:
    all=[]
    def __init__(self,author,book,date,royalties):
        self.author=author
        self.book=book
        self.date=date
        self.royalties=int(royalties)
        Contract.all.append(self)
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,data):
        if not isinstance(data,Author):
            raise Exception 
        self._author=data
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self,data):
        if not isinstance(data,Book):
            raise Exception 
        self._book=data
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self,data):
        if not isinstance(data,str):
            raise Exception 
        self._date=data
    @classmethod
    def contracts_by_date(cls,target):
        return [c for c in cls.all if c.date==target ]