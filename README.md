**Azure ETL Pipeline**

The Azure ETL Pipeline project demonstrates a comprehensive data pipeline using various Azure services and open-source technologies. The pipeline processes raw data stored in Azure Data Lake Storage Gen2, orchestrates data movement and transformation using Azure Data Factory and Apache Airflow, processes the data with PySpark, and stores the processed data in Azure Synapse Analytics for further analysis.

**Architecture Diagram**

![image](https://github.com/omkudale9198/azure-etl-pipeline/assets/68637380/93fa332c-2d3f-4b3a-90bd-ee1f0dfa683b)


Key Components
1.	Azure Data Lake Storage Gen2:
o	Stores raw data files (e.g., CSV, JSON) which are the input for the pipeline.
2.	Azure Data Factory (ADF):
o	Orchestrates and automates the data movement and transformation processes.
o	Integrates with other Azure services to schedule and trigger data processing jobs.
3.	Apache Airflow:
o	Manages the workflow and scheduling of the ETL processes.
o	Defines workflows using Directed Acyclic Graphs (DAGs) to ensure tasks are executed in the correct order.
4.	PySpark:
o	Performs the core data processing and transformation tasks.
o	Reads data from ADLS Gen2, transforms it, and prepares it for storage in Azure Synapse Analytics.
5.	Azure Synapse Analytics:
o	Serves as the final destination for the processed data.
o	Provides powerful querying and analytics capabilities to derive insights from the data.


## Setup Instructions

1. Clone the repository:
    ```
    git clone https://github.com/omkudale9198/azure-etl-pipeline.git
    ```

2. Navigate to the project directory:
    ```
    cd data-pipeline-project
    ```

3. Create and activate a virtual environment (optional but recommended):
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

5. Configure your settings in `config/config.json`.

6. Set up Airflow:
    ```
    export AIRFLOW_HOME=$(pwd)/airflow
    airflow db init
    airflow users create --username admin --firstname FIRST_NAME --lastname LAST_NAME --role Admin --email admin@example.com
   
airflow webserver --port 8080
airflow scheduler
```

7. Set up Azure Data Factory (ADF) and Azure Synapse Analytics:
- Follow the official Azure documentation to create and configure your Data Factory and Synapse Analytics workspace.
- Use the script scripts/adf_pipeline.py to automate pipeline creation in ADF.

8. Run your PySpark job manually or schedule it using Airflow:

python src/data_processing/process_data.py

Usage
Airflow: Navigate to http://localhost:8080 to access the Airflow UI. Here you can trigger DAGs, monitor your workflows, and manage task instances.
Azure Data Factory: Use the Azure portal to monitor and manage your data factory pipelines.
Azure Synapse Analytics: Access your Synapse workspace through the Azure portal to query and analyze the processed data.
Project Components
PySpark: Used for data processing.
Azure Data Factory: Used to orchestrate and automate data movement and transformation.
Azure Data Lake Storage Gen2: Used to store raw and processed data.
Apache Airflow: Used for job scheduling and workflow management.
Azure Synapse Analytics: Used to store and analyze processed data.
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License.

Contact
If you have any questions or need further assistance, please contact omkudale9198@gmail.com
