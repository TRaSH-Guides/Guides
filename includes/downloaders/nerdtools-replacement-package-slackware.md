<!-- markdownlint-disable MD041-->
#### Instructions

In your Unraid terminal, type the following to determine your Slackware version.

```bash
cat /etc/slackware-version
```

Then go to [https://packages.slackware.com/](https://packages.slackware.com/){:target="\_blank" rel="noopener noreferrer"}

![Slackware v15 Search](images/slackware-search-v15.png)

1. Select the correct 64-bit Slackware version from the release dropdown box.

    Currently:

    - `Slackware64 15.0` for `unRAID 6.x`
    - `Slackware64 current` for `unRAID 7.x`

1. Type in the required package you're looking for in the search box.
1. Download the required packages.

Put them in your Unraid flash drive located in the `boot/extra` folder. It will be installed upon Unraid boots.

!!! info "To remove the old/wrong packages (that NerdTools installed for an earlier Slackware version), overwrite them with the new versions on your Unraid flash drive in the `boot/extra` folder. Place the correct versions there and then reboot."
<!-- markdownlint-enable MD041-->
