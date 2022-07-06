package lab12
import akka.actor._

object Boss {
  case class Init(numberOfWorkers: Int)
  case class Result(number: Int)
  case class Work(text: List[String])
}

class Boss extends Actor {
  import Boss._

  def receive: Receive = {
    case Init(numberOfWorkers) =>
      val listOfReferences = (0 to numberOfWorkers).map(_ => context.actorOf(Props[Worker]())).toList
      context.become(givingWork(listOfReferences))
  }

  def givingWork(listOfReferences: List[ActorRef]): Receive = {
    case Work(text) =>
      context.become(receivingResults(listOfReferences, text.length, 0, 0))

      text.zipWithIndex.foreach(pair => {
        listOfReferences(pair(1) % listOfReferences.length) ! Worker.Do(pair(0))
      })
  }

  def receivingResults(listOfReferences: List[ActorRef], numberOfTextLines: Int, whichLine: Int, counter: Int): Receive = {
    case Result(number) =>
      if (numberOfTextLines == whichLine + 1) {
        println(counter + number)
        context.become(givingWork(listOfReferences))
      }

      context.become(receivingResults(listOfReferences, numberOfTextLines, whichLine + 1, counter + number))
  }
}

object Worker {
  case class Do(text: String)
}

class Worker extends Actor {
  import Worker._

  def receive: Receive = {
    case Do(text) => sender() ! Boss.Result(text.split(" ").length)
  }
}

@main
def lab12zad1(): Unit = {
  val data: List[String] = scala.io.Source.fromResource("./lab12/resources/ogniem_i_mieczem.txt").getLines.toList

  val system = ActorSystem("system")

  val boss = system.actorOf(Props[Boss](), "boss")
  boss ! Boss.Init(5)
  boss ! Boss.Work(data)
}
