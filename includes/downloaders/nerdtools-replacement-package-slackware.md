<!-- markdownlint-disable MD041-->
#### Instructions

In your Unraid terminal, type the following to determine your Slackware version.

```bash
cat /etc/slackware-version
```

Then go to [https://packages.slackware.com/](https://packages.slackware.com/){:target="\_blank" rel="noopener noreferrer"} to find the correct 64-bit version of the required package.<br>
Download it and add it to your Unraid flash drive located in the `boot/extra` folder. It will be installed upon Unraid boots.

Currently:

- `Slackware64 15.0` for `unRAID 6.x`
- `Slackware64 current` for `unRAID 7.x`

!!! info "To remove the old/wrong packages (that NerdTools installed for an earlier Slackware version), overwrite them with the new versions on your Unraid flash drive in the `boot/extra` folder. Place the correct versions there and then reboot."
<!-- markdownlint-enable MD041-->
