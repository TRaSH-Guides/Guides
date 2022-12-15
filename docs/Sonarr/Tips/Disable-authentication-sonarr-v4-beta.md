# Sonarr V4 Mandatory Authentication
!!! danger "**Warning: This is ONLY to be used if you have an external authentication service. Most top level indexers and trackers are now requiring authentication in front of Sonarr. Disabling authentication with no third party solution may result in issues with connection to your indexers or trackers**"

With the beta release of Sonarr V4, if your sonarr instance is accessible externally you are now required to add authentication to your Sonarr instance.

This is great in practice to ensure your instance is secure, however some users may be using an external authentication service (Authentik, Authelia, Keycloak) and do not want to have to authenticate twice.

Sonarr has added an Authentication of type "External" to allow users to bypass the built-in Sonarr authentication if you are using one of these services, however, this option is not selectable from the UI when you first set up your Sonarr V4 instance.

To set this, navigate to your `config.xml` file where you store your Sonarr appData and add the following line:

```xml
<AuthenticationMethod>External</AuthenticationMethod>
```

This will bypass the built-in authentication entirely and allow you to rely solely on your external authentication service.

{! include-markdown "../../../includes/support.md" !}
