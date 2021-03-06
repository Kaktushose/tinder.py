class Album:
    __slots__ = ["album_id", "name", "_images"]

    def __init__(self, album: dict):
        self.album_id = album["id"]
        self.name = album["name"]
        images = dict()
        for image in album["images"]:
            images[image["height"]] = image["url"]
        self._images = tuple(images)

    def image_url(self, resolution: int = 640) -> str:
        return self._images[resolution]


class Track:
    __slots__ = ["track_id", "name", "album", "preview_url", "uri"]

    def __init__(self, track: dict):
        self.track_id = track["id"]
        self.name = track["name"]
        self.album = Album(track["album"])
        self.preview_url = track["preview_url"]
        self.uri = track["uri"]


class TopArtist:
    __slots__ = ["artist_id", "name", "selected", "top_track"]

    def __init__(self, artist: dict):
        self.artist_id = artist["id"]
        self.name = artist["name"]
        self.selected = artist["selected"]
        self.top_track = Track(artist["top_track"])
