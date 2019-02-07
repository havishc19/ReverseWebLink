hadoop jar ./target/mapReduceWebLink-1.0.jar edu.gatech.AdvancedInternetComputing.MapReduceWebLink ./data/webLink.tsv ./data/output_webLink
hadoop fs -getmerge ./data/output_webLink/ output_webLink.tsv
hadoop fs -rm -r ./data/output_webLink
