package lab14.model

import akka.actor.{Actor, ActorRef}

object Group {
  case object Round

  // Zawodnicy mają wykonać swoje próby – Grupa
  // kolejno (sekwencyjnie) informuje zawodników
  // o konieczności wykonania próby i „oczekuje”
  // na ich wynik (typu Option[Ocena])
  case object Results

  // Polecenie zwrócenia aktualnego rankingu Grupy
  // Oczywiście klasyfikowani są jedynie Zawodnicy,
  // którzy pomyślnie ukończyli swoją próbę
  case class Results(result: (Person, Option[Grade], ActorRef))

  // Informacja o wyniku Zawodnika (wysyłana przez Zawodnika do Grupy)
  // np. Wynik(Some(Ocena(10, 15, 14)))
  // Jeśli zawodnik nie ukończy próby zwracana jest wartość Wynik(None)
  case object End
  // Grupa kończy rywalizację
}

class Group(contestants: List[ActorRef]) extends Actor {

  import Group._

  def receive: Receive = eliminations(Map())

  def eliminations(results: Map[Person, (Grade, ActorRef)]): Receive = {
    case Round =>
      context.become(receivingResults(results))
      contestants.foreach(contestant => {
        contestant ! Contestant.Try
      })

    case Results =>
      println("Nie rozegrano jeszcze rundy.")

    case msg => println(msg)
  }

  def finals(results: List[(Person, (Grade, ActorRef))]): Receive = {
    case Results =>
      println()
      results.zipWithIndex.foreach(person => {
        val name = person._1._1.name
        val surname = person._1._1.surname

        val grade = person._1._2._1

        val note1 = grade.note1
        val note2 = grade.note2
        val note3 = grade.note3

        val sumOfNotes = note1 + note2 + note3

        println(s"${person._2 + 1}. $name $surname: $note1-$note2-$note3 = $sumOfNotes")
      })

    case Round =>
      context.become(receivingResultsFinals(results.toMap, 0))
      val top20Contestants = results.take(20).map(result => {
        result._2._2
      })

      top20Contestants.foreach(contestant => {
        contestant ! Contestant.Try
      })
  }

  def receivingResults(results: Map[Person, (Grade, ActorRef)]): Receive = {
    case Results(result) =>
      val person = result._1
      val grade = result._2
      val actor = result._3

      if (grade.getOrElse(None) == None) {
        val updatedResults = results.updated(person, (Grade(0, 0, 0), actor))

        if (updatedResults.size == contestants.length) {
          val sortedResults = Utl.sortResults(updatedResults)

          context.become(finals(sortedResults))
          context.parent ! Organiser.Results(sortedResults.toMap)
        } else context.become(receivingResults(updatedResults))
      } else {
        val updatedResults = results.updated(person, (grade.get, actor))

        if (updatedResults.size == contestants.length) {
          val sortedResults = Utl.sortResults(updatedResults)

          context.become(finals(sortedResults))
          context.parent ! Organiser.Results(sortedResults.toMap)
        } else context.become(receivingResults(updatedResults))
      }
  }

  def receivingResultsFinals(results: Map[Person, (Grade, ActorRef)], receivedResults: Int): Receive = {
    case Group.Results(result) =>
      val person = result._1
      val grade = result._2
      val actor = result._3

      if (grade.getOrElse(None) == None) {
        if (receivedResults + 1 == 20) {
          val sortedResults = Utl.sortResults(results)

          context.become(finals(sortedResults))
          context.parent ! Organiser.Results(sortedResults.toMap)
        } else context.become(receivingResultsFinals(results, receivedResults + 1))
      } else {
        val finalGrade = Grade(
          results(person)._1.note1 + grade.get.note1,
          results(person)._1.note2 + grade.get.note2,
          results(person)._1.note3 + grade.get.note3
        )
        val updatedResults = results.updated(person, (finalGrade, actor))

        if (receivedResults + 1 == 20) {
          val sortedResults = Utl.sortResults(updatedResults)

          context.become(finals(sortedResults))
          context.parent ! Organiser.Results(sortedResults.toMap)
        } else context.become(receivingResultsFinals(updatedResults, receivedResults + 1))
      }
  }
}

