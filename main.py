from viewing_party.movie import Movie
from viewing_party.person import Person

Dune = Movie("Dune","Science Fiction",4.8 ,"HBO")
Sandlot = Movie("Sandlot","Family",4.0 ,"Disney+")
Encanto = Movie("Encanto","Family",4.2 ,"Disney+")
Spiderman = Movie("Spiderman","Action",4.0 ,"Netflix")

Jerica = Person("Jerica",[Dune,Sandlot,Spiderman],["Netflix", "HBO"])
Nancy = Person("Nancy",[Encanto,Sandlot,Spiderman],["Netflix", "Disney+"])
Auberon = Person("Auberon",[Encanto,Dune,Spiderman],["Hulu", "HBO"])





