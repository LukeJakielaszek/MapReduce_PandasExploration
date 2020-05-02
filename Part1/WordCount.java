import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

    // mapping class
    public static class TokenizerMapper
	extends Mapper<Object, Text, Text, IntWritable>{
	
	// incrementing variable
	private final static IntWritable one = new IntWritable(1);

	// current word
	private Text word = new Text();
	private String prev = null;
	
	// map each word to a number of occurences
	public void map(Object key, Text value, Context context
			) throws IOException, InterruptedException {
	    // get assigned text
	    StringTokenizer itr = new StringTokenizer(value.toString());

	    // loop through each word
	    while (itr.hasMoreTokens()) {
		if(prev == null){
		    // store current word
		    prev = itr.nextToken();

		    // skip the first word
		    continue;
		}
		
		// prepare our string builder
		StringBuilder sb = new StringBuilder();		

		// start our bigram
		sb.append(prev);

		// add a whitespace delimiter
		sb.append(" ");
		
		// update to the new word
		prev = itr.nextToken();

		// add the new word
		sb.append(prev);

		// set the bigram to our string
		word.set(sb.toString());

		// append map with one
		context.write(word, one);
	    }
	}
    }

    // reducer class
    public static class IntSumReducer
	extends Reducer<Text,IntWritable,Text,IntWritable> {

	// sum variable
	private IntWritable result = new IntWritable();

	// combine maps with same key
	public void reduce(Text key, Iterable<IntWritable> values,
			   Context context
			   ) throws IOException, InterruptedException {
	    // get the combined count for each key in the map by looping over list of values
	    int sum = 0;
	    for (IntWritable val : values) {
		sum += val.get();
	    }

	    // store the sum in our reduced map
	    result.set(sum);
	    context.write(key, result);
	}
    }
    
    public static void main(String[] args) throws Exception {
	// get a job with our defined configuration
	Configuration conf = new Configuration();
	Job job = Job.getInstance(conf, "word count");
	
	// define the types of our mappers and reducers
	job.setJarByClass(WordCount.class);
	job.setMapperClass(TokenizerMapper.class);
	job.setCombinerClass(IntSumReducer.class);
	job.setReducerClass(IntSumReducer.class);
	
	// define 5 reducers
	job.setNumReduceTasks(5);
	
	// define our map key/value types
	job.setOutputKeyClass(Text.class);
	job.setOutputValueClass(IntWritable.class);
	
	// define where input / output is placed
	FileInputFormat.addInputPath(job, new Path(args[0]));
	FileOutputFormat.setOutputPath(job, new Path(args[1]));
	
	// wait for the job to finish
	System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
