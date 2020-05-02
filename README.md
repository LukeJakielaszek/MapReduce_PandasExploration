# Final Exam Instructions

## Part 1
I have already went into detail on how to set up and run mapreduce with images in my final report. Therefore, I will only go over the basic steps below:<br/>

1) Create a T2.large EC2 instance with access anywhere enabled and an IAM role attached that has administrator access for EC2.

2) Log in as a super user:
sudo su

3) Download Hadoop using:
wget https://archive.apache.org/dist/hadoop/core/hadoop-2.7.3/hadoop-2.7.3.tar.gz 
tar -xvf Hadoop-2.7.2.tar.gz 

4) Download Java using:
wget -c --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otnpub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz 
tar -xvf jdk-8u131-linux-x64.tar.gz 

5) Update bashrc with the following variables:
export HADOOP_HOME=/home/ubuntu/hadoop-2.6.0
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib"
export JAVA_HOME=/usr/lib/jvm/java-8-oracle
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar
PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

6) Run the bashrs with source ~/.bashrc

7) Enable passwordless SSH using:
ssh-keygen -t rsa -P '' 
cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys 

8) Configure core-site.xml with the following properties:
<property>
		<name>hadoop.tmp.dir</name>
		<value>/home/ubuntu/hadooptmp/hadoop-${user.name}</value>
		<description>A base for other temporary directories.</description>
	</property>
	<property>
		<name>fs.default.name</name>
		<value>hdfs://localhost:9000</value>
	</property>
  
  9) Add the following line to hadoop-env.sh:
  export JAVA_HOME=/home/ubuntu/jdk1.8.0_131
  
  10) Configure mapred-site.xml with the following properties:
  <property>
		<name>mapred.job.tracker</name>
		<value>localhost:9001</value>
	</property>
  
  11) Configure yarn-site.xml with the following properties:
  <property>
	<name>yarn.nodemanager.aux-services</name>
	<value>mapreduce_shuffle</value>
</property>
  
  12) Create a hadoop data directory for the HDFS using mkdir ~/hadoopdata and configure hdfs-site.xml with the following properties:
  <property>
		<name>dfs.replication</name>
		<value>1</value>
	</property>
	<property><name>dfs.name.dir</name>
		<value>file:///home/ubuntu/hadoopdata/hdfs/namenode</value>
	</property>
	<property>
		<name>dfs.data.dir</name>
		<value>file:///home/ubuntu/hadoopdata/hdfs/datanode</value>
	</property>
  
  13) Format the NameNode using:
  hdfs namenode -format
  
  14) Start the NameNodes and DataNode by running the start-dfs.sh script
  
  15) Start the ResourceManager and NodeManager by running the start-yarn.sh script
  
  16) Compile the WordCount Java Program (this has been converted to a bigram counter:
  Hadoop-2.7.3/bin/hadoop com.sun.tools.javac.Main WordCount.java 
  jar cf wc.jar WordCount*.class 
  
  17) Create an input directory for the MapReduce program:
  hdfs dfs -mkdir /input
  
  18) Add the text file to the input directory:
  hdfs dfs -put myfile.txt /input
  
  19) Run the MapReduce Java program:
  jar wc.jar WordCount /input /output
  
  20) Retreive the output partitions (you should put these in a directory below the processing.py script called hadoop_data. In this instance processing.py would be in output_dir/processing/processing.py and the partitions are in output_dir/processing/hadoop_data/part-*):
  hdfs dfs -get /output/part-* output_dir/processing/hadoop_data
  
  21) Run the processing.py script from the processing directory:
  python3 processing.py
  
  22) View the answers to all problems of Part 1 for the final exam
  
## Part 2 
