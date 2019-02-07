package edu.gatech.AdvancedInternetComputing;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
// import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
// import org.apache.hadoop.mapreduce.Mapper;
// import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.*;
import org.apache.hadoop.mapreduce.lib.output.*;



import java.util.*; 

import org.apache.hadoop.util.*; 

public class MapReduceWebLink {

  public static class GraphMapper
       extends Mapper<Object, Text, Text, Text>{

    // private final static IntWritable one = new IntWritable(1);
    // private Text word = new Text();

  	public void map(Object key, Text value, Context context) throws IOException, InterruptedException  {
		String line = value.toString(); 
		String[] temp = line.split("\t");
		Text source = new Text(temp[0]);
		Text target = new Text(temp[1]);
		context.write(target, source); 
      }
    }

  public static class GraphReducer
       extends Reducer<Text,Text,Text,Text> {
	public void reduce(Text key, Iterable<Text> values,
                       Context context
                       ) throws IOException, InterruptedException {
      String finalVal = "[";
      for (Text val1 : values) {
        String val = val1.toString();
        finalVal = finalVal + val + ",";
      } 
      finalVal = finalVal.substring(0, finalVal.length() - 1) + "]";
      context.write(key, new Text(finalVal));
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "MapReduceWebLink");

    /* TODO: Needs to be implemented */

    job.setJarByClass(MapReduceWebLink.class);
    job.setMapperClass(GraphMapper.class);
    // job.setCombinerClass(GraphReducer.class);
    job.setReducerClass(GraphReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(Text.class);


    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
