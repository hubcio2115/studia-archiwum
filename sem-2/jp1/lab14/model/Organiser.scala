package lab14.model

import akka.actor.{Actor, ActorRef, Props}

val akkaPathAllowedChars = ('a' to 'z').toSet union
  ('A' to 'Z').toSet union
  "-_.*$+:@&=,!~';.)".toSet

object Organiser {
  // rozpoczynamy zawody – losujemy 50 osób, tworzymy z nich zawodników
  // i grupę eliminacyjną
  case object Start

  // polecenie rozegrania rundy (kwalifikacyjnej bądź finałowej) –  wysyłamy Grupa.Runda
  // do aktualnej grupy
  case object Round

  // polecenie wyświetlenia klasyfikacji dla aktualnej grupy
  case object Results

  // wyniki zwracane przez Grupę
  case class Results(results: Map[Person, (Grade, ActorRef)])

  // kończymy działanie
  case object Stop
}

class Organiser extends Actor {
  // importujemy komunikaty na które ma reagować Organizator

  import Organiser._

  def receive: Receive = {
    case Start =>
      // tworzenie 50. osób, opdowiadających im Zawodników
      // oraz Grupy eliminacyjnej
      val contestants = (1 to 50).map(_ =>{
        val person = Utl.person()
        context.actorOf(Props(Contestant(person)), s"${person.name}-${person.surname}" filter akkaPathAllowedChars)
      }).toList

      val group = context.actorOf(Props(new Group(contestants)), "group")

      context.become(eliminations(group))

    case Stop =>
      println("kończymy zawody...")
      context.system.terminate()

    case _ =>
      println(s"[organiser] otrzymano błędny komunikat")
  }

  def eliminations(group: ActorRef): Receive = {
    case Round =>
      group ! Group.Round
    case Results =>
      group ! Group.Results
    case Results(results) =>
       context.become(finals(group))
    case Stop =>
      println("kończymy zawody...")
      context.system.terminate()
  }

  def finals(group: ActorRef): Receive = {
    case Results =>
      group ! Group.Results
    case Round =>
      group ! Group.Round
    case Results(_) =>
      context.become(finished(group))
    case Stop =>
      println("kończymy zawody...")
      context.system.terminate()
  }

  def finished(group: ActorRef): Receive = {
    case Results =>
      group ! Group.Results
    case Stop =>
      println("kończymy zawody...")
      context.system.terminate()
  }
}
