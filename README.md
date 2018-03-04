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

If the target server has SELinux enabled, install the SELinux packages from OS.
We recommend using the role [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/).


Role Variables
--------------
| Variable | Default Value| Description | Required|
|---------|--------------|-------------|---------|
| gcs_proxy_instances| YOUR INSTANCE CONNECTION NAME | Google Cloud SQL instance name | Yes |
| gcs_proxy_credential_file | <PATH_TO_KEY_FILE> | Path to key file on the remtote server | No |
| gcsql_proxy_configure_selinux | false | Ensure Google Cloud SQL Proxy runs when SELinux is enabled | No |

Dependencies
------------
None.
We recommend using the role [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/)

Example Playbook
----------------

```yml
  - hosts: servers
    vars:
      - gcs_proxy_instances: <YOUR INSTANCE CONNECTION NAME>
      - gcs_proxy_credential_file: <PATH_TO_KEY_FILE>
      - centos_base_install_selinux_packages: true
    remote_user: <YOUR REMOTE USER>
    become: yes
    roles:
      - bngsudheer.gcsql_proxy
```

Developement
------------
To run molecule tests locally, you might want to set the ANSIBLE_ROLES_PATH
  variable.
```sh
export ANSIBLE_ROLES_PATH=/path/to/ansible-role-redmine/molecule/default/roles
```

License
-------

BSD

Sudheer Satyanarayana
* Blog: https://www.techchorus.net
* Twitter: https://www.twitter.com/bngsudheer
* Work: https://www.gavika.com
