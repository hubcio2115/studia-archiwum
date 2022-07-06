package lab8.zad2

class Competitor(val name: String, val charmScore: List[Int] = Nil, val cunningScore: List[Int] = Nil) {
  def getAverageCharmScore: Double = {
    charmScore.sum / charmScore.length
  }

  def getAverageCunningScore: Double = {
    cunningScore.sum / cunningScore.length
  }
}
