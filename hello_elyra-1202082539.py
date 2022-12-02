from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.volume_mount import VolumeMount
from airflow.contrib.kubernetes.volume import Volume
from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "hello_elyra-1202082539",
}

dag = DAG(
    "hello_elyra-1202082539",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.12.0 pipeline editor using `hello_elyra.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: work/hello.ipynb

op_b267cc58_e7dd_49f6_8dd0_10aab3f0c457 = KubernetesPodOperator(
    name="hello",
    namespace="airflow",
    image="continuumio/anaconda3:2021.11",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'hello_elyra' --cos-endpoint http://34.204.52.237:9000 --cos-bucket minio-pipeline --cos-directory 'hello_elyra-1202082539' --cos-dependencies-archive 'hello-b267cc58-e7dd-49f6-8dd0-10aab3f0c457.tar.gz' --file 'work/hello.ipynb' "
    ],
    task_id="hello",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "hello_elyra-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)
