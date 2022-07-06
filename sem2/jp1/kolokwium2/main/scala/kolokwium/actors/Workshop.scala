package kolokwium.actors

import akka.actor.*

object Workshop {
  case object Tick

  case class Malfunction(car: ActorRef)
}

class Workshop extends Actor with ActorLogging {

  import Workshop._

  def receive: Receive = initialized(Set(), Set())

  def initialized(
                   setOfIncomingCarsAndDrivers: Set[(ActorRef, ActorRef)],
                   setOfCarsBeingRepaired: Set[((ActorRef, ActorRef), Int)]
                 ): Receive = {
    case Malfunction(car) =>
      val driver = sender()
      context.become(
        initialized(
          setOfIncomingCarsAndDrivers.incl((driver, car)),
          setOfCarsBeingRepaired
        ))
    case Tick =>
      val randomGenerator = scala.util.Random

      setOfCarsBeingRepaired.foreach(pair => {
        val tempSetOfCarsBeingRepaired = setOfCarsBeingRepaired.excl(pair)
        val repairTicks = pair._2

        if (repairTicks - 1 == 0) {
          context.become(
            initialized(setOfIncomingCarsAndDrivers, tempSetOfCarsBeingRepaired))

          val driver = pair._1._1
          val car = pair._1._2
          driver ! Driver.RepairResult(Some(car))
        }

        context.become(
          initialized(
            setOfIncomingCarsAndDrivers,
            tempSetOfCarsBeingRepaired.incl((pair._1, repairTicks - 1))
          )
        )
      })

      setOfIncomingCarsAndDrivers.foreach(pair => {
        if (randomGenerator.nextFloat() * 100 < 80) {
          context.become(
            initialized(
              setOfIncomingCarsAndDrivers.excl(pair),
              setOfCarsBeingRepaired.incl((pair, randomGenerator.nextInt(6) + 1))
            )
          )
        } else pair._2 ! Driver.RepairResult(None)
      })

    case msg =>
  }
}
