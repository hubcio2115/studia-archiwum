package lab1

def frame(script: String): String = {
  val lines = script.split("\n")
  val longestLine = lines.maxBy(s => s.length).length


  f"${"*" * (longestLine + 4)}" +
    "\n" +
    lines.map(line => {
      f"* $line ${" " * (longestLine - line.length)}*"
    }).mkString("\n") +
    "\n" +
    f"${"*" * (longestLine + 4)}"
}

@main
def lab1zad1(): Unit = {
  print(frame(
    """Inwokacja
      |Litwo! Ojczyzno maja! Ty jesteś jak zdrowie,
      |Ile cię trzeba cenić, ten tylko się dowie,
      |Kto cię stracił. Dziś piękność twą w całej ozdobie
      |Widzę i opisuję, bo tęsknię po tobie"
      |Panno święta, co Jasnej bronisz Częstochowy
      |I w Ostrej świecisz Bramie! Ty, co gród zamkowy
      |Nowogródzki ochraniasz z jego wiernym ludem!
      |Jak mnie dziecko do zdrowia powróciłaś cudem,
      |(Gdy od płaczącej matki pod Twoją opiekę
      |Ofiarowany, martwą podniosłem powiekę
      |I zaraz mogłem pieszo do Twych świątyń progu
      |Iść za wrócone życie podziękować Bogu),
      |Tak nas powrócisz cudem na Ojczyzny łono.
      |Tymczasem przenoś moją duszę utęsknioną
      |Do tych pagórków leśnych, do tych łąk zielonych,
      |Szeroko nad błękitnym Niemnem rozciągnionych;
      |Do tych pól malowanych zbożem rozmaitem,
      |Wyzłacanych pszenicą, posrebrzanych żytem;
      |Gdzie bursztynowy świerzop, gryka jak śnieg biała,
      |Gdzie panieńskim rumieńcem dzięcielina pała,
      |A wszystko przepasane jakby wstęgą, miedzą
      |Zieloną, na niej z rzadka ciche grusze siedzą.""".stripMargin))
}
