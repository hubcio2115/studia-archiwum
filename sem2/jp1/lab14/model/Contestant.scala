package lab14.model

import akka.actor.Actor

object Contestant {
  case object Try
  // polecenie wykonania próby (kończy się zwróceniem Wyniku,
  // za pomocą komunikatu Grupa.Wynik)
}

class Contestant(person: Person) extends Actor {
  import Contestant._

//  override def preStart(): Unit = {
//    println(s"${self.path}")
//  }

  def receive: Receive = {
    case Try =>
      val grade = Utl.grade()

      sender() ! Group.Results((person, grade, self))
    case msg => println(s"[${self.path.name}] otrzymano błędny komunikat ")
  }
}
