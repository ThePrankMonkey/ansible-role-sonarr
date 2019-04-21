sonarr
=========

Installs Sonarr.

Requirements
------------

* CentOS
* Internet Connected

Role Variables
--------------

```bash
sonarr_url: http://update.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz.linux.tar.gz
```

Example Playbook
----------------

```plain
- hosts: sonarr
  roles:
  - {name: sonarr, become: yes}
```

References
----------

* [Sonarr](https://github.com/Sonarr/Sonarr)
