package lab14.model

// Generator osób i ocen
object Utl {

  import java.time.Instant
  import java.util.Locale
  import org.scalacheck.rng.Seed
  import faker._

  def person(): Person = {
    val firstName: String = Faker.en_US.firstName()
    val lastName: String = Faker.en_US.lastName()
    Person(firstName, lastName)
  }

  import scala.util.Random

  val rand = new Random
  val trySuccessful = 0.05

  def grade(): Option[Grade] = {
    if (rand.nextDouble() > trySuccessful) {
      val nota1 = rand.nextInt(21)
      val nota2 = rand.nextInt(21)
      val nota3 = rand.nextInt(21)
      Some(Grade(nota1, nota2, nota3))
    } else {
      None
    }
  }

  import akka.actor.ActorRef

  def sortResults(results: Map[Person, (Grade, ActorRef) ]): List[(Person, (Grade, ActorRef))] = {
    results.toList.sortWith((result1, result2) => {
      val grade1 = result1._2._1
      val grade2 = result2._2._1

      val sum1 = grade1.note1 + grade1.note2 + grade1.note3
      val sum2 = grade2.note1 + grade2.note2 + grade2.note3

      if (sum1 != sum2) {
        if (sum1 > sum2) true
        else false
      } else {
        if (grade1.note1 != grade2.note1) {
          if (grade1.note1 > grade2.note1) true
          else false
        } else {
          if (grade1.note3 > grade2.note3) true
          else false
        }
      }
    })
  }

}

