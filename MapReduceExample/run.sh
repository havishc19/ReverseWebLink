hadoop jar ./target/mapReduce-1.0.jar edu.gatech.AdvancedInternetComputing.MapReduce ./data/graph.tsv ./data/output
hadoop fs -getmerge ./data/output/ output.tsv
hadoop fs -rm -r ./data/output
