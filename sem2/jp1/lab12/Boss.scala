package lab12

import akka.actor.{Actor, ActorRef, Props}

object Boss {
  case class Init(numberOfWorkers: Int)
  case class Order(text: List[String])
  case class Result(result: Int)
}

class Boss extends Actor {
  import Boss._

  def receive: Receive = {
    case Init(numberOfWorkers) =>
      val workerRefs = (0 to numberOfWorkers).map(index => context.actorOf(Props[Worker](), s"worker$index")).toList

      context.become(receivingOrder(workerRefs))
  }

  def receivingOrder(workerRefs: List[ActorRef]): Receive = {
    case Order(text) =>
      context.become(receivingResults(workerRefs, 0, text))

      text.zipWithIndex.foreach(pair => {
        val indexOfWorker = pair._2 % (workerRefs.length - 1)
        workerRefs(indexOfWorker) ! Worker.Do(pair._1)
      })
  }

  def receivingResults(workerRefs: List[ActorRef], numberOfLines: Int, text: List[String]): Receive = {
    case Result(result) =>
      if (text.drop(1).isEmpty) {
        println(s"Liczba linijek: ${numberOfLines + result}")

        context.become(receivingOrder(workerRefs))
      } else {
        context.become(receivingResults(workerRefs, numberOfLines + result, text.drop(1)))
      }
  }
}
