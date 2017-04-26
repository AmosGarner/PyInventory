from createCollection import createCollection
from ObjectFactories.albumFactory import AlbumFactory
from ObjectFactories.bookFactory import BookFactory
from ObjectFactories.itemFactory import ItemFactory
from ObjectFactories.movieFactory import MovieFactory

def main():
        createCollection('agarner','books')

        item = ItemFactory.createItem('item1','','')
        print(item.name)
        album = AlbumFactory.createAlbum('album1','','','artist1')
        print(album.name)
        book = BookFactory.createBook('book1','','','author1')
        print(book.name)
        movie = MovieFactory.createMovie('movie1','','','director1')
        print(movie.name)


if __name__ == '__main__':
    main()
