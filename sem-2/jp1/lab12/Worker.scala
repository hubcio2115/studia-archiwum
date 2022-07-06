package lab12

import akka.actor.{Actor, ActorRef, Props}

object Worker {
  case class Do(line: String)
}

class Worker extends Actor {
  import Worker._

  def receive: Receive = receivingWork

  def receivingWork: Receive = {
    case Do(line) =>
      val numberOfWords = line.split(" ").length
      sender() ! Boss.Result(numberOfWords)
  }
}
