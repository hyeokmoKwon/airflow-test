from airflow import DAG
  
global_dag = DAG('global_dag')

def local_dag():
  local_dag = DAG('local_dag')

local_dag()
