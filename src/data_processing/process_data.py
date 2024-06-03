from pyspark.sql import SparkSession
import json

def main():
    with open('config/config.json') as f:
        config = json.load(f)

    spark = SparkSession.builder \
        .appName("DataProcessing") \
        .getOrCreate()

    # Read data from ADLS
    input_path = config["input_path"]
    df = spark.read.csv(input_path, header=True)

    # Data processing steps
    df_processed = df.withColumn("processed_column", df["column"] * 2)

    # Write data to Azure Synapse
    output_path = config["output_path"]
    df_processed.write \
        .format("com.databricks.spark.sqldw") \
        .option("url", config["synapse_url"]) \
        .option("tempDir", config["temp_dir"]) \
        .option("forwardSparkAzureStorageCredentials", "true") \
        .option("dbTable", config["synapse_table"]) \
        .save()

if __name__ == "__main__":
    main()
