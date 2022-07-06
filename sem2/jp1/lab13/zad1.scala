package lab13

import akka.actor.{ActorSystem, Actor, Props}
import scala.concurrent.duration._

@main
def lab13zad1(): Unit = {
  val system = ActorSystem("Jabberwocky")
  import system.dispatcher

  val greaterPower = system.actorOf(Props[GreaterPower](), "greaterPower")

  greaterPower ! GreaterPower.Init

  // Do „animacji” SiłyWyższej wykorzystamy „Planistę” (Scheduler)
  system.scheduler.scheduleWithFixedDelay(
    Duration.Zero,     // opóźnienie początkowe
    1000.milliseconds, // odstęp pomiedzy kolejnymi komunikatami
    greaterPower,      // adresat „korespondencji”
    GreaterPower.Tick  // komunikat
  )
}
