# Installation

Installing AniLinkPy is straightforward. The recommended approach is to use a project manager like Poetry or Hatch, as these tools provide a clean, isolated environment for your project. Alternatively, you can use pipx, which automatically sandboxes your pip installations into separate environments. If you prefer to use pip, you can install AniLinkPy directly as well.

=== "Poetry"

    In `pyproject.toml`:
    
    ```bash
    [tool.poetry.dependencies]
    AniLinkPy = "*" # (1)!
    ```

    1.  The `*` will install the latest version of AniLinkPy. You can also specify a version number to install a specific version. 

        !!! example "Specifying a Version"
            ```bash
            [tool.poetry.dependencies]
            AniLinkPy = "1.0.0"
            ```

=== "Hatch"

    In `pyproject.toml`:
    
    ```bash
    dependencies = [
        "AniLinkPy" # (1)!
    ]
    ```

    1.  To install a specific version of AniLinkPy, you can specify the version number in the dependencies list:
    
        !!! example "Specifying a Version"
            ```bash
            dependencies = [
                "AniLinkPy==1.0.0"
            ]
            ```

=== "pipx"

    Run the following command in your terminal:    

    ```bash
    pipx install AniLinkPy # (1)!
    ```
    
    1.  To install a specific version of AniLinkPy, you can specify the version number with the package name:
        
        !!! example "Specifying a Version"
            ```bash
            pipx install AniLinkPy==1.0.0
            ```

=== "Pip"

    Run the following command in your terminal:    

    ```bash
    pip install AniLinkPy # (1)!
    ```
    
    1.  To install a specific version of AniLinkPy:
    
        !!! example "Specifying a Version"
            ```bash
            pip install AniLinkPy==1.0.0
            ```

## Initialization

To start using AniLink, you need to import it and initialize it with an optional authentication token. You can get an authentication token from the respective platform (e.g. AniList).

!!! example "Importing & Initializing AniLink"

    ```python
    from AniLinkPy import AniLink

    auth_token = 'your-auth-token' # (1)!
    aniLink = AniLink(auth_token)
    ```

    1.  Please replace `'your-auth-token'` with your actual authentication token.

    You can also initialize AniLink without an authentication token
    
    ```python
    aniLink = AniLink()
    ```