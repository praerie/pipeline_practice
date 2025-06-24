import re

class ShotData:
    def __init__(self, sequence, shot, camera, version):
        self.sequence = sequence
        self.shot = shot
        self.camera = camera
        self.version = version

    @property
    def shot_id(self):
        return f"{self.sequence}_{self.shot}_{self.camera}_{self.version}"

    @classmethod
    def from_id(cls, id_str):
        pattern = r"^(sq\d{3})_(s\d{3})_(cam\d{3})_(v\d{3})$"
        match = re.match(pattern, id_str)
        if match:
            return cls(*match.groups())
        return None

    @classmethod
    def from_metadata(cls, metadata):
        if all(key in metadata for key in ["sequence", "shot", "camera", "version"]):
            return cls(
                metadata["sequence"],
                metadata["shot"],
                metadata["camera"],
                metadata["version"]
            )
        return None

    def __repr__(self):
        return f"<ShotData {self.shot_id}>"

# shot data demo
if __name__ == "__main__":
    print("From ID:")
    shot1 = ShotData.from_id("sq200_s100_cam001_v002")
    print(shot1)

    print("\nFrom Metadata:")
    metadata = {
        "sequence": "sq200",
        "shot": "s100",
        "camera": "cam001",
        "version": "v002"
    }
    shot2 = ShotData.from_metadata(metadata)
    print(shot2)
