from airflow.operators.email import EmailOperator
from airflow.operators.bash import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "untitled-1012141548",
}

dag = DAG(
    "untitled-1012141548",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.12.0 pipeline editor using `untitled.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "airflow-package-catalog", "component_ref": {"airflow_package": "apache_airflow-2.4.1-py3-none-any.whl", "file": "airflow/operators/bash.py"}}

op_0e0de2ff_3af3_4ecf_9af1_2ca1afeb7215 = BashOperator(
    task_id="Test_Bash_Operator",
    bash_command="echo 123456",
    env={},
    append_env=False,
    output_encoding="utf-8",
    skip_exit_code=99,
    cwd="",
    executor_config={},
    dag=dag,
)


# Operator source: {"catalog_type": "airflow-package-catalog", "component_ref": {"airflow_package": "apache_airflow-2.4.1-py3-none-any.whl", "file": "airflow/operators/email.py"}}

op_929fd5c0_77f8_49d3_931b_502e38700d99 = EmailOperator(
    task_id="Send_email",
    to="[bac.do@evizi.com]",
    subject="test from elyra",
    html_content="OK, you are good",
    files="",
    cc="",
    bcc="",
    mime_subtype="mixed",
    mime_charset="utf-8",
    conn_id="",
    custom_headers={},
    executor_config={},
    dag=dag,
)

op_929fd5c0_77f8_49d3_931b_502e38700d99 << op_0e0de2ff_3af3_4ecf_9af1_2ca1afeb7215
