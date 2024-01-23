from pyspark.sql import SparkSession
# initialyse spark session

def get_file_size(file_path):
    # returns the file size in kilobytes
    return "filesize"

def calculate_spark_configurations(file_size):
    # Define thresholds for different file size categories
    # adding thrashold based on our neeed
    # example below
    small_file_threshold = 10  # in KiBs
    medium_file_threshold = 100000  # in kib equal to 100 MB

    # category of the file based on its size
    if file_size <= small_file_threshold:
        # Configure Spark for small files
        spark_configs = {
            "spark.executor.instances": 1,
            "spark.executor.memory": "1g",
            # we can also add more configs based on our needs
        }
    elif small_file_threshold < file_size <= medium_file_threshold:
        # Configure Spark for medium files
        spark_configs = {
            "spark.executor.instances": 5,
            "spark.executor.memory": "4g",
            # Add more
        }
    else:
        # Configure Spark for large files
        spark_configs = {
            "spark.executor.instances": 10,
            "spark.executor.memory": "8g",
        }

    return spark_configs

def process_input_file(file_path):
    # Get the size of the input file
    file_size = get_file_size(file_path)

    # call the config calculation
    spark_configs = calculate_spark_configurations(file_size)

    # Initialize Spark session with dynamically adjusted configurations
    spark = SparkSession.builder.appName("DynamicConfigExample").config(
        **spark_configs
    ).getOrCreate()

    # implement ETL processing logic using the spark session
    # Stop the Spark session
    spark.stop()


# testing
input_file_path = "myfile"
process_input_file(input_file_path)