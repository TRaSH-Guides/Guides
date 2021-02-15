# Better Uptime Integration

> This integration allows for notifications from Better Uptime utilizng their webhook system

---

## Trigger options
![!triggers-channels](images/Better-Uptime/triggers-channels.png "Triggers and Channels")

1. Triggers
    - `Started` - Sent when Better Uptime detects an issue with a site you are monitoring
    - `Ack` (Acknowledged) - Sent when you mark the issue as acknowledged through Better Uptime
    - `Resoled` - Sent when the site you are monitoring returns a successful response
1. Channel
    - Pick a channel from your server to send these notifications

---

## Configuration
![!open-configuration](images/Better-Uptime/open-configuration.png "Open Configuration Window")

Click the **cog icon** to open the configuration options for Better Uptime.

![!configuration](images/Better-Uptime/configuration.png "Configuration Window")

1. Notification colors for each trigger type
1. Notification content options that you can turn on/off to show in the notifications
1. Better Uptime team id that is used to link the Incident in the notification

**NOTE:** This integration sends a single notification for all triggers. After the first one is sent, the rest will update the existing notification in the chain.