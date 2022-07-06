package lab7

@main
def lab7zad6(): Unit = {
  val europeanTimeZones = java.util.TimeZone.getAvailableIDs.toSeq
    .filter(timeZone => timeZone.slice(0, 6) == "Europe")
    .sortWith(_.stripPrefix("Europe/").length < _.stripPrefix("Europe/").length)

  println(europeanTimeZones)
}
