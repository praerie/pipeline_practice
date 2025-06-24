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

    def __repr__(self):
        return f"<ShotData {self.shot_id}>"

# Example
if __name__ == "__main__":
    shot = ShotData.from_id("sq200_s100_cam001_v002")
    print(shot)
