package lab11

import akka.actor.{ActorSystem, Actor, ActorRef, Props}

object Ball1
case class Play1(opponent: ActorRef)

class Player1 extends Actor {

  def receive: Receive = {
    case Play1(actor) => actor ! Ball1
    case Ball1 =>
      println(s"Piłeczka ${self.path.name}")
      sender() ! Ball1
  }
}

@main
def lab11zad1(): Unit = {
  val system = ActorSystem("tableTennis")
  val player1 = system.actorOf(Props[Player1](), "player1")
  val player2 = system.actorOf(Props[Player1](), "player2")

  player1 ! Play1(player2)
}
