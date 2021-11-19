import math


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for x in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label):
        for i in range(len(self.photos)):
            for j in range(4):
                if j == len(self.photos[i]):
                    self.photos[i].append(None)
                if not self.photos[i][j]:
                    self.photos[i][j] = label
                    return f"{label} photo added successfully on page {i + 1} slot {j + 1}"
        return "No more free slots"

    def display(self):
        result = ["-----------\n"]
        for i in range(len(self.photos)):
            result.append(' '.join('[]' for _ in self.photos[i]))
            result.append("\n-----------\n")

        return "".join(result).strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())


