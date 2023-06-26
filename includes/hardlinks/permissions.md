### Permissions

Change the ownership (`chown`) and the mode (`chmod`) for the `/data` folder and all of its subfolders (recursively).

??? tip "chown and chmod Tips - [CLICK TO EXPAND]"

    - Use `chown` to set the owner in the below commands to be the user (`$USER`) and group (`:$USER`) that will be running the services.
      - For example, the `PUID` and `GUID` in a service's Docker file will show you the user and group the service is running as, respectively.
      - It is beneficial in this case to run all relevant services as the same user and group
    - Use `'chmod` to change the mode (permissions) of `/data` to 775 or 664
      - `775` will grant the user and its group read, write, and execute permissions, and will grant read and execute permissions to all others
      - `664` will grant read and write permissions for the owner and its group, and will grant read permissions to all others
    - Review the [Servarr Wiki](https://wiki.servarr.com/docker-guide#recursively-chown-user-and-group){:target="_blank"} for more information on setting folder permissions.

```bash
sudo chown -R $USER:$USER /data
sudo chmod -R a=,a+rX,u+w,g+w /data
```
