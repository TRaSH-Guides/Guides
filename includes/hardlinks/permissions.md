### Permissions

Recursively chown user and group and Recursively chmod to 775/664

```bash
sudo chown -R $USER:$USER /data
sudo chmod -R a=,a+rX,u+w,g+w /data
```
