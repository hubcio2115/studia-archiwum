package lab9

import scala.io.Source

@main
def lab9zad1(): Unit = {
  val lines = Source
    .fromResource("./lab9/resources/nazwiska.txt")
    .getLines.toList

  val amountOfUniqs = lines.foldLeft(0)((acc, fullName) => {
    val name = fullName.split(" +").head

    val probableMax = name.groupBy(character => character.toLower).map(element => (element._1, element._2.length)).toList.length

    if (probableMax > acc) probableMax
    else acc
  })

  val listOfFullNames = lines.foldLeft(Nil: List[String])((acc, fullName) => {
    if (fullName
      .split(" +")
      .head
      .groupBy(character => character.toLower)
      .map(element => (element._1, element._2.length))
      .toList.length == amountOfUniqs) acc :+ fullName.split(" +").last
    else acc
  })

  println(listOfFullNames)
}
