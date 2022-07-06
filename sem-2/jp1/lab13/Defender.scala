package lab13

import akka.actor.{Actor, PoisonPill}

object Defender {
  case class Shot(numberOfDefenders: Int)
}

class Defender extends Actor {
  import Defender._

  def receive: Receive = {
    case Shot(numberOfDefenders) =>
      val randomNumberGenerator = scala.util.Random

      val deathChance = if (numberOfDefenders / 200.0 * 100 < 10) {
        10
      } else numberOfDefenders / 200.0 * 100
      if ((randomNumberGenerator.nextFloat() * 100).floor < deathChance.floor ) {
        self ! PoisonPill
      }
  }
}
