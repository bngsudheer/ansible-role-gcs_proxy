Role Name
=========

Role to install Google Cloud Proxy on Google Cloud Compute instance. 
See Google's documentation on [connecting to Cloud SQL from Compute Engine](https://cloud.google.com/sql/docs/mysql/connect-compute-engine). 

Requirements
------------

None.
We recommend using the role [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/).

Role Variables
--------------

* gcs_proxy_instances: <YOUR INSTANCE CONNECTIO NAME>
* gcs_proxy_credential_file: <PATH_TO_KEY_FILE>

Dependencies
------------

None.
We recommend using the role [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/)

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      vars: 
	- gcs_proxy_instances: <YOUR INSTANCE CONNECTIO NAME>
	- gcs_proxy_credential_file: <PATH_TO_KEY_FILE>
      remote_user: <YOUR REMOTE USER>
      become: yes
      roles:
         - bngsudheer.gcsql_proxy 

License
-------

BSD

Author Information
------------------
Sudheer Satyanarayana
Blog: http://www.techchorus.net
Twitter: http://www.twitter.com/bngsudheer
