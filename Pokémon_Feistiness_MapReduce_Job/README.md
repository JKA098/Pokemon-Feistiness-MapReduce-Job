# 🏆 Pokémon Feistiness MapReduce Job

![Big Data](https://img.shields.io/badge/domain-Big%20Data%20-red)
![Analytics](https://img.shields.io/badge/focus-Data%20Analytics-blueviolet)
![Big Data Stack](https://img.shields.io/badge/tech%20stack-Hadoop%2FMapReduce%2FStreaming-lightblue)
![Environment](https://img.shields.io/badge/setup-Virtual%20Environment-important)
![Isolation](https://img.shields.io/badge/dependency%20isolation-Virtualenv%20%2F%20venv-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Focus](https://img.shields.io/badge/focus-MapReduce%20Feistiness%20Analysis-blueviolet)
![Theme](https://img.shields.io/badge/theme-Pok%C3%A9mon%20Feistiness-brightgreen)
![Data](https://img.shields.io/badge/data%20source-pokemon.csv-lightgrey)
![Statistics](https://img.shields.io/badge/statistical%20metrics-Attack%2FWeight-blue)
![ML](https://img.shields.io/badge/hadoop%20mode-Pseudo--Distributed-orange)
![Framework](https://img.shields.io/badge/framework-Hadoop%20Streaming-informational)
![Notebook](https://img.shields.io/badge/editor-Ubuntu%20Terminal-orange)
![Editor](https://img.shields.io/badge/report-MS%20Excel-blue)


## **📌 Project Overview**
This Project aims to implement a **Hadoop MapReduce job in Pseudo-Distributed Mode** to determine the **feistiest Pokémon** based on their **type**. 
The job processes the Pokémon dataset (`pokemon.csv`) and outputs a CSV file containing Pokémon **type1, type2, name, and feistiness score**.

---


---

## **📁 Project Structure**
📂 Project/ 

│── 📄 pokemon.csv # Input dataset

│── 📄 mapper1.py # The code for the Mapper 

│── 📄 reducer.py # The code for the Reducer 

│── 📄 run_pokemon_mapreduce.sh # The code for the Bash script to run MapReduce job 

│── 📄 results.csv # The name of the Final output which is a csv file 

│── 📄 results_fesitest.csv # The name of the final document with feistiest pokemon

│── 📄 README.md # This documentation



---

## **📌 Installation & Setup**

### *** All of the following setup steps, assume that your VirtualBox or other VM software are already installed and running. Further, the following steps are to be performed inside Ubuntu***

### **1️⃣ Prerequisites**
make sure the following softwares are installed:
- **Ubuntu 24.04** (Recommended inside VirtualBox)
- **Hadoop 3.4.1**
- **Python 3**
- **OpenJDK 8** 
- **SSH** for Hadoop execution

### **2️⃣ Install Java (OpenJDK 8)**
```bash

sudo apt install openjdk-8-jdk
```
Verify Java version:

```bash
java version
```

✅ Expected Output:
```bash
openjdk version "1.8.0_442"
```

---

### **3️⃣ Install SSH (Required for Hadoop)**
```bash
# install ssh if not already installed
sudo apt-get install ssh
sudo apt-get install pdsh
```

### **4️⃣ Verify Hadoop Installation**
Check if Hadoop is installed by running:
```bash
hadoop version
```
✅ Expected Output:
```bash
Hadoop 3.4.1 
```
If not:
 **Navigate to the official website and download it**

### **5️⃣ Verify Python Installation**
```bash
python3 --version
```
✅ Expected Output:
```bash
python version "3.x.x"
```
If not present, install python:
``` bash
sudo apt update  # Update the package list
sudo apt install python3  # Installs Python 3

```

________________________________________
## **📌 Configure the Hadoop files**

**The following are all required configuration so that Hadoop can work.** And you should follow the following link, and configure your hadoop environment: https://arjunkrish.medium.com/step-by-step-guide-to-setting-up-hadoop-on-ubuntu-installation-and-configuration-walkthrough-60e493e9370d


### **1️⃣ Set Java Path in Hadoop**
 

```bash
nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh
# set to the root of your Java installation
# scroll down, and you should see it.
# if not add it at the bottom
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```
Save and exit (CTRL+X, then Y, then ENTER).


### **2️⃣ Configure core-site.xml**
```bash
nano $HADOOP_HOME/etc/hadoop/core-site.xml
```

``` bash
# add the following
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```
Save and exit (CTRL+X, then Y, then ENTER).



### **3️⃣ Configure hdfs-site.xml**
```bash
nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```
``` bash
# add the following
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```
Save and exit (CTRL+X, then Y, then ENTER).


### **4️⃣ Configure mapred-site.xml**
```bash
nano $HADOOP_HOME/etc/hadoop/mapred-site.xml
```

```bash
# add the following
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>mapreduce.application.classpath</name>
        <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
    </property>
</configuration>
```
Save and exit (CTRL+X, then Y, then ENTER).



### **5️⃣ Configure yarn-site.xml**
```bash
nano $HADOOP_HOME/etc/hadoop/yarn-site.xml
```
``` bash
# add the following
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>mapreduce.application.classpath</name>
        <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
    </property>
</configuration>
```
Save and exit (CTRL+X, then Y, then ENTER).


________________________________________
## **📌 Running Hadoop**


### **1. Check that you can ssh to the localhost without a passphrase:**

```bash
# run
ssh localhost
```

### **If you cannot ssh to localhost without a passphrase, execute the following commands:**

```bash
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
```

### **Tips:**
After running the ssh, run:
```bash
ls
# find hadoop folder
cd hadoop_folder
# then run the following command
bin/hdfs namenode -format
```

### **2. Start NameNode daemon and DataNode daemon:**
```bash
sbin/start-dfs.sh
```

### **Browse the web interface for the NameNode:**
```
# NameNode - http://localhost:9870/
```

#### At this point if you have done everything correctly, the above web interface should work. If not double check that everything is correct first and then proceed to debugging.

### **3. Make the HDFS directories required to execute MapReduce jobs:**
```bash
bin/hdfs dfs -mkdir -p /user/<username> # replace username with your environment user name. Tips: run "whoami"
```

### **4. Start ResourceManager daemon and NodeManager daemon:**
```bash
sbin/start-yarn.sh
```

### **5.Browse the web interface for the ResourceManager; by default it is available at:**
```
ResourceManager - http://localhost:8088/

```
### **6. Check running services**

*Tips: use the following command:*
```bash
jps
```
*Will allow you to see all the resources that are running.*

✅ Expected Output:
```bash
NameNode
DataNode
SecondaryNameNode
ResourceManager
NodeManager
```

#####################################
### **At this point, that is where you should stop your NameNode, DataNode, ResourceManager and NodeManager daemon. However, we still have to load our mapper, and reducer to start the actual job. As such keep them open. We will shut them down at thend.**

#####################################



________________________________________
## **📌 Running the MapReduce Job**


### **0. Navigate to Your Working Directory**
```bash
# this is a continuation from what you have done so far.
# if you know the absolute path for your working directory use it in the code bellow
cd ~/your/working/directory/inside/ubuntu

# the above directory, should be different from the hadoop directory.
# choose any, so long as you keep using it.


# else, use:
cd .. 
# until you are outside the hadoop directory.
ls
# to find the directories and
cd
# navigate to your desired directory


# lastly use the following command to show all the files inside your directory
ls
```

✅ Expected Output:

```bash
mapper1.py  reducer.py  pokemon.csv  run_pokemon_mapreduce.sh
# In this case, I have copied my files already in my working directory that I am using for this Mapreduce job ahead of time.
# but if you have not done it ahead of time. You should see something different.
```



### **1️⃣ Export Hadoop Configuration (If not done yet, else skip)**
```bash
# the hadoop directory is where there are the needed files
# that are used to run hadoop
# where the type of mode is specified: Standalone, 
# Pseudo-distributed, or Fully Distributed
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
```

### **2️⃣ Ensure Mapper, Reducer and bash file can be excuted**
```bash
# this is important, everytime you start the job
# you must run this command
chmod +x mapper1.py reducer.py run_pokemon_mapreduce.sh
```


### **3️⃣ Run the Mapper Separately**
```bash
# this allows you to see if they are working
cat pokemon.csv | mapper1.py
```
✅ Expected output (First Few Lines):
```bash
# this the ouput you should get
grass,poison,Bulbasaur,7.10
fire,flying,Charizard,1.15
...

```

### **4️⃣ Run the Reducer Separately**
```bash
cat pokemon.csv | reducer.py
```
✅ Expected output (First Few Lines):
```bash
type1,type2,name,feistiness
grass,poison,Bulbasaur,7.10
fire,flying,Charizard,1.15
...

```

### **5️⃣ Run the Hadoop Streaming Job**

```bash
# if this code outputs: FAILED
# double check the files in HADOOP_CONF_DIR
# make sure thy are set to run the appropriate mode
./run_pokemon_mapreduce.sh
```

✅ Expected Output:
```bash
INFO streaming.StreamJob: Output directory: pokemon_output
```

### **6️⃣ Verify Output Directory**
```bash
ls -l pokemon_output/
```

✅ Expected Output:
```bash
_SUCCESS
#part-00000: this part contains final results
#_SUCCESS: this confirms that the job completed successfully
```


### **7️⃣ Save Output as CSV**
```bash
# this code is slightly redundant.
# but it makes sure that if the './run_pokemon_mapreduce.sh'
# does not copy the output to the desired the csv file automatically
# you can stimply copy the output manually

cp pokemon_output/part-00000 results.csv
```

### **8.When done stop the NameNode daemon and DataNode daemon with:**
```bash
sbin/stop-dfs.sh
```
### **9.And the ResourceManager daemon and NodeManager daemon with:**
```bash
sbin/stop-yarn.sh
```
*Tips: using the following command:*
```bash
stop-all.sh 
```
*Also works.*


✅ The final results are now saved in results.csv.

### **10.The rest is simple excel skills:**
- Make a copy of the resulting results.csv
- Go through it.
- Group by type 1. 
- Look for the feistiest Pokémon for each type 1.
- Select them.
- Make new csv document: **results_fesitest.csv**, which contains the feistiest Pokémon for each type 1
- Save results

________________________________________

### **📌 Summary of how the Code Works**


🖥 Mapper (mapper1.py)
1.	Reads the input CSV (pokemon.csv).
2.	Extracts relevant columns: type1, type2, name, attack, weight.
3.	Calculates Feistiness (attack/weight).
4.	Outputs type1,type2,name,feistiness.

🖥 Reducer (reducer.py)

1.	Reads Mapper Output from stdin.
2.	Replaces missing type2 values with "unknown".
3.	Sorts Pokémon by name .

🖥 Bash Script (run_pokemon_mapreduce.sh)

1.	Deletes old output (pokemon_output/).
2.	Runs Hadoop Streaming Job.
3.	Sorts results by Pokémon name.
4.	Saves sorted results as results.csv.

🖥 Excell (results_fesitest.csv)
1. Make a duplicate of results.csv
2. Select the fesitest Pokémon for each type
3. Saves results as results_fesitest.csv



...


________________________________________
# 📌 Important information #

1. **Java Compatibility**:  Initially, per assignment outline, we were supposed to use **OpenJDK 21**, however several issues were encountered were some parts would not work or would not show up. And after some research, suggested there might be some compatibility issues between **OpenJDK 21** and **Hadoop 3.4.1** . Therefore,  **OpenJDK8**, was used instead. 

2. **Reducer code**: initially it was grouping by **type 1** and some errors would happen, whereby, some data would be missing. And after changing and trying the code, the grouping was done by **Pokémon name** instead. Afterwards, it turned out that changing to group by **type 1** would not be difficult, but due to the fact that other elements were not working properly, to avoid introducing any more mistakes that would make debugging complicated, it was decided to leave it be, and use excel to find the **feistiest Pokémon** for each **type1**.

3. **Development Environment**: at first the Hadoop job began in a ** Local (Standalone) Mode**. But in the end, I changed to a ** Pseudo-Distributed Mode**, which meant making all the required changes.

4. **Mode Differentiation**: Mostly because I had assumed that; working in a  ** Local (Standalone) Mode**, would be the same thing as a ** Pseudo-Distributed Mode**. I did not pay much attention to it. However it turned out to be extremely different. But for the purpose of learning how Hadoop works, and knowing how to use it. It was extremely useful. And I was able to test the mapper code, the reducer code, and the bash file(run_pokemon_mapreduce.sh), all of which were running perfectly.

5. **Pseudo-Distributed Mode Challenges**: Due to the fact that **Pseudo-Distributed Mode**, allow to make sure that a MapReduce job is capable of being executed in a massively parallel,  cluster environment with multiple mappers and reducers, it is a totally different from a **Local (Standalone) Mode**, and several issues were encountered while making sure it can work. Some were resolved, by making modifications to the bash file and others could not be resolved.

6. **Output inconsistency**: Despite the many challenges encountered, from time to time, after having changed to a **Pseudo-Distributed Mode**, sometimes the Hadoop job would work, and the resulting csv file would be the same as the one created with a **Local (Standalone) Mode**. 
As such even if everything did not work properly on my machine, at the very least, you can expect the **mapper1.py, reducer.py and run_pokemon_mapreduce.sh** to work properly and consistently on any other machine or virtual machine, that is properly configured. 
However, the expected output; under **Running the MapReduce Job**, beginning at **Run the Hadoop Streaming Job**, might be different on someone’s else machine. The reason being that, that is the expected output, I received when running a **Local (Standalone) Mode**, but since for **Pseudo-Distributed Mode**, several components would not work, or would work poorly. I would get different output. 
But, assuming that everything works properly, you should expect to get a similar output.

7. **Post-Processing**: In the end like already mentioned above, to get the required grouping by type1 and identify the **feistiest Pokémon**, within each group. A manual post-processing of **results.csv** was performed. The results were then extracted and saved into a different csv file: **results_fesitest.csv**.

8. Although not necessary. I was able to exchange files between my virtual environment and my local machine, by uploading and downloading files and folders to and from google drive.


________________________________________
🚀 Additional Debugging Steps

1️⃣ At this point, even if you have done everything correctly you will still get mistake. 
All you can do is read the error, even if you cannot understand them. 
Proceed to google the error, and see what you get, and try to apply it.
And happy coding.



________________________________________
📌 Summary: Key Steps 

✔ Ensure Ubuntu 24.04, Java & Hadoop 3.4.1 are installed.

✔ Set the required environment variables where needed.

✔ Make mapper, reducer and the bash executable (chmod +x).

✔ Run the python files, and then the bash file.

✔ Check _SUCCESS in pokemon_output/ to confirm job completion.

✔ Use cp or mv to transfer results into your desired file. If not already there.

✔ Use excell to select the fesitest Pokémon by type 1, and save to a different file

________________________________________

📜 All References are in a different pdf document.

---

📂 **Dataset Reference**  
This project uses the Pokémon dataset available on Kaggle:  
🔗 [https://www.kaggle.com/datasets/rounakbanik/pokemon](https://www.kaggle.com/datasets/rounakbanik/pokemon)

