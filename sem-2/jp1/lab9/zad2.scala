package lab9

import scala.io.Source

@main
def lab9zad2(): Unit = {
  val lines = Source
    .fromResource("./lab9/resources/ogniem-i-mieczem.txt")
    .getLines
    .toList

  def histogram(max: Int): String = {
    val lettersCounter = lines
      .mkString
      .replaceAll("[^a-zA-ZąĄćĆęĘłŁńŃóÓśŚ]", "")
      .toLowerCase
      .groupBy(character => character.toLower)
      .map(element => (element._1, element._2.length))
      .toList

    lettersCounter.foldLeft("")((acc, pair) => {
      acc + s"\n${pair(0)}: ${"*" * max.min(pair(1))}"
    }).trim
  }

  println(histogram(120))
}
