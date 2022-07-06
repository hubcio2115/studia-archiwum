package kolokwium.actors

import akka.actor.*

object Organiser {
  case class SetMaxTick(maxTick: Int) {
    assert(maxTick > 0)
  }

  case object Tick

  case class RouteTraveled(numberOfKm: Float)
}

class Organiser extends Actor with ActorLogging {
  import Organiser._

  def receive: Receive = {
    case SetMaxTick(mc) =>
      log.info(s"liczba cyknięć do wykonania: $mc")

      val workshop = context.actorOf(Props[Workshop](), "workshop")

      val dt = scala.util.Random.nextInt(10)

      val driversSet = (0 to 10).map(index => {
        context.actorOf(Props(new Driver(workshop, dt)), s"driver$index")
      }).toSet

      driversSet.foreach(driver => {
        driver ! Driver.SetupCar
      })

      context.become(afterInit(mc, 0, workshop, driversSet))
    case _ => // inne pomijamy
  }

  def afterInit(maxTick: Int, currentTicks: Int, workshop: ActorRef, driverSet: Set[ActorRef]): Receive = {
    case Tick =>
      log.info("Tick")
      if (maxTick == currentTicks + 1 ) {
        context.become(finishedRace(Set(), driverSet.toList))

        driverSet.foreach(driver => {
          driver ! Driver.GetRoute
        })
      } else {
        context.become(afterInit(maxTick, currentTicks + 1, workshop, driverSet))
        workshop ! Workshop.Tick

        driverSet.foreach(driver => {
          driver ! Driver.Tick
        })
      }
  }

  def finishedRace(distances: Set[(ActorRef, Float)], driverList: List[ActorRef]): Receive = {
    case RouteTraveled(distance) =>
      if (driverList.drop(1).isEmpty) {
        val leaderboard = distances.incl((sender(), distance)).toList.sortBy(pair => pair._2).reverse

        leaderboard.zipWithIndex.foreach(pair => {
          println(s"${pair._2 + 1}. ${pair._1._1.path.name} - ${BigDecimal(pair._1._2).setScale(2, BigDecimal.RoundingMode.HALF_UP).toDouble}km")
        })

        context.system.terminate()
      } else context.become(
        finishedRace(
          distances.incl((sender(), distance)),
          driverList.drop(1)
        )
      )
    case msg =>
  }
}
