import re

class ShotData:
    def __init__(self, sequence, shot, camera, version):
        self.sequence = sequence      # e.g. "sq200"
        self.shot = shot              # e.g. "s100"
        self.camera = camera          # e.g. "cam001"
        self.version = version        # e.g. "v002"

    @property
    def shot_id(self):
        return f"{self.sequence}_{self.shot}_{self.camera}_{self.version}"

    @classmethod
    def from_metadata(cls, metadata):
        required_fields = ["sequence", "shot", "camera", "version"]
        missing_fields = [field for field in required_fields if field not in metadata]

        if missing_fields:
            raise ValueError(f"Missing metadata field(s): {', '.join(missing_fields)}")

        return cls(
            sequence=metadata["sequence"],
            shot=metadata["shot"],
            camera=metadata["camera"],
            version=metadata["version"]
        )

    @classmethod
    def from_id(cls, id_str):
        # expecting format: "sq200_s100_cam001_v002"
        pattern = r"^(sq\d{3})_(s\d{3})_(cam\d{3})_(v\d{3})$"
        match = re.match(pattern, id_str)  # match id_str against pattern from start (^) to finish ($)
        if not match:
            raise ValueError(f"Invalid ID format: {id_str}")
        return cls(*match.groups())  # returns tuple of all captured groups from regex pattern

    def __repr__(self):
        return f"<ShotData {self.shot_id}>"

# mock scene object simulating metadata
class MockScene:
    def __init__(self, metadata=None):
        self._metadata = metadata

    def get_metadata(self):
        return self._metadata

# load ShotData from scene
def load_shot_data_from_scene(scene):
    metadata = scene.get_metadata()

    if not metadata:
        print("Scene has no metadata. Likely not a valid shot file.")
        return None

    try:
        shot_data = ShotData.from_metadata(metadata)
        print(f"Loaded shot: {shot_data.shot_id}")
        return shot_data
    except ValueError as e:
        print(f"Metadata error: {e}")
        return None

# shot data demo
if __name__ == "__main__":
    valid_metadata = {
        "sequence": "sq200",
        "shot": "s100",
        "camera": "cam001",
        "version": "v002"
    }

    invalid_metadata = {
        "sequence": "sq200",
        "shot": "s100"
        # missing camera
        # missing version
    }

    scene_with_metadata = MockScene(valid_metadata)
    scene_without_metadata = MockScene(invalid_metadata)
    scene_empty = MockScene()

    print("\nValid Metadata:")
    load_shot_data_from_scene(scene_with_metadata)

    print("\nInvalid Metadata:")
    load_shot_data_from_scene(scene_without_metadata)

    print("\nEmpty Metadata:")
    load_shot_data_from_scene(scene_empty)

    print("\nCreate from ID:")
    try:
        shot = ShotData.from_id("sq100_s020_cam002_v005") 
        print(f"Shot from ID: {shot}")
    except ValueError as e:
        print(e)
