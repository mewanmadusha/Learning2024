

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.rdd.RDD

import scala.language.postfixOps

object Task3 {
  val sc: SparkContext = new SparkContext(new SparkConf().setAppName("Test").setMaster("local[1]"))

  // Execution time measurement for code blocks
  def time[R](block: => R): R = {
    val t0 = System.nanoTime()
    val result = block // call-by-name
    val t1 = System.nanoTime()
    println("Elapsed time: " + (t1 - t0) + "ns")
    result
  }

  def unoptimalCode1(text: RDD[String]): (Array[String], Array[String]) = {

    // ignore empty lines
    val nonEmptyLines = text.filter(_.nonEmpty)

    // get first tab separated token from each line (code)
    val codes = nonEmptyLines.map(_.split("\t").head)

    // codes grouped by 2 first characters
    val groupedCodes = codes.groupBy(_.substring(0, 2))

    // compute sizes of all groups
    val groupSizes = groupedCodes.map { case (group, members) => (group, members.size) }

    // sort groups by sizes descending
    val sortedGroups = groupSizes.sortBy(_._2, ascending = false)

    // get 3 groups with most members
    val top3Groups = sortedGroups.map(_._1).take(3)

    // sort groups by sizes ascending
    val sortedGroupsAsc = groupSizes.sortBy(_._2)

    // get 3 groups with least members
    val bottom3Groups = sortedGroupsAsc.map(_._1).take(3)

    (top3Groups, bottom3Groups)
  }

  // TODO: Improve unoptimalCode1. Implement and test optimalCode1
  // Requirement: Write more time efficient code
  // Hint: you probably want to use reduceByKey.
  // Hint2: what about persistence?
  // Hint3: Any other way how to get results?
  // Hint4: use sc.parallelize() when providing data for tests
  def optimalCode1(text: RDD[String]): (Array[String], Array[String]) = {
    //TODO: Insert Your code here!

    // TODO: REMOVE THIS AFTER PROPER SOLUTION
    (Array[String](), Array[String]())
  }

  // TODO: Rewrite optimalCode1 using aggregateByKey() instead of reduceByKey. Implement and test
  def optimalCode11(text: RDD[String]): (Array[String], Array[String]) = {
    //TODO: Insert Your code here!

    // TODO: REMOVE THIS AFTER PROPER SOLUTION
    (Array[String](), Array[String]())
  }

  def unoptimalCode2(crimesDb: RDD[String], commitedCrimes: RDD[String]): Unit = {

    case class Crime(code: String, code2: String, category: String, subcategory: String, level: String)
    case class CommitedCrime(cdatetime: String, address: String, district: String, beat: String, grid: String, crimedescr: String, ucr_ncic_code: String, latitude: String, longitude: String)

    // ignore empty lines
    val nonEmptyLines = crimesDb.filter(_.nonEmpty)

    // create RDD[Crime]
    val crimes = nonEmptyLines.map(line => {
      val cols = line.split("\t")
      Crime(cols(0), cols(1), cols(2), cols(3), cols(4))
    })

    var idx = 0

    // This function does processing and saving of data
    def addCommitedCrimes(commited: RDD[String]) = {

      // Map commited crimes with it's codes
      val codesCommited = commited.map(line => {
        val cols = line.split(",")
        // column 6 contains code
        (cols(6), CommitedCrime(cols(0), cols(1), cols(2), cols(3), cols(4), cols(5), cols(6), cols(7), cols(8)))
      })

      // combine each CommitedCrime with corresponding Crime by it's code
      val joinedCrimes = crimes.map(crime => (crime.code, crime)).join(codesCommited)

      // Store files in FS.
      joinedCrimes.map { case (_, (crime, commitedCrime)) => (commitedCrime.district, crime.category) }
        .reduceByKey(_ + "," + _)
        .saveAsTextFile("output/" + System.nanoTime() + "_output" + idx)
      idx += 1
    }

    // Code below simulates situation when new data comes in portions.
    // Think of it like each day you receive new data and need to process it and save the result
    val commitedCrimesParts = commitedCrimes.randomSplit(Array(.2, .2, .2, .2, .2))
    // 1st day data
    addCommitedCrimes(commitedCrimesParts(0))
    // 2nd day data
    addCommitedCrimes(commitedCrimesParts(1))
    // 3rd day data
    addCommitedCrimes(commitedCrimesParts(2))
    // 4th day data
    addCommitedCrimes(commitedCrimesParts(3))
    // 5th day data
    addCommitedCrimes(commitedCrimesParts(4))
  }

  // TODO: Improve unoptimalCode2. Implement and test optimalCode2
  // Requirement: Write more time efficient code
  // Hint: Use range partitioner
  // Hint1: Are there any other improvements?
  // Hint2: Do you need to persist something?
  def optimalCode2(crimesDb: RDD[String], commitedCrimes: RDD[String]): Unit = {

    // TODO: pre process crimesDB here

    var idx = 0

    // This function does processing and saving of data
    def addCommitedCrimes(commited: RDD[String]) = {

      // TODO: join commitedCrimes with Crimes DB by code
      // TODO: for each district create list of categories of commited crimes
      // TODO: resulting RDD assign to result value
      val result: RDD[String] = ???

      // Store results
      result.saveAsTextFile("output/" + System.nanoTime() + "_output" + idx)
      idx += 1
    }


    // DO NOT CHANGE CODE BELOW!
    // Code below simulates situation when new data comes in portions.
    // Think of it like each day you receive new data and need to process it and save the result
    val commitedCrimesParts = commitedCrimes.randomSplit(Array(.2, .2, .2, .2, .2))
    // 1st day data
    addCommitedCrimes(commitedCrimesParts(0))
    // 2nd day data
    addCommitedCrimes(commitedCrimesParts(1))
    // 3rd day data
    addCommitedCrimes(commitedCrimesParts(2))
    // 4th day data
    addCommitedCrimes(commitedCrimesParts(3))
    // 5th day data
    addCommitedCrimes(commitedCrimesParts(4))
  }

  def main(args: Array[String]): Unit = {

    // read text into RDD
    val crimeCategories = sc.textFile("ucr_ncic_codes.tsv")

    val (top, bottom) = time {
      unoptimalCode1(crimeCategories)
    }
    println("(" + top.mkString(",") + "..." + bottom.reverse.mkString(",") + ")")

    val commitedCrimes = sc.textFile("SacramentocrimeJanuary2006.csv")

    time {
      unoptimalCode2(crimeCategories, commitedCrimes)
    }
  }
}
