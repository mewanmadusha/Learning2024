from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import Row

# Set up the Spark configuration
conf = SparkConf().setAppName("Test").setMaster("local[1]")
sc = SparkContext(conf=conf)
spark = SparkSession(sc)

# Execution time measurement for code blocks
def time(block):
    import time
    t0 = time.time()
    result = block()
    t1 = time.time()
    print("Elapsed time:", (t1 - t0), "seconds")
    return result

def unoptimalCode1(text):
    # Ignore empty lines
    nonEmptyLines = text.filter(lambda x: len(x.strip()) > 0)

    # Get first tab-separated token from each line (code)
    codes = nonEmptyLines.map(lambda x: x.split('\t')[0])

    # Codes grouped by 2 first characters
    groupedCodes = codes.groupBy(lambda x: x[:2])

    # Compute sizes of all groups
    groupSizes = groupedCodes.map(lambda group: (group[0], len(group[1])))

    # Sort groups by sizes descending
    sortedGroups = groupSizes.sortBy(lambda x: x[1], ascending=False)

    # Get 3 groups with most members
    top3Groups = sortedGroups.map(lambda x: x[0]).take(3)

    # Sort groups by sizes ascending
    sortedGroupsAsc = groupSizes.sortBy(lambda x: x[1])

    # Get 3 groups with least members
    bottom3Groups = sortedGroupsAsc.map(lambda x: x[0]).take(3)

    return top3Groups, bottom3Groups

def optimalCode1(text):
    # Ignore empty lines and get the first tab-separated token
    codes = (
        text.filter(lambda x: len(x.strip()) > 0)
        .map(lambda x: (x.split('\t')[0][:2], 1))  # Map to (code_prefix, 1) pairs
    )

    # use shuffeling to reduce shuffeled data
    # Use reduceByKey to efficiently calculate group sizes
    # also use aggregate data based on keys
    groupSizes = codes.reduceByKey(lambda x, y: x + y)

    # Get the 3 groups with the most members
    # takeOrdered used to get specified number of elements from data
    top3Groups = groupSizes.takeOrdered(3, key=lambda x: -x[1])

    # Get the 3 groups with the least members
    bottom3Groups = groupSizes.takeOrdered(3, key=lambda x: x[1])

    return [group[0] for group in top3Groups], [group[0] for group in bottom3Groups]


# def unoptimalCode2(crimesDb, commitedCrimes):
#     # TODO: Implement unoptimalCode2
#     pass

def optimalCode2(crimesDb, commitedCrimes):
    # use shared variable
    # Broadcast crimesDb to all worker nodes for efficient lookup
    crimesBroadcast = sc.broadcast(set(crimesDb.collect()))

    # caching
    # Filter commited crimes using broadcasted crimesDb for efficient lookup
    # if we run this code second time it take much less time
    matchingCrimes = commitedCrimes.filter(lambda x: x in crimesBroadcast.value)

    return matchingCrimes

if __name__ == "__main__":
    # Read text into RDD
    crimeCategories = sc.textFile("ucr_ncic_codes.tsv")

    # Measure time for unoptimalCode1
    top, bottom = time(lambda: unoptimalCode1(crimeCategories))
    print(f"({','.join(top)}...{','.join(bottom[::-1])})")

    # Measure time for optimalCode1
    top2, bottom2 = time(lambda: optimalCode1(crimeCategories))
    print(f"({','.join(top)}...{','.join(bottom[::-1])})")

    # Read commited crimes data
    commitedCrimes = sc.textFile("SacramentocrimeJanuary2006.csv")

    # Measure time for unoptimalCode2
    time(lambda: optimalCode2(crimeCategories, commitedCrimes))