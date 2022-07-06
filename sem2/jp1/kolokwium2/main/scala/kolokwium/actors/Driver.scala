package kolokwium.actors

import akka.actor._

object Driver {
  case object Tick

  case object SetupCar

  case class CarReaction(ov: Option[Int])

  case object GetRoute

  case class RepairResult(effect: Option[ActorRef])
}

class Driver(workshop: ActorRef, dt: Int) extends Actor with ActorLogging {
  import Driver._

  def receive: Receive = {
    case SetupCar =>
      val car = context.actorOf(Props[Car](), "car")

      context.become(setup(car, 0))
  }

  def setup(car: ActorRef, distance: Float): Receive = {
    case Tick =>
      car ! Car.Next

    case CarReaction(reaction) =>
      if (reaction.getOrElse(None) != None) {
        val speed = reaction.get

        val time = dt.toFloat / 60
        val s = distance + (speed * time)

        context.become(setup(car, s))
      } else {
        context.become(carBroken(car, distance))
        workshop ! Workshop.Malfunction(car)
      }

    case GetRoute =>
      sender() ! Organiser.RouteTraveled(distance)

    case msg =>
  }

  def carBroken(car: ActorRef, distance: Float): Receive = {
    case RepairResult(repairResult) =>
      if (repairResult.getOrElse(None) != None) {
        context.become(setup(car, distance))
      } else context.become(finishedRace(distance))

    case GetRoute =>
      sender() ! Organiser.RouteTraveled(distance)

    case msg =>
  }

  def finishedRace(distance: Float): Receive = {
    case GetRoute =>
      sender() ! Organiser.RouteTraveled(distance)

    case msg =>
  }
}
