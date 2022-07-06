package lab14

// „Interfejs użytkownika” wymaga pewnych dodatkowych elementów:

import scala.concurrent.ExecutionContext
import scala.util.control.Breaks._
import scala.io.StdIn

import akka.actor.{ActorSystem, Props}

import model.*

@main
def competition(): Unit = {

  val system = ActorSystem("system")
  val organiser = system.actorOf(Props[Organiser](), "organiser")

  // Interfejs „organizatora”:
  implicit val ec: ExecutionContext = ExecutionContext.global

  breakable {
    while (true) {
      StdIn.readLine("polecenie: ") match {
        case "start" =>
          organiser ! Organiser.Start
        case "eliminacje" =>
          // polecenie rozegrania rundy eliminacyjnej
          organiser ! Organiser.Round
        case "finał" =>
          // polecenie rozegrania rundy finałowej
          // wymaga zamknięcia Rundy eliminacyjnej i utworzenie
          // Rundy finałowej, zawierającej najlepszych 20.
          // zawodników z Rundy eliminacyjnej
          organiser ! Organiser.Round
        case "wyniki" =>
          // żądanie rankingów (lub rankingu finałowego)
          organiser ! Organiser.Results
        case "stop" =>
          organiser ! Organiser.Stop
          break()
        case _ =>
          println("błędny komunikat")
      }
    }
  }
}
