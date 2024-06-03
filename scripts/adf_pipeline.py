from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient

def create_pipeline():
    subscription_id = '<your_subscription_id>'
    resource_group_name = '<your_resource_group>'
    data_factory_name = '<your_data_factory_name>'
    pipeline_name = 'ExamplePipeline'

    credentials = DefaultAzureCredential()
    adf_client = DataFactoryManagementClient(credentials, subscription_id)

    # Define your pipeline here

    adf_client.pipelines.create_or_update(resource_group_name, data_factory_name, pipeline_name, pipeline)
    print(f'Pipeline {pipeline_name} created successfully.')

if __name__ == "__main__":
    create_pipeline()
