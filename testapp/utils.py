import requests


def undotted_keys(dict):
    """
    Transform dotted keys to undotted keys. This is for the `.tag` key
    in the dict that Dropbox returns.
    """
    return {k.lstrip("."): v for k, v in dict.items()}


def dropbox_list_folder(user, path=""):
    """
    Returns a generator of files and subfolders for the given folder.
    """
    social_auth = user.social_auth.filter(provider="dropbox-oauth2").first()
    if not social_auth:
        raise ValueError("user is not authorized with Dropbox")
    headers = {
        "Authorization": "Bearer {token}".format(token=social_auth.access_token),
        "Content-Type": "application/json",
    }
    response = requests.post(
        url="https://api.dropboxapi.com/2/files/list_folder",
        headers=headers,
        json={"path": path},
    )
    response.raise_for_status()
    content = response.json()
    for entry in content['entries']:
        yield undotted_keys(entry)

    while content['has_more']:
        response = requests.post(
            url="https://api.dropboxapi.com/2/files/list_folder/continue",
            headers=headers,
            json={"cursor": content["cursor"]},
        )
        response.raise_for_status()
        content = response.json()
        for entry in content['entries']:
            yield undotted_keys(entry)
