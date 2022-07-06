package kolokwium.actors

import akka.actor._

object Car {
  case object Next
}

class Car extends Actor with ActorLogging {
  import Car._

  def receive: Receive = {
    case Next =>
      val randomGenerator = scala.util.Random

      if (randomGenerator.nextFloat * 100 > 15) {
        val speed = randomGenerator.nextInt(200)

        sender() ! Driver.CarReaction(Some(speed))
      } else sender() ! Driver.CarReaction(None)
  }
}
