# Final Exam Instructions

## Part 1
I have already went into detail on how to set up and run mapreduce with images in my final report. Therefore, I will only go over the basic steps below:<br/>

1) Create a T2.large EC2 instance with access anywhere enabled and an IAM role attached that has administrator access for EC2.

2) Log in as a super user:<br/>
sudo su

3) Download Hadoop using:<br/>
wget https://archive.apache.org/dist/hadoop/core/hadoop-2.7.3/hadoop-2.7.3.tar.gz <br/>
tar -xvf Hadoop-2.7.2.tar.gz <br/>

4) Download Java using:<br/>
wget -c --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otnpub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz <br/>
tar -xvf jdk-8u131-linux-x64.tar.gz <br/>

5) Update bashrc with the following variables:<br/>
export HADOOP_HOME=/home/ubuntu/hadoop-2.6.0<br/>
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native<br/>
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib"<br/>
export JAVA_HOME=/usr/lib/jvm/java-8-oracle<br/>
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar<br/>
PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin<br/>

6) Run the bashrs with source ~/.bashrc<br/>

7) Enable passwordless SSH using:<br/>
ssh-keygen -t rsa -P '' <br/>
cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys <br/>

8) Configure core-site.xml with the following properties:<br/>
<property><br/>
		<name>hadoop.tmp.dir</name><br/>
		<value>/home/ubuntu/hadooptmp/hadoop-${user.name}</value><br/>
		<description>A base for other temporary directories.</description><br/>
	</property><br/>
	<property><br/>
		<name>fs.default.name</name><br/>
		<value>hdfs://localhost:9000</value><br/>
	</property><br/>
  
  9) Add the following line to hadoop-env.sh:<br/>
  export JAVA_HOME=/home/ubuntu/jdk1.8.0_131<br/>
  
  10) Configure mapred-site.xml with the following properties:<br/>
  <property><br/>
		<name>mapred.job.tracker</name><br/>
		<value>localhost:9001</value><br/><br/>
	</property><br/>
  
  11) Configure yarn-site.xml with the following properties:<br/>
  <property><br/>
	<name>yarn.nodemanager.aux-services</name><br/>
	<value>mapreduce_shuffle</value><br/>
</property><br/>
  
  12) Create a hadoop data directory for the HDFS using mkdir ~/hadoopdata and configure hdfs-site.xml with the following properties:<br/>
  <property><br/>
		<name>dfs.replication</name><br/>
		<value>1</value><br/>
	</property><br/>
	<property><name>dfs.name.dir</name><br/>
		<value>file:///home/ubuntu/hadoopdata/hdfs/namenode</value><br/>
	</property><br/>
	<property><br/>
		<name>dfs.data.dir</name><br/>
		<value>file:///home/ubuntu/hadoopdata/hdfs/datanode</value><br/>
	</property><br/>
  
  13) Format the NameNode using:<br/>
  hdfs namenode -format<br/>
  
  14) Start the NameNodes and DataNode by running the start-dfs.sh script<br/>
  
  15) Start the ResourceManager and NodeManager by running the start-yarn.sh script<br/>
  
  16) Compile the WordCount Java Program (this has been converted to a bigram counter:<br/>
  Hadoop-2.7.3/bin/hadoop com.sun.tools.javac.Main WordCount.java <br/>
  jar cf wc.jar WordCount*.class <br/>
  
  17) Create an input directory for the MapReduce program:<br/>
  hdfs dfs -mkdir /input<br/>
  
  18) Add the text file to the input directory:<br/>
  hdfs dfs -put myfile.txt /input<br/>
  
  19) Run the MapReduce Java program:<br/>
  jar wc.jar WordCount /input /output<br/>
  
  20) Retreive the output partitions (you should put these in a directory below the processing.py script called hadoop_data. In this instance processing.py would be in output_dir/processing/processing.py and the partitions are in output_dir/processing/hadoop_data/part-*):<br/>
  hdfs dfs -get /output/part-* output_dir/processing/hadoop_data<br/>
  
  21) Run the processing.py script from the processing directory:<br/>
  python3 processing.py<br/>
  
  22) View the answers to all problems of Part 1 for the final exam<br/>
  
## Part 2 
