# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai
# lehti. Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä,
# kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6
# (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien julkaisujen
# kaikki tiedot toteuttamiesi metodien avulla.


class Publishment:
    def __init__(self,p_name):
        self.p_name = p_name

    def print(self):
        print(self.p_name)

class Book(Publishment):
    def __init__(self, writer, pages, p_name):
        self.writer = writer
        self.pages = pages
        super().__init__(p_name)

    def print(self):
        super().print()
        print(f"Writer: {self.writer}, amount of pages:{self.pages}")


class Paper(Publishment):
    def __init__(self, editor, p_name):
        self.editor = editor
        super().__init__(p_name)

    def print(self):
        super().print()
        print(f"Editor: {self.editor}")

if __name__=='__main__':
    book = Book("Rosa Liksom", 200, "Hytti n:o 6 ")
    book.print()
    paper = Paper("Aki Hyyppä", "Aku Ankka")
    paper.print()