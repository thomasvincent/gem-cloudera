# gem-cloudera
A ruby gem to interact with the Cloudera REST API

API access to Cloudera Manager
Cloudera Manager's REST API lets you work with existing tools, and programmatically manage your Hadoop clusters. The API is available in both Cloudera Express and Cloudera Enterprise, and comes with open-source client libraries. The goal of this project is to provide a ruby gem that can be used to manage Cloudera Hadoop installtions. 

Here are some of the cool things you can do with Cloudera Manager via the API:

Deploy an entire Hadoop cluster programmatically. Cloudera Manager supports HDFS, MapReduce, YARN, ZooKeeper, HBase, Hive, Oozie, Hue, Flume, Impala, Solr, Sqoop, Spark and Accumulo.
Configure various Hadoop services and get config validation.
Take admin actions on services and roles, such as start, stop, restart, failover, etc. Also available are the more advanced workflows, such as setting up high availability and decommissioning.
Monitor your services and hosts, with intelligent service health checks and metrics.
Monitor user jobs and other cluster activities.
Retrieve timeseries metric data.
Search for events in the Hadoop system.
Administer Cloudera Manager itself.
Download the entire deployment description of your Hadoop cluster in a json file.
Additionally, with the appropriate licenses, the API lets you:

Perform rolling restart and rolling upgrade.
Audit user activities and accesses in Hadoop.
Perform backup and cross data-center replication for HDFS and Hive.
Retrieve per-user HDFS usage report and per-user MapReduce resource usage report.
