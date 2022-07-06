package lab13

import scala.concurrent.duration._
import concurrent.ExecutionContext.Implicits.global
import akka.actor.{ActorSystem, Props}
import lab13.GreaterPower._

@main
def main(): Unit = {
  val system = ActorSystem("system")

  val greaterPower = system.actorOf(Props[GreaterPower](), "greaterPower")

  greaterPower ! GreaterPower.Init

  system.scheduler.scheduleWithFixedDelay(
    Duration.Zero,
    1000.milliseconds,
    greaterPower,
    GreaterPower.Tick
  )
}
