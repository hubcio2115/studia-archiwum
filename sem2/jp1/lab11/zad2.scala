package lab11

import akka.actor.{Actor, ActorRef, ActorSystem, Props}

case class Ball2(max: Int, i: Int)
case class Play2(opponent: ActorRef, max: Int)

class Player2 extends Actor {
  def receive: Receive = {
    case Play2(actor, max) =>
      actor ! Ball2(max, 1)
    case Ball2(max, i) =>
      if (i > max) context.system.terminate()
      else {
        println(s"Piłeczka ${self.path.name}")
        sender() ! Ball2(max, i + 1)
      }
  }
}

@main
def lab11zad2(): Unit = {
  val system = ActorSystem("tableTennis")

  val player1Ref = system.actorOf(Props[Player2](), "player1")
  val player2Ref = system.actorOf(Props[Player2](), "player2")

  player1Ref ! Play2(player2Ref, 6)
}
