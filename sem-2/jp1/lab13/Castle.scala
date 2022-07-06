package lab13

import akka.actor.{Actor, ActorRef, Props, Terminated}
import lab13.Defender

object Castle {
  case object Init
  case object Fight
}

class Castle extends Actor {
  import Castle._

  def receive: Receive = {
    case Init =>
      val listOfDefenders = (1 to 100).map(index => {
        val defender = context.actorOf(Props[Defender](), s"defender$index")
        context.watch(defender)

        defender
      }).toList

      context.become(Fighting(listOfDefenders))
  }

  def Fighting(listOfDefenders: List[ActorRef]): Receive = {
    case Fight =>
      println(s"${self.path.name}: ${listOfDefenders.length} defenders")

      listOfDefenders.foreach(defender => {
        defender ! Defender.Shot(listOfDefenders.length)
      })
    case Terminated(defender: ActorRef) =>
      val newListOfDefenders = listOfDefenders.filter(p => p != defender)


      if (newListOfDefenders.isEmpty) {
        println(s"\n${self.path.name} lost")
        context.system.terminate()
        System.exit(0)
      } else {
        context.become(Fighting(newListOfDefenders))
      }
  }
}
