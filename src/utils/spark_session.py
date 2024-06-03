from pyspark.sql import SparkSession

def create_spark_session(app_name="MyApp"):
    return SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()
