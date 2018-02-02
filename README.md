Role Description
=========

Role to install Google Cloud Proxy on Google Cloud Compute instance. 
See Google's documentation on [connecting to Cloud SQL from Compute Engine](https://cloud.google.com/sql/docs/mysql/connect-compute-engine). 

Starting And Stopping The service
----------------
```sh
systemctl start gcsql_proxy
```
```sh
systemctl stop gcsql_proxy
```

Requirements
------------
None.
We recommend using the role [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/).

Role Variables
--------------
|Variable | Default Value| Description | Required|
|---------|--------------|-------------|---------|
|gcs_proxy_instances| YOUR INSTANCE CONNECTION NAME | Google Cloud SQL instance name | Yes |
|gcs_proxy_credential_file | <PATH_TO_KEY_FILE> | Path to key file on the remtote server | No |

Dependencies
------------
None.
We recommend using the role [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/)

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yml
  - hosts: servers
    vars: 
      - gcs_proxy_instances: <YOUR INSTANCE CONNECTIO NAME>
      - gcs_proxy_credential_file: <PATH_TO_KEY_FILE>
    remote_user: <YOUR REMOTE USER>
    become: yes
    roles:
      - bngsudheer.gcsql_proxy 
```

License
-------

BSD

Sudheer Satyanarayana
* Blog: https://www.techchorus.net
* Twitter: https://www.twitter.com/bngsudheer
* Work: https://www.gavika.com
