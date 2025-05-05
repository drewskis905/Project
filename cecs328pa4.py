#Andrew Pham
from pyspark.sql import SparkSession
import os
import glob

def sort_csv(input_file, output_file, num_partitions):
    spark = SparkSession.builder.appName("SortLargeCSV").getOrCreate()

    df = spark.read.csv(
        path=input_file,
        header=True,
        inferSchema=True,
        sep=","  
    )

    df = df.repartition(num_partitions, "column_1")

    sorted_df = df.sort("column_1")

    tmp_dir = output_file + "_tmp"
    sorted_df.coalesce(1).write.csv(
        path=tmp_dir,
        header=False,
        mode="overwrite"
    )

    part_path = glob.glob(os.path.join(tmp_dir, "part-*.csv"))[0]

    final_file = output_file if output_file.lower().endswith('.csv') else output_file + '.csv'
    os.rename(part_path, final_file)

    for f in glob.glob(os.path.join(tmp_dir, "*")):
        os.remove(f)
    os.rmdir(tmp_dir)

    spark.stop()