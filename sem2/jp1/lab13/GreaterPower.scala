package lab13

import akka.actor.{Actor, ActorRef, Props}
import lab13.Castle._

object GreaterPower {
  case object Init
  case object Tick
}

class GreaterPower extends Actor {
  import GreaterPower._

  def receive: Receive = {
    case Init =>
      val castle1 = context.actorOf(Props[Castle](), "castle1")
      val castle2 = context.actorOf(Props[Castle](), "castle2")

      castle1 ! Castle.Init
      castle2 ! Castle.Init

      context.become(Fighting(List(castle1, castle2)))
  }

  def Fighting(castles: List[ActorRef]): Receive = {
    case Tick =>
      val castle1 = castles.head
      val castle2 = castles(1)

      castle1 ! Castle.Fight
      castle2 ! Castle.Fight
  }
}
